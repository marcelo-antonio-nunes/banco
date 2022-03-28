# imports
from modulos import Client, Conta, Utils, Banco, CaixaEletronico


def main():
    utils = Utils()
    caixa_eletronico = CaixaEletronico()
    utils.limpa_tela()
    itau = Banco()
    # ===== DADOS MOCADOS SO PARA TESTE ==========
    # cadastra o cliente
    c1 = Client('Marcelo Antonio', '@tecno')
    c2 = Client('Luiza Adriana', '@trancas')
    c3 = Client('Marcelo Henrique', '@dev')
    # cria a conta do cliente
    ct1 = Conta(c1, 1978, 350, 'ma123', 2000.0, 1000.0)
    ct2 = Conta(c2, 2121, 350, 'lu123', 3000.0, 1000.0)
    ct3 = Conta(c3, 1998, 350, 'celi123', 6000.0, 2000.0)
    # adiciona a conta e retorna uma lista com todas as contas
    itau.adiciona_conta(ct1)
    itau.adiciona_conta(ct2)
    lista = itau.adiciona_conta(ct3)
    # transferencia
    caixa_eletronico.trasferencia(lista)

if __name__ == '__main__':
    main()
