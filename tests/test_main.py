import pytest
from main import MedSync


def test_adicionar_com_sucesso():
    app = MedSync()
    resultado = app.adicionar_medicamento("Aspirina", "08:00", "500mg", "Apos cafe")
    assert "Sucesso" in resultado
    assert len(app.medicamentos) == 1
    assert app.medicamentos[0]["dose"] == "500mg"
    assert app.medicamentos[0]["observacao"] == "Apos cafe"


def test_erro_entrada_vazia():
    app = MedSync()
    with pytest.raises(ValueError):
        app.adicionar_medicamento("", "")


def test_lista_vazia_inicial():
    app = MedSync()
    assert app.listar_medicamentos() == "Nenhum medicamento agendado."


def test_listar_medicamento_com_dose_e_observacao():
    app = MedSync()
    app.adicionar_medicamento("Aspirina", "08:00", "500mg", "Apos cafe")

    resultado = app.listar_medicamentos()

    assert "Aspirina - 08:00" in resultado
    assert "Dose: 500mg" in resultado
    assert "Obs: Apos cafe" in resultado


def test_endereco_entrega_inicial():
    app = MedSync()
    assert app.ver_endereco_entrega() == "Nenhum endereco de entrega cadastrado."
