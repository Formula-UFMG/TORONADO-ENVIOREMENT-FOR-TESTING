class Pilotos:
    def __init__(self, id_piloto, temporada, n_testes, email, kms):
        self.id_piloto = (id_piloto)
        self.temporada = int(temporada)
        self.n_testes = int(n_testes)
        self.email = str(email)
        self.kms = float(kms)

    def modifica(self, temporada=None, n_testes=None, kms=None) -> None:
        if temporada is not None:
            self.temporada = int(temporada)
        if n_testes is not None:
            self.n_testes = int(n_testes)
        if kms is not None:
            self.kms = float(kms)
