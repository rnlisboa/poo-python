class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        
        self.preco = self.preco - (self.preco * (percentual / 100))

    ## Getter
    @property
    def nome(self):
        return self._nome
    ## Setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.lower()
   
   
   
    ## Getter
    @property
    def preco(self):
        return self._preco
    ## Setter
    @preco.setter
    def preco(self, valor):
        # chegando se o valor é uma instancia de string
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor
produto_01 = Produto('CAMISETA', 150)
produto_01.desconto(10)

produto_02 = Produto('CANECA', 'R$15')
produto_02.desconto(10)

print(produto_01.preco, produto_01.nome)
print(produto_02.preco, produto_02.nome)