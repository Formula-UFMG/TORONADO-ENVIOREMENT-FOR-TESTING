class Pilotos:
    def __init__(self, id_piloto, temporada, n_testes, email, kms):
        self.id_piloto = id_piloto
        self.temporada = temporada
        self.n_testes = n_testes
        self.email = email
        self.kms = kms

    def modifica(self, temporada=None, n_testes=None, kms=None) -> None:
        if temporada is not None:
            self.temporada = temporada
        if n_testes is not None:
            self.n_testes = n_testes
        if kms is not None:
            self.kms = kms
