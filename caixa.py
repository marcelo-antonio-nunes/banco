# imports
from modulos import Client, Conta, Utils, Banco


def main():
    utils = Utils()
    utils.limpa_tela()
    itau = Banco()
    # cadastra o cliente
    c1 = Client('Marcelo', '@tecno')
    c2 = Client('Luiza', '@trancas')
    c3 = Client('Marcelinho', '@dev')
    # cria a conta do cliente
    ct1 = Conta(c1, 1978, 350, 'ma123', 2000.0, 1000.0)
    ct2 = Conta(c2, 2121, 350, 'lu123', 3000.0, 1000.0)
    ct3 = Conta(c3, 1998, 350, 'celi123', 6000.0, 2000.0)
    # adiciona a conta e retorna uma lista com todas as contas
    itau.adiciona_conta(ct1)
    itau.adiciona_conta(ct2)
    lista = itau.adiciona_conta(ct3)
    # transferencia
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
                            print(conta_destino.saldo_cliente(conta.saldo_cliente))
                            conta.transferir(conta_destino, valor, senha)
                            print(conta_destino.saldo_cliente(conta.saldo_cliente))


if __name__ == '__main__':
    main()
