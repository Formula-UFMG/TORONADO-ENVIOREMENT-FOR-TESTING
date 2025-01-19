import os
import pytest
from datetime import date
from classes.circuito import Circuito

def test_criacao_circuito():
    # Definir a data de criação como a data atual
    data_criacao = date.today()

    circuito = Circuito(id_circuito=1, 
                        nome="Autódromo", 
                        tempo_descolcamento=10, 
                        KM=100,
                        curvas=12, 
                        cones=5, 
                        local="Contagem",
                        data_criacao=data_criacao
                        )
    
    # Confere se as definições foram salvas corretamente
    assert circuito.id_circuito == 1
    assert circuito.nome == "Autódromo"
    assert circuito.tempo_descolcamento == 10
    assert circuito.KM == 100
    assert circuito.curvas == 12
    assert circuito.cones == 5
    assert circuito.local == "Contagem"
    
    # Verifica se o nome do arquivo é o esperado (apenas o nome, sem o caminho completo)
    assert os.path.basename(circuito.caminho) == "circuito1.png"
    
    # Verifica se a data de criação foi corretamente atribuída
    assert circuito.data_criacao == data_criacao

def test_modifica_circuito():
    # Definir a data de criação como a data atual
    data_criacao = date.today()

    circuito = Circuito(id_circuito=1, nome="Autódromo", tempo_descolcamento=10, KM=100,
                         curvas=12, cones=5, local="Contagem", data_criacao=data_criacao)
    
    # Faz a modificação do circuito
    circuito.modificar(nome="Autódromo2", tempo_descolcamento=15, KM=80,
                         curvas=15, cones=8, local="Betim")
    
    # Testa se modificações foram feitas com sucesso
    assert circuito.nome == "Autódromo2"
    assert circuito.tempo_descolcamento == 15
    assert circuito.KM == 80
    assert circuito.curvas == 15
    assert circuito.cones == 8
    assert circuito.local == "Betim"
    assert circuito.data_criacao == data_criacao

def test_ID_Nulo_circuito():
    # Definir a data de criação como a data atual
    data_criacao = date.today()

    circuito = Circuito(id_circuito=None, nome="Autódromo", tempo_descolcamento=10, KM=100,
                         curvas=12, cones=5, local="Contagem", data_criacao=data_criacao)
    
    # Confere se as definições foram salvas corretamente
    assert circuito.id_circuito == None
    assert circuito.nome == "Autódromo"
    assert circuito.tempo_descolcamento == 10
    assert circuito.KM == 100
    assert circuito.curvas == 12
    assert circuito.cones == 5
    assert circuito.local == "Contagem"
