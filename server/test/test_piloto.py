import pytest
from datetime import date
from classes.piloto import Pilotos

def test_criacao_piloto():
    #Definir a data atual
    data_criacao = date.today()

    #Teste da criação da classe
    piloto = Pilotos(
        id_piloto=1,
        temporada=2025,
        n_testes=5,
        email="piloto@email.com",
        kms=40
    )

    #Conferir as mudanças
    assert piloto.id_piloto == 1
    assert piloto.temporada == 2025
    assert piloto.n_testes == 5
    assert piloto.email == "piloto@email.com"
    assert piloto.kms == 40

def test_modifica_piloto():
    #Definir a data atual
    data_criacao = date.today()

    #Criar a classe inicial
    piloto = Pilotos(
        id_piloto=2,
        temporada=2024,
        n_testes=10,
        email="piloto@email.com",
        kms=50
    )

    #Modificação de aspectos
    piloto.modifica(
        temporada=2025,
        n_testes=15,
        kms=60
    )

    #Verifica se as modificações foram feitas com uscesso
    assert piloto.temporada == 2025
    assert piloto.n_testes == 15
    assert piloto.kms == 60
    