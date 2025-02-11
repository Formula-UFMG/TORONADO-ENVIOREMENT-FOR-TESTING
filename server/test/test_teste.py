import pytest
from datetime import datetime, date
from classes.teste import Teste  

def test_teste_criacao():
    # Definir a data atual
    data_criacao = date.today()
    
    # Teste de criação da classe
    teste = Teste(
        N_teste=1,
        pilotos=["Piloto A", "Piloto B"],
        id_objetivos=[111, 222],
        N_voltas=15,
        inicio="08:00",
        fim="16:00",
        almoco="12:00-13:00",
        data=data_criacao,
        id_prototipo=101,
        id_circuito=201,
        n_testes=5
    )

    assert teste.N_teste == 1
    assert teste.pilotos == ["Piloto A", "Piloto B"]
    assert teste.id_objetivos == [111, 222]
    assert teste.N_voltas == 15
    assert teste.inicio == "08:00"
    assert teste.fim == "16:00"
    assert teste.almoco == "12:00-13:00"
    assert teste.data == data_criacao
    assert teste.id_prototipo == 101
    assert teste.id_circuito == 201
    assert teste.n_testes == 5
    assert teste.documento == "pre_teste1.pdf"

def test_teste_sem_numero():
    # Definir a data atual
    data_criacao = date.today()

    # Teste para verificar comportamento quando N_teste é None
    teste = Teste(
        N_teste=None,
        pilotos=["Piloto C"],
        id_objetivos=[333],
        N_voltas=10,
        inicio="09:00",
        fim="15:00",
        almoco="12:00-12:30",
        data=data_criacao,
        id_prototipo=102,
        id_circuito=202,
        n_testes=10
    )

    assert teste.N_teste is None
    assert teste.documento is None
    assert teste.pilotos == ["Piloto C"]
    assert teste.n_testes == 10

def test_teste_modifica():
    # Definir a data atual
    data_criacao = date.today()

    teste = Teste(
        N_teste=2,
        pilotos=["Piloto X", "Piloto Y"],
        id_objetivos=[444, 555],
        N_voltas=20,
        inicio="07:00",
        fim="14:00",
        almoco="12:00-12:30",
        data=data_criacao,
        id_prototipo=103,
        id_circuito=203,
        n_testes=3
    )

    # Modificar atributos
    teste.modifica(
        pilotos=["Piloto A", "Piloto B"],
        N_voltas=30,
        inicio="08:00",
        fim="15:00",
        almoco="12:30-13:30",
        n_testes=5
    )

    # Verificar alterações
    assert teste.pilotos == ["Piloto A", "Piloto B"]
    assert teste.N_voltas == 30
    assert teste.inicio == "08:00"
    assert teste.fim == "15:00"
    assert teste.almoco == "12:30-13:30"
    assert teste.n_testes == 5
