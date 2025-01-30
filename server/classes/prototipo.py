class Prototipo:
    def __init__(self, id, nome, ano_fabricacao, status, peso, temporada, n_teste):
        self.id = id
        self.nome = str(nome)
        self.ano_fabricacao = int(ano_fabricacao)
        self.status = str(status)
        self.peso = float(peso)
        self.temporada = int(temporada)
        self.n_teste = int(n_teste)

    def modificar(self, nome, ano_fabricacao, status, peso, temporada, n_teste):
        self.nome = nome
        self.ano_fabricacao = int(ano_fabricacao)
        self.status = str(status)
        self.peso = float(peso)
        self.temporada = int(temporada)
        self.n_teste = int(n_teste)
