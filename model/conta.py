# modelo de conta
from modulos import Client


class Conta:
    def __init__(self, Client: Client, numero: int, agencia: int, senha: str, saldo: float, limite: float) -> None:
        self._client = Client
        self._numero = numero
        self._agencia = agencia
        self._senha = senha
        self._saldo = saldo
        self._limite = limite

    def __str__(self) -> str:
        return f'''Cliente: {self._client._nome} Conta: {self._numero}\nAgencia: {self._agencia}\n'''

    @property
    def saldo(self, ) -> float:
        return self._saldo

    @property
    def limite(self, ) -> float:
        return self._limite

    @property
    def numero(self, ) -> int:
        return self._numero

    @property
    def nome(self, ) -> str:
        return self._client._nome

    @property
    def cliente(self, ) -> Client:
        return self._client

    def tem_saldo(self, valor: float) -> bool:
        return True if self._saldo+self._limite >= valor else False

    def depositar(self, valor: float) -> None:
        self._saldo += valor

    def sacar(self, valor: float, senha: str) -> None:
        if senha == self._senha:
            if self.tem_saldo(valor):
                self._saldo -= valor
            else:
                print("Saldo insuficiente\n")
        else:
            print("Senha invalida!\n")

    def saldo_cliente(self, cliente: Client) -> str:
        return f'O saldo Cliente {self.cliente.nome} é de R${self.saldo}\n'

    def transferir(self, destino: object, valor: float, senha) -> None:
        if self._senha == senha:
            if self.tem_saldo(valor):
                self._saldo -= valor
                destino._saldo += valor
                print(f'transferido da conta {self._numero}\nCliente {self._client._nome}')
                print(f'pra conta {destino._numero}\nCliente {destino._client._nome}')
                print(f'O valor de R${valor} com sucesso!\n')
            else:
                print("Saldo insuficiente")
        else:
            print("Senha invalida!\n")
            input()
            exit()