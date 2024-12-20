import sys
import os

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)

from mysql.connector import Error

from database import connection
from error_reporter import send_email
from server.classes import teste

TABLE = "TEFT.teste"

def get_testes(id_prototipo):
    comando = """SELECT * FROM {} WHERE = id_prototipo = \'{}\'""".format(TABLE, id_prototipo)
    verificador, cursor, con = connection.connect_to_db() # coleta as informações para a 
    if verificador == True:
        try:
            # tenta executar o comando 
            cursor.execute(comando) 
            linhas = cursor.fetchall()
            # verifica a informação
            saida = [] 
            for linha in linhas:
                saida.append(teste.Teste(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6],linha[7],linha[8],linha[9]))
            var_login = saida
        except Error as e: # 
            verificador = False
            send_email(e)
        # finaliza a conexão com o banco 
        connection.close_connect_to_bd(cursor,con)
        return verificador, var_login
    else:
        return verificador, None
