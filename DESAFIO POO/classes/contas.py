from abc import abstractmethod

class Conta:
    def __init__(self, conta, agencia, saldo):
        self._conta = conta
        self._agencia = agencia
        self._saldo = saldo

    @abstractmethod
    def sacar(self, valor): pass

    @property
    def agencia(self):
        return self._agencia
    @property
    def saldo(self):
        return self._saldo
    @property
    def conta(self):
        return self._conta
    
    def depositar(self, valor):
        if isinstance(valor, (int, float)):
            print(f'Deposito realizado no valor de {valor}')
            self._saldo += valor
        else:
            print('Informe apenas números!') 
    
    def detalhes(self):
        print(f'Agência: {self._agencia} Conta: {self._conta} Saldo: R$ {self._saldo}')
    

