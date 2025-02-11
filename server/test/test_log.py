import pytest
from classes.log import Log

def test_log():

#Cria o log de acordo com os parametros definidos
    log = Log(
        vazao_de_bancada_a=10,
        wps=5,
        temperatura_oleo=20,
        pressao_embreagem=100,
        id_teste=101,
        tps=10,
        time=45,
        velo_rte=50,
        amortecedor_te=40,
        forca_g_long=8,
        amortecedor_de=11,
        tensao_bateria=110,
        velo_rtd=50,
        pressao_oleo=80,
        temperatura_ar=30,
        temperatura_motor=60,
        pressao_diferencial_combustivel=90,
        sonda_geral=3,
        pressao_freio=20,
        rpm=2000,
        marcha=4,
        velo_rfe=115,
        id_logs=202,
        link="www.link.com",
        descricao="descrição do log teste",
        forca_g_lateral=9,
        id_piloto=303
    )

    #Verificar se as mudanças fora mfeitas com sucesso
    assert log.vazao_de_bancada_a == 10
    assert log.wps == 5
    assert log.temperatura_oleo == 20
    assert log.pressao_embreagem == 100
    assert log.id_teste == 101
    assert log.tps == 10
    assert log.time == 45
    assert log.velo_rte == 50
    assert log.amortecedor_te == 40
    assert log.forca_g_long == 8
    assert log.amortecedor_de == 11
    assert log.tensao_bateria == 110
    assert log.velo_rtd == 50
    assert log.pressao_oleo == 80
    assert log.temperatura_ar == 30
    assert log.temperatura_motor == 60
    assert log.pressao_diferencial_combustivel == 90
    assert log.sonda_geral == 3
    assert log.pressao_freio == 20
    assert log.rpm == 2000
    assert log.marcha == 4
    assert log.velo_rfe == 115
    assert log.id_logs == 202
    assert log.link == "www.link.com"
    assert log.descricao == "descrição do log teste"
    assert log.forca_g_lateral == 9
    assert log.id_piloto == 303


def test_modifica():
    
    # Criação do objeto inicial
    log = Log(
        vazao_de_bancada_a=10,
        wps=5,
        temperatura_oleo=20,
        pressao_embreagem=100,
        id_teste=101,
        tps=10,
        time=45,
        velo_rte=50,
        amortecedor_te=40,
        forca_g_long=8,
        amortecedor_de=11,
        tensao_bateria=110,
        velo_rtd=50,
        pressao_oleo=80,
        temperatura_ar=30,
        temperatura_motor=60,
        pressao_diferencial_combustivel=90,
        sonda_geral=3,
        pressao_freio=20,
        rpm=2000,
        marcha=4,
        velo_rfe=115,
        id_logs=202,
        link="www.link.com",
        descricao="descrição do log teste",
        forca_g_lateral=9,
        id_piloto=303
    )

    # Modificando os valores do log
    log.modifica(
        vazao_de_bancada_a=15,
        wps=6,
        temperatura_oleo=25,
        pressao_embreagem=105,
        id_teste=102,
        tps=12,
        time=50,
        velo_rte=55,
        amortecedor_te=45,
        forca_g_long=9,
        amortecedor_de=13,
        tensao_bateria=115,
        velo_rtd=55,
        pressao_oleo=85,
        temperatura_ar=35,
        temperatura_motor=65,
        pressao_diferencial_combustivel=95,
        sonda_geral=4,
        pressao_freio=25,
        rpm=2500,
        marcha=5,
        velo_rfe=120,
        id_logs=203,
        link="www.novelink.com",
        descricao="descrição do log modificado",
        forca_g_lateral=10,
        id_piloto=304
    )

    # Verifica se os valores foram atualizados corretamente
    assert log.vazao_de_bancada_a == 15
    assert log.wps == 6
    assert log.temperatura_oleo == 25
    assert log.pressao_embreagem == 105
    assert log.id_teste == 102
    assert log.tps == 12
    assert log.time == 50
    assert log.velo_rte == 55
    assert log.amortecedor_te == 45
    assert log.forca_g_long == 9
    assert log.amortecedor_de == 13
    assert log.tensao_bateria == 115
    assert log.velo_rtd == 55
    assert log.pressao_oleo == 85
    assert log.temperatura_ar == 35
    assert log.temperatura_motor == 65
    assert log.pressao_diferencial_combustivel == 95
    assert log.sonda_geral == 4
    assert log.pressao_freio == 25
    assert log.rpm == 2500
    assert log.marcha == 5
    assert log.velo_rfe == 120
    assert log.id_logs == 203
    assert log.link == "www.novelink.com"
    assert log.descricao == "descrição do log modificado"
    assert log.forca_g_lateral == 10
    assert log.id_piloto == 304

