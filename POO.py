class Triangulo:
    def __init__(self,lado1,lado2,lado3,base,altura):
        self.lado1= lado1 #criando os objetos - atributos
        self.lado2 = lado2
        self.lado3 = lado3 
        self.base = base
        self.altura = altura
        
    def area(self):
        return(self.base + self.altura)/2
    
    def lado(self):
        if self.lado1 > self.lado2 + self.lado3:
            return 'não é um triângulo'
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3:
            return 'triangulo isosceles'
        else:
            return 'outro tipo de triangulo'

t1 = Triangulo(2,1,3,4,3) #passando via parâmetro os valores pros objetos
t2 = Triangulo(3,4,1,2,6) #passando via parâmetro os valores pros objetos
print(t2.lado1,t2.lado2,t2.lado3,t2.base,t2.altura)

print(t2.area())
print(t2.lado())