import pytest
from classes.teste import Teste 

def test_teste_criacao():
    # Teste de criação da classe
    teste = Teste(
        N_teste=1,
        pilotos=["Piloto A", "Piloto B"],
        id_objetivos=[111, 222],
        N_voltas=15,
        inicio="08:00",
        fim="16:00",
        almoco="12:00-13:00",
        data="2025-01-09",
        id_prototipo=101,
        id_circuito=201
    )

    assert teste.N_teste == 1
    assert teste.pilotos == ["Piloto A", "Piloto B"]
    assert teste.id_objetivos == [111, 222]
    assert teste.N_voltas == 15
    assert teste.inicio == "08:00"
    assert teste.fim == "16:00"
    assert teste.almoco == "12:00-13:00"
    assert teste.data == "2025-01-09"
    assert teste.id_prototipo == 101
    assert teste.id_circuito == 201
    assert teste.documento == "pre_teste1.pdf"

def test_teste_sem_numero():
    # Teste para verificar comportamento quando N_teste é None
    teste = Teste(
        N_teste=None,
        pilotos=["Piloto C"],
        id_objetivos=[333],
        N_voltas=10,
        inicio="09:00",
        fim="15:00",
        almoco="12:00-12:30",
        data="2025-01-10",
        id_prototipo=302,
        id_circuito=402
    )

    assert teste.N_teste is None
    assert teste.documento is None