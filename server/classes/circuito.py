import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)

import path_manager 

class Circuito:
    def __init__(self, id_circuito, nome, tempo_descolcamento, KM, curvas, cones, n_setores ,local,data_criacao):
        self.id_circuito = id_circuito
        self.nome = nome
        self.tempo_descolcamento = tempo_descolcamento
        self.KM = KM
        self.curvas = curvas
        self.cones = cones
        self.n_setores = n_setores
        self.local = local
        self.data_criacao = data_criacao
        if id_circuito != None:
            caminho = "circuito" + str(id_circuito) + ".png"
            self.caminho = path_manager.join_path(path_manager.get_circuitos_path(),caminho)
            self.caminho_exi = "../static/upload/circuitos/" + caminho

    def modificar(self, nome, tempo_descolcamento, KM, curvas, cones, n_setores , local):
        self.nome = nome
        self.tempo_descolcamento = float(tempo_descolcamento)
        self.KM = float(KM)
        self.curvas = int(curvas)
        self.n_setores = int(n_setores)
        self.cones = int(cones)
        self.local = local
