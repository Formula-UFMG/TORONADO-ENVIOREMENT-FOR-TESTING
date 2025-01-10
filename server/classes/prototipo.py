class Prototipo:
    def __init__(self, id, nome, ano_fabricacao, status, peso, temporada, n_teste):
        self.id = id
        self.nome = nome
        self.ano_fabricacao = ano_fabricacao
        self.status = status
        self.peso = peso
        self.temporada = temporada
        self.n_teste = n_teste

    def modificar(self, nome, ano_fabricacao, status, peso, temporada, n_teste):
        self.nome = nome
        self.ano_fabricacao = ano_fabricacao
        self.status = status
        self.peso = peso
        self.temporada = temporada
        self.n_teste = n_teste
