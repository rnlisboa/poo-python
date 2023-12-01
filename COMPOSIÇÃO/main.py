from classes import Endereco, Cliente

cliente_01 = Cliente('Mateus', 32)

cliente_01.insere_indereco('Recife', 'PE')
print(cliente_01.nome)
cliente_01.lista_enderecos()
print()

cliente_02 = Cliente('Fernando', 56)
cliente_02.insere_indereco('Salvador', 'BH')
print(cliente_02.nome)
cliente_02.lista_enderecos()
print()

cliente_03 = Cliente('João', 32)
cliente_03.insere_indereco('Juiz de fora', 'MG')
print(cliente_03.nome)
cliente_03.lista_enderecos()
print()

