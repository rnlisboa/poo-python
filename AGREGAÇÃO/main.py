from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 8750)
p3 = Produto('Sapato', 150)
carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.lista_produtos()
print(carrinho.soma_total())