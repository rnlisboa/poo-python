class A:
    def falar(self):
        print('Está falando em A')

class B(A):
    def falar (self):
        print('Falando em B')

class C(A):
    def falar (self):
        print('Falando em C')

#### HERANÇA MÚLTIPLA

class D(B, C):
    pass
d = D()
d.falar()