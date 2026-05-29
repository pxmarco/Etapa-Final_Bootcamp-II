import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from auth_utils import create_token, hash_password, parse_token, verify_password  # noqa: E402


def test_hash_password_nao_salva_senha_pura():
    senha = "senha-segura-123"
    senha_hash = hash_password(senha)

    assert senha not in senha_hash
    assert verify_password(senha, senha_hash)
    assert not verify_password("senha-errada", senha_hash)


def test_token_assinado_com_usuario(monkeypatch):
    monkeypatch.setenv("MEDSYNC_SECRET", "segredo-de-teste")

    token = create_token("user-123")
    payload = parse_token(token)

    assert payload["sub"] == "user-123"


def test_token_recusa_assinatura_alterada(monkeypatch):
    monkeypatch.setenv("MEDSYNC_SECRET", "segredo-de-teste")

    token = create_token("user-123")
    adulterado = token.replace(token[-1], "x" if token[-1] != "x" else "y")

    assert parse_token(adulterado) is None
