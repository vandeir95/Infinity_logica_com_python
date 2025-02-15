## Grupo 1: Classe `Veículo`

# 1. **Exercício 1**: Crie uma classe `Veículo` com um método `mover()` que imprime "O veículo está se movendo". 
# Crie uma classe `Carro` que herda de `Veículo` e sobrescreve o método `mover()` para imprimir "O carro está andando na estrada".

# 2. **Exercício 2**: Adicione um atributo `marca` à classe `Veículo` e um método `apresentar()` 
# que imprime "Este veículo é da marca [marca]". Crie uma classe `Moto` que herda de `Veículo` e 
# sobrescreve o método `apresentar()` para incluir "Esta moto é da marca [marca]".

# 3. **Exercício 3**: Crie uma classe `Caminhão` que herda de `Veículo` e sobrescreve o método
# `mover()` para imprimir "O caminhão está transportando carga". Adicione um método `carregar()` que imprime "Caminhão carregado!".

# 4. **Exercício 4**: Crie uma classe `Bicicleta` que herda de `Veículo` e sobrescreve o método `mover()`
# para imprimir "A bicicleta está pedalando". Adicione um método `parar()` que imprime "Bicicleta parada".

# 5. **Exercício 5**: Crie uma lista de objetos do tipo `Veículo` que contenha instâncias
# de `Carro`, `Moto`, `Caminhão` e `Bicicleta`. Use um loop para chamar o método `mover()` de cada objeto, demonstrando polimorfismo.

class Veiculo:
    def __init__(self,marca):
      self.marca = marca
      
    def mover(self):
       print("o Veiculo está se movendo")
    
    def apresentar(self):
       pass

class Carro(Veiculo):
   def __init__(self):
      super().__init__(self.marca) 

   def mover(self):
        return "O carro esta na estrada"  
   
   def apresentar(self):
      return f"O Carro e da marca {self.marca}"

class Moto(Veiculo):
   def __init__(self):
      super().__init__(self.marca) 

   def mover(self):
        return "O carro esta na estrada"  
   
   def apresentar(self):
      return f"Essa moto e da marca {self.marca}"
   

   
# 3. **Exercício 3**: Crie uma classe `Caminhão` que herda de `Veículo` e sobrescreve o método
# `mover()` para imprimir "O caminhão está transportando carga". Adicione um método `carregar()` que imprime "Caminhão carregado!"


class Camiao(Veiculo):
   def __init__(self, marca):
      super().__init__(marca)

   def mover(self):
      return "O caminhão está transportando carga"   
   
   def carregar(self):
      return "que imprime Caminhão carregado!"
   
   def apresentar(self):
      return f"Essa camião  e da marca {self.marca}"
   



class Bicicleta(Veiculo):
   def __init__(self, marca):
      super().__init__(marca)

   def mover(self):
      return "A bicicleta está pedalando"   
   
   def parar(self):
      return "Bicicleta parada"   



# 5. **Exercício 5**: Crie uma lista de objetos do tipo `Veículo` que contenha instâncias
# de `Carro`, `Moto`, `Caminhão` e `Bicicleta`. Use um loop para chamar o método `mover()` de cada objeto, demonstrando polimorfismo.
