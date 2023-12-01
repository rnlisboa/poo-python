from random import randint
class Pessoa:
    ano_atual = 2019
    # METODOS DE INSTÂNCIA
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
    # MÉTODO DE CLASSE
    @classmethod
    def por_ano_de_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    # MÉTODO ESTÁTICO
    @staticmethod
    def gera_id():
        rand = randint(1000, 19999)
        return rand

#pessoa_01 = Pessoa.por_ano_de_nascimento('João', 1987)
pessoa_01 = Pessoa('mangusto', 17)
print(pessoa_01.gera_id())