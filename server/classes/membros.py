class Membros:
    def __init__(self, email, senha, nome, subgrupo) ->None:
        self.email = email
        self.senha = senha
        self.nome = str(nome)
        self.subgrupo = str(subgrupo)

    def modifica(self, nome, subgrupo, senha) -> None:
        self.nome = str(nome)
        self.subgrupo = str(subgrupo)
        if senha != None:
            self.senha = senha

    def to_dict(self):
        #Converte para um dicinário
        return {
            "email": self.email,
            "nome": self.nome,
            "subgrupo": self.subgrupo,
        }