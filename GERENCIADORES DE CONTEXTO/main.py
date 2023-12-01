arquivo = open('abc.txt', 'w')
arquivo.write('jeje')
arquivo.close()
### isso abaixo é um gerenciador de contexto
with open('jeje.txt', 'w') as arquivo:
    arquivo.write('something')