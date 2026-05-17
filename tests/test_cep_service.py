import json

import pytest
from cep_service import CepServiceError, consultar_cep, formatar_endereco


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False

    def read(self):
        return json.dumps(self.payload).encode("utf-8")


def test_consultar_cep_com_resposta_mockada():
    def fake_opener(url, timeout):
        assert url == "https://viacep.com.br/ws/01001000/json/"
        assert timeout == 10
        return FakeResponse(
            {
                "cep": "01001-000",
                "logradouro": "Praca da Se",
                "bairro": "Se",
                "localidade": "Sao Paulo",
                "uf": "SP",
            }
        )

    endereco = consultar_cep("01001-000", opener=fake_opener)

    assert endereco == {
        "cep": "01001-000",
        "logradouro": "Praca da Se",
        "bairro": "Se",
        "cidade": "Sao Paulo",
        "uf": "SP",
    }
    assert formatar_endereco(endereco) == "Praca da Se - Se - Sao Paulo - SP"


def test_consultar_cep_invalido():
    with pytest.raises(ValueError):
        consultar_cep("123")


def test_consultar_cep_nao_encontrado():
    def fake_opener(url, timeout):
        return FakeResponse({"erro": True})

    with pytest.raises(CepServiceError):
        consultar_cep("00000000", opener=fake_opener)
