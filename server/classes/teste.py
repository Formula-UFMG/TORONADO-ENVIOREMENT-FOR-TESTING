import sys
import os
from datetime import timedelta

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)

from path_manager import get_briefing_path, get_debriefing_path

class Teste:
    def __init__(self, N_teste, nome, pilotos, id_objetivos, N_voltas, inicio, fim, almoco, data, id_prototipo, id_circuito, status, observacao):
        self.N_teste = N_teste
        self.nome = nome
        self.pilotos = pilotos
        self.id_objetivos = id_objetivos
        self.N_voltas = N_voltas
        self.inicio = inicio
        self.fim = fim
        self.almoco = almoco
        self.data = data
        self.id_prototipo = id_prototipo
        self.id_circuito = id_circuito
        self.status = status
        self.observacao = observacao
        if self.N_teste is not None:
            self.briefing = get_briefing_path() + "briefing" + str(self.N_teste) + ".pdf"
            self.debriefing = get_debriefing_path() + "debriefing" + str(self.N_teste) + ".pdf"
        else:
            self.briefing = None
            self.debriefing = None

    def serialize_timedelta(self, value):
        if isinstance(value, timedelta):
            # Retorna o número de segundos do timedelta
            return value.total_seconds()
        return value

    def to_dict(self):
        # Retorna os atributos da instância como um dicionário
        return {
            'N_teste': self.N_teste,
            'pilotos': self.pilotos,
            'id_prototipo': self.id_prototipo,
        }
