# ## Grupo 2: Classe `FormaGeométrica`

# 1. **Exercício 6**: Crie uma classe `FormaGeométrica` com um método `calcularArea()` que retorna 0. 
# Crie uma classe `Quadrado` que herda de `FormaGeométrica` e sobrescreve o método `calcularArea()` 
# para calcular a área de um quadrado (lado * lado).

# 2. **Exercício 7**: Crie uma classe `Círculo` que herda de `FormaGeométrica` e sobrescreve o método
# `calcularArea()` para calcular a área de um círculo (π * raio²). Use π = 3.14.

# 3. **Exercício 8**: Adicione um método `calcularPerimetro()` à classe `FormaGeométrica` 
# que retorna 0. Sobrescreva esse método nas classes `Quadrado` e `Círculo` para calcular o perímetro de cada forma.

# 4. **Exercício 9**: Crie uma classe `Triângulo` que herda de `FormaGeométrica` e implementa os métodos 
# `calcularArea()` e `calcularPerimetro()` para um triângulo equilátero.

# 5. **Exercício 10**: Crie uma lista de objetos do tipo `FormaGeométrica` que contenha instâncias de 
# `Quadrado`, `Círculo` e `Triângulo`. Use um loop para chamar os métodos `calcularArea()` e `calcularPerimetro()` 
# de cada objeto, demonstrando polimorfismo.

# ---
import math
class FormaGeometrica:
    def __init__(self):
        pass

    def calcularArea(self):
        return 0
    
    def calcularPerimetro():
        pass
    

class quadrado(FormaGeometrica):
    def __init__(self,lado):
        super().__init__()   
        self.lado = lado 

    def calcularArea(self):
        Area = self.lado * self.lado 
        return "Area do quadra e igual :", Area
    def calcularPerimetro(self):
        perimetro = 4 * self.lado
        return f"o perimetr do Quadrado e igula :",perimetro

class Circulo(FormaGeometrica):
    def __init__(self,raio):
        super().__init__()
        self.raio = raio
    
    def calcularArea(self):
        Area = 3.14 * (self.raio**2)
        return "Area quadrado ",Area
    # perimetro = 2* raio * PI
    def calcularPerimetro(self):
        perimetro =  2* self.raio  * 3.14

        return "o perimetro do circulo e igual :", perimetro

# 4. **Exercício 9**: Crie uma classe `Triângulo` que herda de `FormaGeométrica` e implementa os métodos 
# `calcularArea()` e `calcularPerimetro()` para um triângulo equilátero.

class triangulo(FormaGeometrica):
    def __init__(self,lado):
        super().__init__()
        self.lado = lado
    def calcularArea(self):
        area = ((self.lado ** 2 )* math.isqrt(3)) / 4
        return "area do triangulo : ", area

    def calcularPerimetro(self):
        perimetro = self.lado * 3
        return "perimetro e igual", perimetro


meu_quadrado = quadrado(5)

meu_circulo = Circulo(5)    

meu_triangulo = triangulo(5)


lista_figuras_geometricas = [meu_circulo,meu_quadrado,meu_triangulo]


for i in lista_figuras_geometricas:
    print(i.calcularArea())

for i in lista_figuras_geometricas:
    print(i.calcularPerimetro())
