class Teste:
    def __init__(self, N_teste, pilotos, id_objetivos, N_voltas, inicio, fim, almoco, data, id_prototipo, id_circuito, n_testes):
        self._N_teste = int(N_teste) if N_teste is not None else None
        self._pilotos = pilotos
        self._id_objetivos = id_objetivos
        self._N_voltas = int(N_voltas)
        self._inicio = inicio
        self._fim = fim
        self._almoco = str(almoco)
        self._data = data
        self._id_prototipo = int(id_prototipo)
        self._id_circuito = int(id_circuito)
        self._n_testes = int(n_testes)

        
        self.documento = f"pre_teste{self._N_teste}.pdf" if self._N_teste is not None else None

    # Getter e Setter para N_teste
    @property
    def N_teste(self):
        return self._N_teste

    @N_teste.setter
    def N_teste(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("N_teste deve ser um número inteiro ou None.")
        self._N_teste = value

    # Getter e Setter para pilotos
    @property
    def pilotos(self):
        return self._pilotos

    @pilotos.setter
    def pilotos(self, value):
        if not isinstance(value, list):
            raise ValueError("Pilotos deve ser uma lista.")
        self._pilotos = value

    # Getter e Setter para N_voltas
    @property
    def N_voltas(self):
        return self._N_voltas

    @N_voltas.setter
    def N_voltas(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("N_voltas deve ser um número inteiro positivo.")
        self._N_voltas = value

    # Getter e Setter para inicio
    @property
    def inicio(self):
        return self._inicio

    @inicio.setter
    def inicio(self, value):
        self._inicio = value

    # Getter e Setter para fim
    @property
    def fim(self):
        return self._fim

    @fim.setter
    def fim(self, value):
        self._fim = value

    # Getter e Setter para almoco
    @property
    def almoco(self):
        return self._almoco

    @almoco.setter
    def almoco(self, value):
        self._almoco = str(value)

    # Getter e Setter para data
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        # Validação para garantir que seja do tipo `date`
        from datetime import date
        if not isinstance(value, date):
            raise ValueError("Data deve ser do tipo `datetime.date`.")
        self._data = value

    # Getter e Setter para id_prototipo
    @property
    def id_prototipo(self):
        return self._id_prototipo

    @id_prototipo.setter
    def id_prototipo(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("id_prototipo deve ser um número inteiro positivo.")
        self._id_prototipo = value

    # Getter e Setter para id_circuito
    @property
    def id_circuito(self):
        return self._id_circuito

    @id_circuito.setter
    def id_circuito(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("id_circuito deve ser um número inteiro positivo.")
        self._id_circuito = value

    # Getter e Setter para n_testes
    @property
    def n_testes(self):
        return self._n_testes

    @n_testes.setter
    def n_testes(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("n_testes deve ser um número inteiro positivo.")
        self._n_testes = value

    # Função para modificar atributos
    def modifica(self, pilotos=None, N_voltas=None, inicio=None, fim=None, almoco=None, n_testes=None):
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
