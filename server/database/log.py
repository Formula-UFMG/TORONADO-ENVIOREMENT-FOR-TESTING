import sys
import os

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)

from mysql.connector import Error
from database import connection
from error_reporter import send_email
from server.classes import log

TABLE = "TEFT.log"

def get_logs():
    comando = f"SELECT * FROM {TABLE}"  # comando SQL
    verificador, cursor, con = connection.connect_to_db()  # Conexão com o banco
    if verificador:
        try:
            cursor.execute(comando)  # Executa o comando
            linhas = cursor.fetchall()
            saida = []
            for linha in linhas:
                # Cria objetos Log com os valores retornados
                saida.append(log.Log(
                    linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6],
                    linha[7], linha[8], linha[9], linha[10], linha[11], linha[12],
                    linha[13], linha[14], linha[15], linha[16], linha[17], linha[18],
                    linha[19], linha[20], linha[21], linha[22], linha[23], linha[24], linha[25]
                ))
            var_login = saida
        except Error as e:
            verificador = False
            send_email(e)
        connection.close_connect_to_bd(cursor, con)  # Fecha a conexão
        return verificador, var_login
    else:
        return verificador, None

