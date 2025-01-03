import sys
import os

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)

from mysql.connector import Error

from database import connection
from error_reporter import send_email
from server.classes import sensores
TABLE = "TEFT.sensores"

def creat_sensores(sensor):
    comando = """INSERT INTO {} (nome, id_prototipo, informacao) VALUE (\'{}\', \'{}\',\'{}\')""".format(TABLE,sensor.nome, sensor.id_prototipo, sensor.informacao)
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
