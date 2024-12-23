import sys
import os

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)

from mysql.connector import Error

from database import connection
from error_reporter import send_email
from server.classes import circuito

TABLE = "TEFT.circuito"

def creat_circuito(circuito):
    comando = """INSERT INTO {} (nome, tempo_descolcamento, KM, curvas, cones, local) VALUE(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')""".format(TABLE, circuito.nome, circuito.tempo_descolcamento, circuito.KM, circuito.curvas, circuito.cones, circuito.local)
    verificador, cursor, con = connection.connect_to_db()
    if verificador == True:
        try:
            cursor.execute(comando)
            con.commit()
            var_login = True
        except Error as e:
            var_login = False
            send_email(e)
        connection.close_connect_to_bd(cursor, con)
        return verificador, var_login
    else:
        return verificador, None

def get_circuitos():
    comando = "SELECT * FROM {}".format(TABLE)
    verificador, cursor, con = connection.connect_to_db()
    if verificador == True:
        try:
            cursor.execute(comando)
            linhas = cursor.fetchall()
            saida = []
            for linha in linhas:
                saida.append(circuito.Circuito(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6],None))
            var_login = saida
        except Error as e:
            verificador = False
            send_email(e)
        connection.close_connect_to_bd(cursor, con)
        return verificador, var_login
    else:
        return verificador, None

def get_circuito(id_circuito):
    comando = "SELECT * FROM {} WHERE ID_circuito = \'{}\'".format(TABLE, id_circuito)
    verificador, cursor, con = connection.connect_to_db()
    if verificador == True:
        try:
            cursor.execute(comando)
            linhas = cursor.fetchall()
            saida = []
            for linha in linhas:
                saida.append(circuito.Circuito(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6],None))
            var_login = saida
        except Error as e:
            verificador = False
            send_email(e)
        connection.close_connect_to_bd(cursor, con)
        return verificador, var_login
    else:
        return verificador, None 

def modificar(circuito):
    comando = """UPDATE {} SET nome = \'{}\' tempo_descolcamento = \'{}\' KM = \'{}\' curvas = \'{}\' cones = \'{}\' local WHERE ID_circuito = \'{}\'""".format(TABLE, circuito.nome, circuito.tempo_descolcamento, circuito.KM, circuito.curvas, circuito.cones, circuito.local, circuito.id_circuito)
    verificador, cursor, con = connection.connect_to_db()
    if verificador == True:
        try:
            cursor.execute(comando)
            con.commit()
            var_login = True
        except Error as e:
            var_login = False
            send_email(e)
        connection.close_connect_to_bd(cursor, con)
        return verificador, var_login
    else:
        return verificador, None

def apagar(circuito):
    comando = """DELETE FROM {} WHERE ID_circuito = \'{}\'""".format(circuito.id_circuito)
    verificador, cursor, con = connection.connect_to_db()
    if verificador == True:
        try:
            cursor.execute(comando)
            con.commit()
            var_login = True
        except Error as e:
            var_login = False
            send_email(e)
            connection.close_connect_to_bd(cursor, con)
        return verificador, var_login
    else:
        return verificador, None

def get_id(prototipo):
    comando = "SELECT * FROM {} WHERE nome, ano_fabricacao, status, peso, temporada = \'{}\'".format(TABLE, prototipo.nome, prototipo.ano_fabricacao, prototipo.status, prototipo.peso, prototipo.temporada)
    verificador, cursor, con = connection.connect_to_db()
    if verificador == True:
        try:
            cursor.execute(comando)
            linhas = cursor.fetchall()
            saida = []
            for linha in linhas:
                saida.append(prototipo.Prototipo(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5]))
            var_login = saida
        except Error as e :
            verificador = False
            send_email(e)
        connection.close_connect_to_bd(cursor, con)
        return verificador, var_login
    else:
        return verificador, None
