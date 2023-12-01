from contas import Conta

class ContaCorrente(Conta):
    tipo = 'Corrente'
    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite
    
    @property
    def limite(self):
        return self._limite
    
    def sacar(self, valor):
        if valor > (self._limite + self._saldo):
            print('Valor indisponível para saque.')
            return
        print(f'Saque realzizado no valor de {valor}')
        self._saldo -=  valor
        self.detalhes()

"""c2 = ContaCorrente(1111, 5456, 0)

c2.sacar(500)"""

            