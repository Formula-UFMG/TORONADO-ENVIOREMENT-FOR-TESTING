import hashlib
from datetime import date
import path_manager

from database import metodologia as bd_metodologia
from server.classes import objetivos

def encode_password(password):
    result = hashlib.md5()
    result.update(password.encode('utf-8'))
    return result.hexdigest()

def get_temporada():
    data = date.today()
    if data.month >= 1 and data.month <= 8:
        return str(data.year - 1) + "/" + str(data.year)
    elif data.month > 8:
        return str(data.year) + "/" + str(data.year + 1)

def concatenar_vetor(vetor):
    saida = ""
    contador = 1
    for elemento in vetor:
        if contador == 1:
            saida = str(elemento)
        else:
            saida += ";" + str(elemento)
        contador += 1
    return saida

def string_int(vetor):
    saida = []
    for elemento in vetor:
        saida.append(int(elemento))
    return saida

def string_float(vetor):
    saida = []
    for elemento in vetor:
        saida.append(float(elemento))
    return saida

def deserializacao(entrada,tipo):
    entrada = str(entrada)
    saida = entrada.split(";")
    match tipo:
        case "int":
            return string_int(saida)
        case _:
            return string_float(saida)

def verificador_arquivos(testes):
    saida = []
    for teste in testes:
        confirma = path_manager.file_exists(teste.documento)
        if confirma == True:
            saida.append(teste)
    return saida

def cria_objetivo(id):
    verificador, metodologia = bd_metodologia.get_metodologia(id)
    if verificador == True:
        saida = objetivos.Objetivos(metodologia.id_metodologia,metodologia.objetivo,metodologia.status) 
    else:
        saida = None
    return saida


def get_objetivos(lista_testes):
    for teste in lista_testes:
        teste.id_objetivos = deserializacao(teste.id_objetivos, "int")
        objetivos = []
        for objetivo in teste.id_objetivos:
            objetivos.append(cria_objetivo(objetivo))
    return lista_testes