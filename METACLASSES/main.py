"""
Metaclasses são classes que criam classes

ERRO DESSE PROGRAMA CORRIGIDO NO ARQUIVO metaclasses.py
"""
class A:
    
    def fala(self):
        self.b_fala()

class B(A):
    """
    ESTA CLASSE ESTÁ HERDANDO O MÉTODO fala() DA CLASSE A
    O METODO HERDADO CHAMA O MÉTODO b_fala()
    """
    """def b_fala(self):
        print('oi')
    """
    pass
b = B()
b.fala()