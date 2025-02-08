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

class FormaGeometrica:
    def __init__(self):
        pass

    def calcular_area(self):
        return 0
    
    def calcularPerimetro():
        pass
    

class quadrado(FormaGeometrica):
    def __init__(self,lado):
        super().__init__()   
        self.lado = lado 

    def calcular_area(self):
        return self.lado * self.lado 

    def calcularPerimetro(self):
        perimetro = 4 * self.lado
        print(f"o perimetr do Quadrado e igula :",perimetro)
    

    # 2. **Exercício 7**: Crie uma classe `Círculo` que herda de `FormaGeométrica` e sobrescreve o método
# `calcularArea()` para calcular a área de um círculo (π * raio²). Use π = 3.14.


class Circulo(FormaGeometrica):
    def __init__(self,raio):
        super().__init__()
        self.raio = raio
    
    def calcular_area(self):
        Area = 3.14 * (self.raio**2)
        print(Area) 
    # perimetro = 2* raio * PI
    def calcularPerimetro(self):
        perimetro =  2* self.raio  * 3.14

        print("o perimetro do circulo e igual :", perimetro)
    
meu_circulo = Circulo(5)    

meu_circulo.calcular_area()


# 3. **Exercício 8**: Adicione um método `calcularPerimetro()` à classe `FormaGeométrica` 
# que retorna 0. Sobrescreva esse método nas classes `Quadrado` e `Círculo` para calcular o perímetro de cada forma.
