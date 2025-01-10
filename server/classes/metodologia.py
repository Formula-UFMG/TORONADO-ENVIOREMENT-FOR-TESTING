class Metodologia:
    def __init__(self, id_metodologia, objetivo, N_pessoas, subgrupo, procedimento, N_voltas, temporada):
        self.id_metodologia = id_metodologia
        self.objetivo = objetivo
        self.N_pessoas = N_pessoas
        self.subgrupo = subgrupo
        self.procedimento = procedimento
        self.N_voltas = N_voltas
        self.temporada = temporada
    
    def modificar(self, objetivo, N_pessoas, subgrupo, procedimento, N_voltas):
        self.objetivo = objetivo
        self.N_pessoas = N_pessoas
        self.subgrupo = subgrupo
        self.procedimento = procedimento
        self.N_voltas = N_voltas
