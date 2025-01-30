class Sensores:
    def __init__(self,id_sensor, nome, id_prototipo, informacao):
        self.id_sensor = id_sensor
        self.nome = str(nome)
        self.id_prototipo = id_prototipo
        self.informacao = str(informacao)

    def modificar(self, nome, informacao):
        self.nome = str(nome)
        self.informacao = str(informacao)
