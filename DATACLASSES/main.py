"""
O módulo dataclasses fornece um decorador e funções 
para criar automaticamente métodos como __init__(), __repr__(), __eq__(etc)
em clases definidas pelo usuário
"""

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def __post__init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    """@property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'"""

p1 = Pessoa('Luiz', 'Gama')
print(p1)
print(p1.nome)
print(p1.sobrenome)
print(p1.nome_completo)