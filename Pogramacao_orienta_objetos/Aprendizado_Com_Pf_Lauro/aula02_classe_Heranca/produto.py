## Grupo 4: Classe `Produto`

# 1. **Exercício 16**: Crie uma classe `Produto` com um método `calcularPreco()` que retorna 0. Crie uma classe `Livro` 
# que herda de `Produto` e sobrescreve o método `calcularPreco()` para retornar o preço de um livro com 10% de desconto.

# 2. **Exercício 17**: Crie uma classe `Eletrônico` que herda de `Produto` e sobrescreve o método `calcularPreco()` 
# para retornar o preço de um eletrônico com 5% de imposto.

# 3. **Exercício 18**: Adicione um atributo `nome` à classe `Produto` e um método `descrever()` 
# que imprime "Este produto é um [nome]". Sobrescreva esse método nas classes `Livro` e `Eletrônico` para incluir detalhes específicos.

# 4. **Exercício 19**: Crie uma classe `Roupa` que herda de `Produto` e sobrescreve o método `calcularPreco()` 
# para retornar o preço de uma roupa com 20% de desconto.

# 5. **Exercício 20**: Crie uma lista de objetos do tipo `Produto` que contenha instâncias de
# `Livro`, `Eletrônico` e `Roupa`. Use um loop para chamar os métodos `calcularPreco()` e `descrever()` de cada objeto, demonstrando polimorfismo.

# ---

class Produto():
    def __init__(self,nome):
        self.nome = nome

    def descrever(self):
        return f"Este produto é um {self.nome}" 

    def calcular_preco(self):
        return 0
    

class Livro(Produto):
    def __init__(self,nome,preco,editora):
        super().__init__(nome)  
        self.preco = preco
        self.editora = editora

    def calcular_preco(self):
        self.preco = self.preco * 0.9

        return self.preco
    
    def descrever(self):
        return f"Este produto é o livro {self.nome} da editora {self.editora}" 

    
class Eletronico(Produto):
    def __init__(self,nome,preco,marca):
        super().__init__(nome) 
        self.marca = marca  

        self.preco = preco


    def calcular_preco(self):
        self.preco = self.preco * 1.05 

        return self.preco  


    def descrever(self):
        return f"Este produto é um {self.nome} da marca {self.marca}"  
    

   # 4. **Exercício 19**: Crie uma classe `Roupa` que herda de `Produto` e sobrescreve o método `calcularPreco()` 
# para retornar o preço de uma roupa com 20% de desconto.
 
class Roupa(Produto):
    def __init__(self, nome,preco,marca,numeracao):
        super().__init__(nome)

        self.marca = marca
        self.numeracao = numeracao
        self.preco = preco


    def calcular_preco(self):
        self.preco = self.preco * 0.8

        return self.preco  


    def descrever(self):
        return f"Este produto é um {self.nome} da marca {self.marca} com numeração {self.numeracao}"    


meu_livro = Livro("paraiso",103.99, "viva")

tv_k4 = Eletronico("tv Ultra k4",1100,"SAMSUNG")

camiseta_12 = Roupa("blusa",59.99,"NIKE","M")


minha_compra = [meu_livro,tv_k4,camiseta_12]

for i in minha_compra:
   
    print(i.descrever())
    print("preço : ", i.calcular_preco())
    print("------------------")