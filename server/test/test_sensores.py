import pytest
from classes.sensores import Sensores

def test_sensores_criacao():
    # Teste de criação da Classe
    sensor = Sensores(
        id_sensor = 1,
        nome = "sensor-velocidade",
        id_prototipo = 2,
        informacao= "Sensor de velocidade do carro"
    )

    assert sensor.id_sensor == 1
    assert sensor.nome == "sensor-velocidade"
    assert sensor.id_prototipo == 2
    assert sensor.informacao == "Sensor de velocidade do carro"

def test_sensor_modificar():
    # Teste de modificação da Classe
    sensor = Sensores(
        id_sensor = 2,
        nome = "sensor-aceleracao",
        id_prototipo = 3,
        informacao = "Sensor de aceleracao do carro"
    )

    sensor.modificar(
        nome = "sensor-aceleracao-v2",
        informacao = "Novo sensor de aceleracao do carro"
    )

    assert sensor.id_sensor == 2
    assert sensor.nome == "sensor-aceleracao-v2"
    assert sensor.id_prototipo == 3
    assert sensor.informacao == "Novo sensor de aceleracao do carro"