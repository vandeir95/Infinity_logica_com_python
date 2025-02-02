#classe


class Quadrado:
    #atributo
    def __init__(self,lado):
        self.lado = lado
        


    def perimetro(self):
        
        perimetro = self.lado * 4
        print(f"O perimetro do quadrado e :", perimetro)

    def area(self):
        area = self.lado * self.lado
        print(f"A area do quadra e igual :", area) 
#instanciando  a classe
meu_primeiro_quadrado = Quadrado(6)

print(vars(meu_primeiro_quadrado))

meu_primeiro_quadrado.perimetro()

meu_primeiro_quadrado.area()

