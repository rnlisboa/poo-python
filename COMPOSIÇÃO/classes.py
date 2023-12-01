# UMA CLASSE VAI SER DONA DE OBJETOS DE OUTRA CLASSE

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
    def insere_indereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))
    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado