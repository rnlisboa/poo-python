"""# type é uma metaclasse pra criar classe
class Pai:
    nome = 'yerefr'
A = type(
    'A',
    (Pai,),
    {'attr': 'Hello, world'}
)

a = A()
print(a.attr, a.nome)"""
num = int(input('Informe um numero: '))
num2 = list(range(1, num + 1))
n = 0
for i in num2:
    i = i + i 
    n+=i
print(n)