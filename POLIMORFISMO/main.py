"""
Polimorfismo é o principio que permite que classes derivadas de uma mesma 
superclasse tenham métodos iguais (mesma quantidade e tipos de parâmetros) mas comportamentos diferentes. 

como feitos em CLASSES ABSTRATAS
"""
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self, msg): pass

class B(A):
    def fala(self, msg):
        print(f'B está falando {msg}')

class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')

b = B()
c = C()
b.fala('sobre o mundial do palmeiras')
c.fala('que 51 é pinga')