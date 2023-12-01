import sys
classes = sys.path.append('C:\CursoPython\SEÇÃO04\CLASSES ABSTRATAS\classes')
from classes.contaPoupanca import ContaPoupanca
from classes.cCorrente     import ContaCorrente

c = ContaPoupanca(1233, 4565, 0)
c.depositar(60)
c.sacar(27)

print('********************')
cc = ContaCorrente(agencia = 8925, conta = 3333, saldo = 0, limite= 500)
cc.depositar(150)
cc.sacar(270)