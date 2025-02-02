# Exercício 1 : Crie uma classe Pessoa com os atributos nome(string) e idade(int). 
# Implemente um construtor para inicializar esses atributos.
# Exercício 2 : Adicione métodos getNome()
# e getIdade()para retornar os valores dos atributos nomee idade.
# Exercício 3 : Adicione métodos setNome(string nome)e setIdade(int idade)para modificar os valores dos atributos.]
# Exercício 4 : Instancie dois objetos da classe Pessoa com valores diferentes e exiba seus atributos.

# Exercício 5 : Adicione um método fazerAniversario()que incrementa a idade da pessoa em 1. Teste o método com uma instância.

# Exercício 6 : Adicione um atributo amigos(lista de objetos Pessoa) e um método adicionarAmigo(Pessoa amigo)para adicionar um amigo à lista. 
# Crie um método listarAmigos()que exiba os nomes dos amigos.

# Exercício 7 : Crie um método removerAmigo(string nome)para remover um amigo da lista pelo nome. Teste o método.


class Pessoa:
    def __init__(self,nome, idade, amigos=None ):
        self.nome = nome 
        self.idade = idade 
        self.amigos = amigos


    def get_lista_amigos(self):
        for i in self.amigos:
            print(i)    
        

    def adicionar_amigos(self,amigo):
        self.amigos = amigo

    def remover_amigo(self,nome):
         for amigo in self.amigos:
            if amigo == nome:
                self.amigos.remove(nome)    

     


    def fazer_aniversario(self):
        self.idade = self.idade + 1 
        


    def getNome(self):
        return self.nome
     
    def getIdade(self):
        return self.idade

    def set_Nome(self,novo_nome):
        self.nome = novo_nome
       
    def set_Idade(self,nova_idade):
        self.idade = nova_idade   

    
        
        


pessoa1 = Pessoa("vandeir de souza cruz", 23)
pessoa2 = Pessoa("Lauro", 30)
pessoa2.set_Nome("lira")
print(pessoa2.getNome())

pessoa1.set_Idade(3)

print(pessoa1.getIdade())

pessoa1.fazer_aniversario()

print("fez aniversario")

print(pessoa1.getIdade())

print("lista amigos ")


pessoa1.adicionar_amigos(["jose","kaka","jaja"])




print(pessoa1.get_lista_amigos())

# pessoa1.remover_amigo("jaja")

# print("amigo removido")
# print(pessoa1.get_lista_amigos())
# pessoa1.set_Nome("Vander S. Cruz",25)
# print(pessoa1)

# print(vars(vandeir))


# print(vandeir.getNome())

# print(vandeir.getIdade())

# vandeir.set_Nome("jose")


