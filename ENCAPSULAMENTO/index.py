"""
public, protected, private
_ protected - convencionado para não ser modificado, mas se quiser pode
__ private - pra ser acessado e modificado usa-se ( instancia._nomeDaClasse__atributo)
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_cliente(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()

bd.inserir_cliente(1, 'joão')
bd.inserir_cliente(2, 'ban')
bd.inserir_cliente(3, 'daide')
bd._dados = 'kkakak'
bd.apaga_cliente(2)
bd.lista_cliente()
