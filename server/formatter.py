import hashlib
from datetime import datetime, date, time
import path_manager

from database import metodologia as bd_metodologia
from database import piloto as bd_piloto
from database import membros as bd_membros
from database import metodologia as bd_metodologia
from server.classes import objetivos

def encode_password(password: str) -> str:
    result = hashlib.md5()
    result.update(password.encode('utf-8'))
    return result.hexdigest()

def get_temporada() -> str:
    data = date.today()
    if data.month >= 1 and data.month <= 8:
        return str(data.year - 1) + "/" + str(data.year)
    elif data.month > 8:
        return str(data.year) + "/" + str(data.year + 1)

def concatenar_vetor(vetor: list) -> str:
    saida = ""
    contador = 1
    for elemento in vetor:
        if contador == 1:
            saida = str(elemento)
        else:
            saida += ";" + str(elemento)
        contador += 1
    return saida

def string_int(vetor: list) -> list:
    saida = []
    for elemento in vetor:
        saida.append(int(elemento))
    return saida

def string_float(vetor: list) -> list:
    saida = []
    for elemento in vetor:
        saida.append(float(elemento))
    return saida

def deserializacao(entrada: str,tipo: str) -> list:
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
        saida = objetivos.Objetivos(metodologia.id_metodologia, metodologia.objetivo, metodologia.status, metodologia.temporada) 
    else:
        saida = None
    return saida

def get_objetivos(lista_testes):
    for teste in lista_testes:
        teste.id_objetivos = deserializacao(teste.id_objetivos, "int")
        objetivos = []
        for objetivo in teste.id_objetivos:
            objetivos.append(cria_objetivo(objetivo))
        teste.id_objetivos = objetivos
    return lista_testes

def coleta_informacao(entrada):
    saida = entrada.split("|")
    return saida[0]

def string_to_datetime(time_str):
    time_obj = datetime.strptime(time_str, "%H:%M").time()
    return time_obj

def formatação_graficos(entrada):# criar uma lista de objetos para ser plotado nos grafico
    pass

def formatacao_piloto(entrada: list):
    lista_pilotos = []
    for piloto in entrada:
        verificador_piloto,entidade_piloto = bd_piloto.get_piloto(piloto)
        if verificador_piloto == True:
            verificador_membro, entidade_membro = bd_membros.get_membro(entidade_piloto.email)
            if verificador_membro == True:
                entidade_piloto.add_nome(entidade_membro.nome)
                dic = {
                    "id": entidade_piloto.id_piloto,
                    "nome": entidade_piloto.nome
                }
                lista_pilotos.append(dic)
            else:
                return "Erro ao realizar a busca"
        else:
            return "Erro ao realizar a busca"
    return lista_pilotos

def formatar_select_log(log):
    entidade = {
        "id": log.id_logs,
        "nome": "log: " + str(log.id_logs)
    }
    return entidade

def formatar_descricao(log):
    entidade = {
        "descricao": log.descricao
    }
    return entidade

def formata_coodenadas(entrada):# coleta o ponto inicial de converte em 2 saidas(x e y)
    pass

def formata_classe_dicionario(lista_classes):
    return [classe.to_dict() for classe in lista_classes]

def verifica_formatacao_temporada(temporada):
    anos = temporada.split("/")
    if len(anos) != 2:
        return False
    else:
        if len(anos[0]) == 4 and len(anos[1]) == 4:
            return True
        else:
            return False

def formata_informacoes_piloto(piloto, membro):
    piloto.add_nome(membro.nome)
    return piloto

def formata_lista_pilotos(lista):
    for piloto in lista:
        verificador, entidade_membro = bd_membros.get_membro(piloto.email)
        if verificador == True:
            piloto = formata_informacoes_piloto(piloto, entidade_membro)
        else: 
            return False
    return lista

def id_piloto_nome(lista):
    nova_lista = deserializacao(lista, 'int')
    saida = []
    for piloto in nova_lista:
        verificador, entidade = bd_piloto.get_piloto(piloto)
        if verificador == True:
            verificador_membro, entidade_membro = bd_membros.get_membro(entidade.email)
            if verificador_membro == True:
                saida.append(entidade_membro.nome)
            else:
                return False
        else:
            return False
    return saida

def id_objetivo_objetivo(lista):
    nova_lista = deserializacao(lista, "int")
    saida = []
    for id in nova_lista:
        verificador, entidade_metodologia = bd_metodologia.get_metodologia(id)
        if verificador == True:
            saida.append(entidade_metodologia.objetivo)
        else:
            return False
    return saida

def formatar_lista_testes(lista):
    for teste in lista:
        teste.pilotos = id_piloto_nome(teste.pilotos)
    return lista
