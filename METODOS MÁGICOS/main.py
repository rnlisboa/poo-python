"""
https://rszalski.github.io/magicmethods/
"""
"""class A:
    ## Construtor
    def __new__(cls, *args, **kwargs):
        

        def fala_oi( *args, **kwargs):
            print('Oi')
        cls.fala_oi = fala_oi

        return object.__new__(cls)
    def __init__(self):
        print('Ich bin den INIT')

a = A()
a.fala_oi()"""

class A:

    def __init__(self):
        print('Ich bin den INIT')
    ## FAZ A CLASSE SE COMPORTAR COMO UMA FUNÇÃO
    def __call__(self, *args, **kwargs):
        """print(args)
        print(kwargs)"""
        resultado = 1
        for i in args:
            resultado+= i
        return resultado
    def __setattr__(self, key, value):
        self.__dict__[key] = value
a = A()
variavel = a(1,2,3,4,5,6,8,9,)
print(variavel)
a.nome = 'JOJO'