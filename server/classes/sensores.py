class Sensores:
    def __init__(self,id_sensor, nome, id_prototipo, informacao):
        self.id_sensor = id_sensor
        self.nome = nome
        self.id_prototipo = id_prototipo
        self.informacao = informacao

    def modificar(self, nome, informacao):
        self.nome = nome
        self.informacao = informacao
