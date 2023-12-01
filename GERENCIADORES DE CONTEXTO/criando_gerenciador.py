
"""class Arquivo:
    def __init__(self, arquivo, modo):
        print('INIT, Abrindo arquivo')
        self.arquivo = open(arquivo, modo)
    
    ## RETORNAR O QUE VAI PARA A VARIAVEL DPS DE 'as'
    def __enter__(self):
        print('Entrou na classe, retornou arquivo')
        return self.arquivo
    
    ## MÉTODO DE SAIDA, as variaveis dps de self são excessões
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Saiu da classe, saiu do arquivo')
        self.arquivo.close()
        print(exc_tb)
        print(exc_type)
        print(exc_val)


with Arquivo('jeje.txt', 'w') as arquivo:
    arquivo.write('something')"""

## OUTRA MANEIRA
from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        print('abrindo arquivo')
        yield arquivo
    finally:
        print('fechando arquivo')
        arquivo.close()

with abrir('abc.txt', 'w') as arquivo:
    for i in range(100000):
        arquivo.write(f'linha {i} \n')

