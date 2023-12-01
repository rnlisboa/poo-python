from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta 
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()
    
    def detalhes(self):
        print(f'Agência: {self.agencia} Conta: {self.conta} Saldo: {self. saldo}')

    @abstractmethod
    def sacar(self, valor): pass

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if isinstance(valor, (int, float)):
            if valor > self.saldo:
                print('Saldo insuficiente para saque.')
                return
            self.saldo -= valor
            self.detalhes()

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if isinstance(valor, (int, float)):
            if valor > (self.saldo + self.limite):
                print('Saldo insuficiente para saque.')
                return
            self.saldo -= valor
            self.detalhes()
