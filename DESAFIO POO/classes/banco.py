from pessoa import Pessoa
from clientes import Cliente
from cCorrente import ContaCorrente
from cPoupanca import ContaPoupanca

class Banco:
    def __init__(self):
        self._clientes = {}
    
    # CLIENTES
    def novo_cliente(self, cliente):
        self._clientes[cliente.nome] = {
            'nome': cliente.nome,
            'detalhes': {
                'Agencia': conta.agencia,
                'Conta'  : conta.conta,
                'Saldo'  : conta.saldo,
                'tipo'   : conta.tipo
            }
        }
    
    def lista_cliente(self):
        if len(self._clientes) == 0:
            print('Seu banco não tem clientes.')
            return
        for cliente in self._clientes:
            print(' Nome:',self._clientes[cliente]['nome'], '\n Detalhes:', self._clientes[cliente]['detalhes'])

conta = ContaPoupanca(4588, 1012, 1500)
cliente1 = Cliente('João Alberto', 25, conta)
banco = Banco()
banco.novo_cliente(cliente1)
banco.lista_cliente()

conta = ContaCorrente(3424, 2454, 750.20)
cliente2 = Cliente('Guilherme Andrade', 37, conta)
banco = Banco()
banco.novo_cliente(cliente2)
banco.lista_cliente()


    
    
    
    
