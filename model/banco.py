from modulos import Conta


class Banco:
    lista = []

    def __init__(self, ) -> None:
        pass

    def adiciona_conta(self, conta: Conta) -> set:
        Banco.lista.append(conta)
        return Banco.lista
