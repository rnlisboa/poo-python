" Typing --> https://docs.python.org/3/library/typing.html "

def funcao(a: int, b: float, c: str):
    return a,b,c

print(funcao('df',5, 1.8))

def funcao2(a: int, b: float, c: str) -> float:
    return 10.01

print(funcao2('df',[], 1.8))
 
def funcao3() -> list | dict:
    return 'a,b,c'

print(funcao3())

