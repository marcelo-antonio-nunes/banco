from model.conta import Conta
from model.utils import Utils

utils = Utils()


class CaixaEletronico:
    # transferencia
    def trasferencia(self, lista) -> None:
        numero_origem = int(input("Numero da conta de origem: "))
        for conta in lista:
            if conta.numero == numero_origem:
                numero_destino = int(input('Numero conta destino: '))
                valor = float(input('Valor: '))
                senha = input('Senha por favo: ')
                conta_destino: Conta
                for conta in lista:
                    if conta.numero == numero_destino:
                        conta_destino = conta
                        for conta in lista:
                            if conta._senha == senha:
                                print(
                                    f'Saldo de R${conta.saldo} Cliente {conta.nome}\n')
                                print(conta_destino.saldo_cliente(
                                    conta.saldo_cliente))
                                utils.limpa_tela()
                                conta.transferir(conta_destino, valor, senha)
                                print(
                                    f'Saldo de R${conta.saldo} Cliente {conta.nome}\n')
                                print(conta_destino.saldo_cliente(
                                    conta.saldo_cliente))
                                input()
