from classes.circuito import Circuito

def test_criacao_circuito():
    circuito = Circuito(id_circuito=1, nome="Autódromo", tempo_descolcamento=10, KM=100,
                         curvas=12, cones=5, local="Contagem")
    
    #Confere se o as definições foram salvas corretamente
    assert circuito.id_circuito == 1
    assert circuito.nome == "Autódromo"
    assert circuito.tempo_descolcamento == 10
    assert circuito.KM == 100
    assert circuito.curvas == 12
    assert circuito.cones == 5
    assert circuito.local == "Contagem"
    assert circuito.caminho == "circuito1.PNG" #Como o ID não é nulo cria o caminho

def test_modifica_circuito():
    circuito = Circuito(id_circuito=1, nome="Autódromo", tempo_descolcamento=10, KM=100,
                         curvas=12, cones=5, local="Contagem")
    
    #Faz a modificação do circuito
    circuito.modificar(nome="Autódromo2", tempo_descolcamento=15, KM=80,
                         curvas=15, cones=8, local="Betim")
    
    #Testa se modificações foram feitas com sucesso
    assert circuito.nome == "Autódromo2"
    assert circuito.tempo_descolcamento == 15
    assert circuito.KM == 80
    assert circuito.curvas == 15
    assert circuito.cones == 8
    assert circuito.local == "Betim"

def test_ID_Nulo_circuito():
    circuito = Circuito(id_circuito=None, nome="Autódromo", tempo_descolcamento=10, KM=100,
                         curvas=12, cones=5, local="Contagem")
    
    #Confere se o as definições foram salvas corretamente
    assert circuito.id_circuito == None
    assert circuito.nome == "Autódromo"
    assert circuito.tempo_descolcamento == 10
    assert circuito.KM == 100
    assert circuito.curvas == 12
    assert circuito.cones == 5
    assert circuito.local == "Contagem"