from contas import Conta

class ContaPoupanca(Conta):
    tipo = 'Poupança'
    def sacar(self, valor):
        if not valor > self._saldo:
            print('Saldo insuficiente para saque.')
            return

        print(f'Saque realizado no valor de R$ {valor}')
        self._saldo -= valor
        
       

