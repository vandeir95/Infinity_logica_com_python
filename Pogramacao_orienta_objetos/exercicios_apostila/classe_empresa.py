# ATIVIDADE PRÁTICA 3

# Crie uma classe Empresa que permita gerenciar
# funcionários. Os funcionários devem ter informações
# como nome, cargo e salário. A empresa deve ser capaz

# de adicionar, remover e listar funcionários.
class funcionario:
    def __init__(self,nome,idade, salario,cargo):

        self.nome = nome
        self.idade = idade
        
        self.salario = salario
        self.cargo = cargo

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"  



jose = funcionario("jose",54,8000.00,"gerente geral")

maria = funcionario("maria",34,5000.00,"gerente")
carla = funcionario("carla",25,1500.00,"atendente")

class empresa:
    def __init__(self,nome):
        self.nome = nome
        self.funcionarios = []
        

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def lista_funcionarios(self):
         print("lista de funcionarios")
         for funcionario in self.funcionarios:
            print(funcionario)
        
    def demitir_funcionario(self,nome):
        for funcionario in self.funcionarios:
            if funcionario == nome:
                self.funcionarios.remove(nome)




casas_bb = empresa("casas_bb" )

print(casas_bb.nome)

casas_bb.adicionar_funcionario(jose)

casas_bb.adicionar_funcionario(maria)

print(casas_bb.lista_funcionarios())

casas_bb.demitir_funcionario(jose)

print(casas_bb.lista_funcionarios())

casas_bb.adicionar_funcionario(carla)

print(casas_bb.lista_funcionarios())