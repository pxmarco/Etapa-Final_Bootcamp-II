import pytest
from main import MedSync

def test_adicionar_com_sucesso():
    app = MedSync()
    resultado = app.adicionar_medicamento("Aspirina", "08:00")
    assert "Sucesso" in resultado
    assert len(app.medicamentos) == 1

def test_erro_entrada_vazia():
    app = MedSync()
    with pytest.raises(ValueError):
        app.adicionar_medicamento("", "")

def test_lista_vazia_inicial():
    app = MedSync()
    assert app.listar_medicamentos() == "Nenhum medicamento agendado."