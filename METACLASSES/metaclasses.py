class Meta(type):
       #__new__(mcs: metaclasses, name: nome da classe, bases: classes pai das classes que estão sendo criadas, namespace)    
    def __new__(mcs, name, bases, namespace):
        #print(name)
        if name == "A":
            return type.__new__(mcs, name, bases, namespace)
        
        #print(namespace)
        if 'b_fala' not in namespace:
            print(f'Você precisa criar o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'B_fala precisa ser um atributo em {name}')
        
        if 'attr_classe' in namespace:
            del namespace['attr_classe']
        
        
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass = Meta):
    attr_classe = 'Valor A'
    def fala(self):
        self.b_fala()

class B(A):
    attr_classe = 'valor B'
    def sei_la(self):
        pass
    def b_fala(self):
        print('oi')
b = B()
print(b.attr_classe)
print(b.attr_classe)