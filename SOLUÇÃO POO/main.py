from banco import Banco
from cliente import Cliente
from contas import ContaCorrente, ContaPoupanca

banco = Banco()

cliente_01 = Cliente('Rastafaro', 30)
cliente_02 = Cliente('Gulerson', 27)
cliente_03 = Cliente('Marserine', 70)
cliente_04 = Cliente('Camponeto', 21)

conta_01 = ContaPoupanca(1111,256587,0)
conta_02 = ContaPoupanca(2222,354245,0)
conta_03 = ContaPoupanca(1234,123644,0)
conta_04 = ContaPoupanca(4321,201458,0)

cliente_01.inserir_conta(conta_01)
cliente_02.inserir_conta(conta_02)
cliente_03.inserir_conta(conta_03)
cliente_04.inserir_conta(conta_04)

banco.inserir_cliente(cliente_01)
banco.inserir_conta(conta_01)


if banco.autenticar(cliente_01):
    cliente_01.conta.depositar(124)
    cliente_01.conta.sacar(20)
else:
    print("cliente não autenticado")