class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def falar(self):
        print(f'{self.nome} está falando dentro da classe Pessoa')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} está comprando')
    def falar(self):
        print(f'{self.nome} está falando dentro da classe Cliente')

class ClienteVIP(Cliente):
    ### SOBRE(SCREVENDO, PONDO) O MÉTODO FALAR DE Pessoa
    ### PEGANDO O CONSTRUTOR DO CLIENTE VIP E ADIONANDO ALGO MAIS
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome
    
    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')
    """def falar(self):
        #super().falar() ## <-- se usar assim, vai ser o usado o metodo da primeira classe que ele encontrar acima
        Pessoa.falar(self) ## <-- se refere a superClasse
        Cliente.falar(self)
        print(f'{self.nome} está falando dentro da classe ClienteVIP')"""

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} está estudando')