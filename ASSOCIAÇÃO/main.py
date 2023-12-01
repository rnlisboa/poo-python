from classes import Escritor, Caneta, MaquinaEscrever

escritor = Escritor('Juanito')
maquina = MaquinaEscrever()
caneta = Caneta('BIC')
"""print(escritor.nome)
print(caneta.marca)
print(escritor.nome)"""
escritor.ferramenta = caneta
escritor.ferramenta.escrever()