import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from auth_utils import user_initials  # noqa: E402


def test_user_initials_com_nome_completo():
    assert user_initials("Heber Macedo") == "HM"


def test_user_initials_com_um_nome():
    assert user_initials("Ana") == "A"


def test_user_initials_sem_nome():
    assert user_initials("") == "--"
