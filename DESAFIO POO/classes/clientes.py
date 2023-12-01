from pessoa import Pessoa
from cCorrente import ContaCorrente
from cPoupanca import ContaPoupanca

class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self._conta = conta
    
    def conta(self):
        return self._conta
    def det(self):
        return self._conta.detalhes()

"""conta = ContaPoupanca(1222, 5458, 0)
#conta.detalhes()
print(conta.agencia)
c1 = Cliente('joão', 27, conta)
print(c1.conta())
c1.conta().depositar(50)
#conta.detalhes()
#print(c1.nome, c1.idade)"""