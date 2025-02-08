## Grupo 1: Classe `Veículo`

# 1. **Exercício 1**: Crie uma classe `Veículo` com um método `mover()` que imprime "O veículo está se movendo". 
# Crie uma classe `Carro` que herda de `Veículo` e sobrescreve o método `mover()` para imprimir "O carro está andando na estrada".

# 2. **Exercício 2**: Adicione um atributo `marca` à classe `Veículo` e um método `apresentar()` que imprime "Este veículo é da marca [marca]".
# Crie uma classe `Moto` que herda de `Veículo` e sobrescreve o método `apresentar()` para incluir "Esta moto é da marca [marca]".

# 3. **Exercício 3**: Crie uma classe `Caminhão` que herda de `Veículo` e sobrescreve o método 
# `mover()` para imprimir "O caminhão está transportando carga". Adicione um método `carregar()` que imprime "Caminhão carregado!".

# 4. **Exercício 4**: Crie uma classe `Bicicleta` que herda de `Veículo` e sobrescreve o método 
# `mover()` para imprimir "A bicicleta está pedalando". Adicione um método `parar()` que imprime "Bicicleta parada".

# 5. **Exercício 5**: Crie uma lista de objetos do tipo 
# `Veículo` que contenha instâncias de `Carro`, `Moto`, `Caminhão` e `Bicicleta`. Use um loop para chamar o método 
# `mover()` de cada objeto, demonstrando polimorfismo.


class Veiculo:
    def __init__(self,marca):
        self.marca = marca

    def mover(self):
        print("O Veiculo esta andando")    

    def apresentar(self):

        print(f"Este veículo é da marca {self.marca}")


titan_150 = Veiculo("HONDA")



class Camiao(Veiculo):
    def __init__(self, marca):
        super().__init__(marca)

    def mover(self):
        print("O caminhão está transportando carga")  

    def carregar(self):
        print("Caminhão carregado!")    

wv_710 = Camiao("Volkswagen")


class Bicicleta(Veiculo):
    def __init__(self, marca):
        super().__init__(marca)

    def mover(self):
        print("A bicicleta está pedalando") 


    def parar(self):
        print("Bicicleta parada")    


minha_bicicleta = Bicicleta("kikos")    


titan_150.apresentar()


lista_veiculos = [titan_150,wv_710,minha_bicicleta]



for i in lista_veiculos:
    i.mover()