import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)

import path_manager 

class Circuito:
    def __init__(self, id_circuito, nome, tempo_descolcamento, KM, curvas, cones, local,data_criacao):
        self.id_circuito = id_circuito
        self.nome = str(nome)
        self.tempo_descolcamento = float(tempo_descolcamento)
        self.KM = float(KM)
        self.curvas = int(curvas)
        self.cones = int(cones)
        self.local = str(local)
        self.data_criacao = data_criacao
        if id_circuito != None:
            caminho = "circuito" + str(id_circuito) + ".png"
            self.caminho = path_manager.join_path(path_manager.get_upload_path(),caminho)
    def modificar(self, nome, tempo_descolcamento, KM, curvas, cones, local):
        self.nome = str(nome)
        self.tempo_descolcamento = float(tempo_descolcamento)
        self.KM = float(KM)
        self.curvas = int(curvas)
        self.cones = int(cones)
        self.local = str(local)
