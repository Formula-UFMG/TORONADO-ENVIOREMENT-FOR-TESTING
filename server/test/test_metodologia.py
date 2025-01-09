import pytest
from classes.metodologia import Metodologia 

def test_metodologia_criacao():
    # Teste de criação da classe
    metodo = Metodologia(
        id_metodologia=1,
        objetivo="Teste de aceleração",
        N_pessoas=8,
        subgrupo="Motor",
        procedimento="Acelerar o carro nas retas",
        N_voltas=5
    )

    assert metodo.id_metodologia == 1
    assert metodo.objetivo == "Teste de aceleração"
    assert metodo.N_pessoas == 8
    assert metodo.subgrupo == "Motor"
    assert metodo.procedimento == "Acelerar o carro nas retas"
    assert metodo.N_voltas == 5

def test_metodologia_modificar():
    # Teste do método 'modificar'
    metodo = Metodologia(
        id_metodologia=1,
        objetivo="Teste de curva",
        N_pessoas=10,
        subgrupo="Aerodinâmica",
        procedimento="Testar o carro nas curvas",
        N_voltas=3
    )

    metodo.modificar(
        objetivo="Teste de temperatura",
        N_pessoas=12,
        subgrupo="Chassi",
        procedimento="Testar a temepratura do carro por longo periodos",
        N_voltas=15
    )

    assert metodo.objetivo == "Teste de temperatura"
    assert metodo.N_pessoas == 12
    assert metodo.subgrupo == "Chassi"
    assert metodo.procedimento == "Testar a temepratura do carro por longo periodos"
    assert metodo.N_voltas == 15
