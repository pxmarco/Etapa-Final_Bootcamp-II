import os
import re
import sys
import traceback
import uuid
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

import psycopg2
import psycopg2.extras
from psycopg2 import OperationalError

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from auth_utils import (  # noqa: E402
    bearer_token,
    create_token,
    hash_password,
    json_response,
    parse_token,
    public_user,
    read_json,
    verify_password,
)


EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def _connect():
    database_url = os.environ.get("DATABASE_URL") or os.environ.get("POSTGRES_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL ou POSTGRES_URL nao configurada.")
    return psycopg2.connect(database_url)


def _ensure_users_table(cursor):
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


def _normalize_email(email):
    return str(email or "").strip().lower()


def _validate_credentials(payload, creating=False):
    name = str(payload.get("name", "")).strip()
    email = _normalize_email(payload.get("email"))
    password = str(payload.get("password", ""))

    if creating and len(name) < 2:
        raise ValueError("Informe seu nome com pelo menos 2 caracteres.")
    if not EMAIL_RE.match(email):
        raise ValueError("Informe um email valido.")
    if len(password) < 8:
        raise ValueError("A senha precisa ter pelo menos 8 caracteres.")

    return name, email, password


def _register(payload):
    name, email, password = _validate_credentials(payload, creating=True)
    user = {
        "id": str(uuid.uuid4()),
        "name": name,
        "email": email,
        "password_hash": hash_password(password),
    }

    with _connect() as connection:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            _ensure_users_table(cursor)
            try:
                cursor.execute(
                    """
                    INSERT INTO users (id, name, email, password_hash)
                    VALUES (%(id)s, %(name)s, %(email)s, %(password_hash)s)
                    RETURNING id::text, name, email
                    """,
                    user,
                )
            except psycopg2.errors.UniqueViolation as exc:
                raise ValueError("Este email ja esta cadastrado.") from exc
            saved_user = cursor.fetchone()

    return {"user": public_user(saved_user), "token": create_token(saved_user["id"])}


def _login(payload):
    _, email, password = _validate_credentials(payload)

    with _connect() as connection:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            _ensure_users_table(cursor)
            cursor.execute(
                """
                SELECT id::text, name, email, password_hash
                FROM users
                WHERE email = %s
                """,
                (email,),
            )
            user = cursor.fetchone()

    if not user or not verify_password(password, user["password_hash"]):
        raise ValueError("Email ou senha invalidos.")

    return {"user": public_user(user), "token": create_token(user["id"])}


def _me(headers):
    payload = parse_token(bearer_token(headers))
    if not payload:
        raise PermissionError("Sessao invalida ou expirada.")

    with _connect() as connection:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            _ensure_users_table(cursor)
            cursor.execute(
                """
                SELECT id::text, name, email
                FROM users
                WHERE id = %s
                """,
                (payload["sub"],),
            )
            user = cursor.fetchone()

    if not user:
        raise PermissionError("Usuario nao encontrado.")

    return {"user": public_user(user)}


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if urlparse(self.path).path != "/api/auth/me":
                json_response(self, 404, {"error": "Rota nao encontrada."})
                return
            json_response(self, 200, _me(self.headers))
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
            json_response(self, 500, {"error": "Nao foi possivel validar a sessao."})

    def do_POST(self):
        try:
            path = urlparse(self.path).path
            if path == "/api/auth/register":
                json_response(self, 201, _register(read_json(self)))
                return
            if path == "/api/auth/login":
                json_response(self, 200, _login(read_json(self)))
                return
            json_response(self, 404, {"error": "Rota nao encontrada."})
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
            json_response(
                self,
                500,
                {"error": "Nao foi possivel conectar ao banco da Supabase agora."},
            )
