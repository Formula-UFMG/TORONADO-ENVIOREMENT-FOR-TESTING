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

    def modifica(self, pilotos=None, N_voltas=None, inicio=None, fim=None, almoco=None, n_testes=None) -> None:
        if pilotos is not None:
            self.pilotos = pilotos
        if N_voltas is not None:
            self.N_voltas = N_voltas
        if inicio is not None:
            self.inicio = inicio
        if fim is not None:
            self.fim = fim
        if almoco is not None:
            self.almoco = almoco
        if n_testes is not None:
            self.n_testes = n_testes