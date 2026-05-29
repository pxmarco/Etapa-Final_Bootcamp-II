import os
import sys
import traceback
import uuid
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

import psycopg2
import psycopg2.extras
from psycopg2 import OperationalError

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from auth_utils import bearer_token, json_response, parse_token, read_json  # noqa: E402


def _connect():
    database_url = os.environ.get("DATABASE_URL") or os.environ.get("POSTGRES_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL ou POSTGRES_URL nao configurada.")
    return psycopg2.connect(database_url)


def _ensure_table(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id UUID PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS medications (
            id UUID PRIMARY KEY,
            user_id UUID REFERENCES users(id) ON DELETE CASCADE,
            name TEXT NOT NULL,
            time TEXT NOT NULL,
            dose TEXT NOT NULL DEFAULT '',
            note TEXT NOT NULL DEFAULT '',
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        )
        """
    )
    cursor.execute("ALTER TABLE medications ADD COLUMN IF NOT EXISTS user_id UUID")
    cursor.execute(
        """
        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1
                FROM pg_constraint
                WHERE conname = 'medications_user_id_fkey'
            ) THEN
                ALTER TABLE medications
                ADD CONSTRAINT medications_user_id_fkey
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;
            END IF;
        END $$;
        """
    )


def _current_user_id(headers):
    payload = parse_token(bearer_token(headers))
    if not payload:
        raise PermissionError("Faca login para acessar seus medicamentos.")
    return payload["sub"]


def _list_medications(user_id):
    with _connect() as connection:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            _ensure_table(cursor)
            cursor.execute(
                """
                SELECT id::text, name, time, dose, note
                FROM medications
                WHERE user_id = %s
                ORDER BY time, created_at
                """,
                (user_id,),
            )
            return cursor.fetchall()


def _create_medication(payload, user_id):
    name = str(payload.get("name", "")).strip()
    time = str(payload.get("time", "")).strip()
    dose = str(payload.get("dose", "")).strip()
    note = str(payload.get("note", "")).strip()

    if not name or not time:
        raise ValueError("Nome e horario sao obrigatorios.")

    medication = {
        "id": str(uuid.uuid4()),
        "user_id": user_id,
        "name": name,
        "time": time,
        "dose": dose,
        "note": note,
    }

    with _connect() as connection:
        with connection.cursor() as cursor:
            _ensure_table(cursor)
            cursor.execute(
                """
                INSERT INTO medications (id, user_id, name, time, dose, note)
                VALUES (%(id)s, %(user_id)s, %(name)s, %(time)s, %(dose)s, %(note)s)
                """,
                medication,
            )

    medication.pop("user_id")
    return medication


def _delete_medication(medication_id, user_id):
    if not medication_id:
        raise ValueError("Informe o id do medicamento.")

    with _connect() as connection:
        with connection.cursor() as cursor:
            _ensure_table(cursor)
            cursor.execute(
                "DELETE FROM medications WHERE id = %s AND user_id = %s",
                (medication_id, user_id),
            )
            return cursor.rowcount


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            user_id = _current_user_id(self.headers)
            json_response(self, 200, {"medications": _list_medications(user_id)})
        except PermissionError as exc:
            json_response(self, 401, {"error": str(exc)})
        except RuntimeError as exc:
            json_response(self, 503, {"error": str(exc)})
        except OperationalError:
            print(traceback.format_exc(), file=sys.stderr)
            json_response(
                self,
                503,
                {"error": "Conexao com Supabase indisponivel. Confira a Transaction Pooler URL."},
            )
        except Exception:
            print(traceback.format_exc(), file=sys.stderr)
            json_response(self, 500, {"error": "Nao foi possivel listar os medicamentos."})

    def do_POST(self):
        try:
            user_id = _current_user_id(self.headers)
            medication = _create_medication(read_json(self), user_id)
            json_response(self, 201, {"medication": medication})
        except PermissionError as exc:
            json_response(self, 401, {"error": str(exc)})
        except ValueError as exc:
            json_response(self, 400, {"error": str(exc)})
        except RuntimeError as exc:
            json_response(self, 503, {"error": str(exc)})
        except OperationalError:
            print(traceback.format_exc(), file=sys.stderr)
            json_response(
                self,
                503,
                {"error": "Conexao com Supabase indisponivel. Confira a Transaction Pooler URL."},
            )
        except Exception:
            print(traceback.format_exc(), file=sys.stderr)
            json_response(self, 500, {"error": "Nao foi possivel salvar o medicamento."})

    def do_DELETE(self):
        try:
            user_id = _current_user_id(self.headers)
            query = parse_qs(urlparse(self.path).query)
            deleted = _delete_medication(query.get("id", [""])[0], user_id)
            json_response(self, 200, {"deleted": deleted})
        except PermissionError as exc:
            json_response(self, 401, {"error": str(exc)})
        except ValueError as exc:
            json_response(self, 400, {"error": str(exc)})
        except RuntimeError as exc:
            json_response(self, 503, {"error": str(exc)})
        except OperationalError:
            print(traceback.format_exc(), file=sys.stderr)
            json_response(
                self,
                503,
                {"error": "Conexao com Supabase indisponivel. Confira a Transaction Pooler URL."},
            )
        except Exception:
            print(traceback.format_exc(), file=sys.stderr)
            json_response(self, 500, {"error": "Nao foi possivel remover o medicamento."})
