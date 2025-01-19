import pytest
from classes.prototipo import Prototipo

def test_prototipo_criacao():
     # Teste de criação da classe
    prototipo = Prototipo(
        id=1,
        nome="TR-9",
        ano_fabricacao=2023,
        status="Concluido",
        peso=1500,
        temporada="2024",
        n_teste=5
    )

    assert prototipo.id == 1
    assert prototipo.nome == "TR-9"
    assert prototipo.ano_fabricacao == 2023
    assert prototipo.status == "Concluido"
    assert prototipo.peso == 1500
    assert prototipo.temporada == "2024"
    assert prototipo.n_teste == 5

def test_prototipo_modificar():
    # Teste do método 'modificar'
    prototipo = Prototipo(
        id=1,
        nome="Prototipo-1",
        ano_fabricacao=2024,
        status="Em desenvolvimento",
        peso=1500,
        temporada="2024",
        n_teste=10
    )

    prototipo.modificar(
        nome="Prototipo-1.1",
        ano_fabricacao=2024,
        status="Concluído",
        peso=1350,
        temporada="2025",
        n_teste=15
    )
    
    #Verifica se as mudanças foram feitas com sucesso
    assert prototipo.nome == "Prototipo-1.1"
    assert prototipo.ano_fabricacao == 2024
    assert prototipo.status == "Concluído"
    assert prototipo.peso == 1350
    assert prototipo.temporada == "2025"
    assert prototipo.n_teste == 15
    