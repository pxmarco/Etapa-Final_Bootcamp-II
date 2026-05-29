import pytest
from unittest.mock import patch

from api.medications import _create_medication, _list_medications


class DummyCursor:
    def __init__(self, fetch_result=None):
        self.fetch_result = fetch_result or []
        self.executed = []

    def execute(self, query, params=None):
        self.executed.append((query, params))

    def fetchall(self):
        return self.fetch_result

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


class DummyConnection:
    def __init__(self, cursor):
        self._cursor = cursor

    def cursor(self, *args, **kwargs):
        return self._cursor

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


def test_create_medication_saves_address_fields():
    payload = {
        "name": "Dipirona",
        "time": "08:00",
        "dose": "500mg",
        "note": "Tomar após o café",
        "cep": "01001-000",
        "logradouro": "Praça da Sé",
        "cidade": "São Paulo",
        "uf": "SP",
    }
    cursor = DummyCursor()
    connection = DummyConnection(cursor)

    with patch("api.medications._connect", return_value=connection):
        medication = _create_medication(payload, "user-123")

    assert medication["name"] == "Dipirona"
    assert medication["cep"] == "01001-000"
    assert medication["logradouro"] == "Praça da Sé"
    assert medication["cidade"] == "São Paulo"
    assert medication["uf"] == "SP"
    assert "user_id" not in medication
    assert any("INSERT INTO medications" in query for query, _ in cursor.executed)
    assert any("cep" in query and "logradouro" in query and "cidade" in query and "uf" in query for query, _ in cursor.executed)


def test_list_medications_returns_address_fields():
    expected = [
        {
            "id": "1111-2222-3333",
            "name": "Amoxicilina",
            "time": "12:00",
            "dose": "250mg",
            "note": "Tomar com água",
            "cep": "20040-002",
            "logradouro": "Rua da Quitanda",
            "cidade": "Rio de Janeiro",
            "uf": "RJ",
        }
    ]
    cursor = DummyCursor(fetch_result=expected)
    connection = DummyConnection(cursor)

    with patch("api.medications._connect", return_value=connection):
        medications = _list_medications("user-123")

    assert medications == expected
