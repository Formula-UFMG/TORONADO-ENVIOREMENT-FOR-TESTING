class Teste:
    def __init__(self, N_teste, pilotos, id_objetivos, N_voltas, inicio, fim, almoco, data, id_prototipo, id_circuito, n_testes):
        self.N_teste = N_teste
        self.pilotos = pilotos
        self.id_objetivos = id_objetivos
        self.N_voltas = N_voltas
        self.inicio = inicio
        self.fim = fim
        self.almoco = almoco
        self.data = data
        self.id_prototipo = id_prototipo
        self.id_circuito = id_circuito
        self.n_testes = n_testes
        if self.N_teste != None:
            self.documento = "pre_teste" + str(self.N_teste) + ".pdf"
        else:
            self.documento = None
