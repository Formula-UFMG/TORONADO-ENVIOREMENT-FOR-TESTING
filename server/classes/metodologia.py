class Metodologia:
    def __init__(self, id_metodologia, objetivo, N_pessoas, subgrupo, procedimento, N_voltas, temporada):
        self.id_metodologia = id_metodologia
        self.objetivo = str(objetivo)
        self.N_pessoas = int(N_pessoas)
        self.subgrupo = str(subgrupo)
        self.procedimento = str(procedimento)
        self.N_voltas = int(N_voltas)
        self.temporada = int(temporada)
    
    def modificar(self, objetivo, N_pessoas, subgrupo, procedimento, N_voltas):
        self.objetivo = str(objetivo)
        self.N_pessoas = int(N_pessoas)
        self.subgrupo = str(subgrupo)
        self.procedimento = str(procedimento)
        self.N_voltas = int(N_voltas)
