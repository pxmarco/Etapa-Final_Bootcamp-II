import json
from urllib.error import URLError
from urllib.request import urlopen


class CepServiceError(Exception):
    """Erro ao consultar a API de CEP."""


def limpar_cep(cep):
    return "".join(char for char in cep if char.isdigit())


def consultar_cep(cep, opener=urlopen):
    cep_limpo = limpar_cep(cep)
    if len(cep_limpo) != 8:
        raise ValueError("Informe um CEP com 8 digitos.")

    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"

    try:
        with opener(url, timeout=10) as response:
            dados = json.loads(response.read().decode("utf-8"))
    except (URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
        raise CepServiceError("Nao foi possivel consultar o CEP agora.") from exc

    if dados.get("erro"):
        raise CepServiceError("CEP nao encontrado na base do ViaCEP.")

    return {
        "cep": dados.get("cep", ""),
        "logradouro": dados.get("logradouro", ""),
        "bairro": dados.get("bairro", ""),
        "cidade": dados.get("localidade", ""),
        "uf": dados.get("uf", ""),
    }


def formatar_endereco(endereco):
    partes = [
        endereco.get("logradouro"),
        endereco.get("bairro"),
        endereco.get("cidade"),
        endereco.get("uf"),
    ]
    partes_validas = [parte for parte in partes if parte]
    return " - ".join(partes_validas)
