# ## **Grupo 4: Classe `Produto`**

# 22. **Exercício 22**: Crie uma classe `Produto` com os atributos `nome` (string), `preco` (double) e `quantidadeEmEstoque` (int).
# Implemente um construtor para inicializar esses atributos.
# 23. **Exercício 23**: Adicione métodos `getNome()`, `getPreco()` e `getQuantidadeEmEstoque()` para retornar os valores dos atributos.
# 24. **Exercício 24**: Adicione métodos `setNome(string nome)`, `setPreco(double preco)` e `setQuantidadeEmEstoque(int quantidade)`
# para modificar os valores dos atributos.
# 25. **Exercício 25**: Instancie três objetos da classe `Produto` com valores diferentes e exiba seus atributos.
# 26. **Exercício 26**: Adicione um método `vender(int quantidade)` que reduz a quantidade em estoque do produto.
# Se a quantidade for maior que o estoque, exiba uma mensagem de erro. Teste o método com uma instância.
# 27. **Exercício 27**: Adicione um atributo `compras` (lista de objetos `Pessoa`) 
# que armazena os clientes que compraram o produto. Crie um método `registrarCompra(Pessoa cliente)` para adicionar um cliente à lista.
# 28. **Exercício 28**: Crie um método `listarClientes()` que exibe os nomes dos clientes que compraram o produto. Teste o método.


class Produto:
    def __init__(self,nome,preco,quantidadeEmEstoque):
    
        self.nome = nome
        self.preco = preco
        self.quantidadeEmEstoque = quantidadeEmEstoque
        self.compras = []
        self.clientes = []
    def __str__(self):
        return f"nome :{self.nome},  preco: {self.preco}, quantidadeEmEstoque {self.quantidadeEmEstoque}" 
    
    def listaClientes(self):
        for i in self.clientes:
            print(i)
        

    def vender(self,Qtd):
        if Qtd > self.quantidadeEmEstoque:
            print("ERRO: o a quantida de produto comprada e maior que o de estoque")
        else:
            
           self.quantidadeEmEstoque -= Qtd
        self.compras.append(f"nome :{self.nome},  preco: {self.preco}, UND {Qtd} valor = {Qtd * self.preco}")

    def getNome(self) :

        return self.nome


    def getPreco(self):

        return self.preco
        
    def getQuantidadeEmEstoque(self):

        return self.quantidadeEmEstoque


    def setNome(self, novo_nome) :

        self.nome = novo_nome


    def setPreco(self,novo_preco):

         self.preco = novo_preco
        
    def setQuantidadeEmEstoque(self,QtdEs):

         self.quantidadeEmEstoque = QtdEs

       


Arroz = Produto("Arroz prato fino 5kg", 25.99, 500)   

Feijao = Produto("Feijão BH 1kg", 6.99, 800)


Macarrao = Produto("Macarrão Santa Amelia", 4.99, 400)

#print(vars(Macarrao))
# print(Feijao.getNome())

Feijao.vender(2)
Feijao.vender(500)
#print(Feijao.getQuantidadeEmEstoque())

print(vars(Feijao))




   
