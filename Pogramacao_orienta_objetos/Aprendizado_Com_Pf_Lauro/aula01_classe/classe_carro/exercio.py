# Exercício 8 : Crie uma classe Carro com os atributos marca(string), modelo(string) e ano(int). 
# Implemente um construtor para inicializar esses atributos.
# Exercício 9 : Adicione métodos getMarca()e para retornar os valores dos atributos.getModelo()getAno()
# Exercício 10 : Adicione métodos setMarca(string marca)e para modificar os valores dos atributos.
# setModelo(string modelo)setAno(int ano)
# Exercício 11 : Instancie três objetos da classe Carrocom valores diferentes e exiba seus atributos.
# Exercício 12 : Adicione um método idadeCarro(int anoAtual)que retorna a idade do carro com base no ano atual. 
# Teste o método com uma instância.
# Exercício 13 : Adicione um atributo proprietarios(lista de objetos Pessoa) 
# e um método adicionarProprietario(Pessoa proprietario)para adicionar um proprietário à lista. 
# Crie um método listarProprietarios()que exiba os nomes dos proprietários.
# Exercício 14 : Crie um método transferirProprietario(Pessoa novoProprietario)
# que transfere o carro para um novo proprietário, adicionando-o à lista de proprietários. Teste o método.


class Carro:
    def __init__(self,nome,modelo,ano:int):

        self.nome = nome
        self.modelo = modelo
        self.ano = ano
        self.ano_atual = 2025
        self.proprietarios = []

    def adicionar_proprietarios(self,propritario):
        self.proprietarios.append(propritario)  

    def get_proprrietario(self):
        return self.proprietarios  

    def transferencia(self,Novo_proprietario):
        self.proprietarios.clear()
        self.proprietarios.append(Novo_proprietario)    

    def ideade(self):
        idade =  self.ano_atual - self.ano 
        return idade    

    def getModelo(self):

        return self.modelo
    
    def getAno(self):

        return self.ano  

    
    def setModelo(self, novo_modelo):
        self.modelo = novo_modelo
    
    def setAno(self, novo_ano):
        self.ano = novo_ano  

        
gol = Carro ("gol","volkswagen",2013)

mareia = Carro ("mareia","FIAT",2005)

corrola = Carro ("corrola","Toyota",2014)

# print(vars(gol))
# print(gol.getAno())
# print(gol.getModelo())

# print("alterando nome ")
# gol.setAno(2015)
# gol.setModelo("VW")

# print(gol.getAno())
# print(gol.getModelo())

print(corrola.ideade())

gol.adicionar_proprietarios({"nome": "carlos","Idade":15})

print(gol.get_proprrietario())

print("novo proprietario")
gol.transferencia({"nome": "Amarildo","Idade":45})

print(gol.get_proprrietario())