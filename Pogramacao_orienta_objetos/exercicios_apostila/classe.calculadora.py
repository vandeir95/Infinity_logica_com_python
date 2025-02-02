# Crie uma classe Calculadora que tenha métodos
# para realizar operações matemáticas básicas (+ , - ,
# *
# , / ).

class calculadora:
    def __init__(self,nome,arg_1,arg_2):
         self.nome = nome
         self.arg_1 = arg_1
         self.arg_2 = arg_2
        
    def soma(self):
         resultado = self.arg_1 + self.arg_2
         print("soma e igual :" ,resultado)
    
    def subtracao(self):
         resultado = self.arg_1 - self.arg_2
         print("subtracao e igual :" ,resultado)
    
    def multiplicacao(self):
         resultado = self.arg_1 * self.arg_2
         print("multiplicacao e igual :" ,resultado)
    
    def divisao(self):
         resultado = self.arg_1 / self.arg_2
         print("divisao e igual :" ,resultado)
    
    


minha_calculadora = calculadora("minha_calculadora", 5, 9)

print(minha_calculadora.divisao())