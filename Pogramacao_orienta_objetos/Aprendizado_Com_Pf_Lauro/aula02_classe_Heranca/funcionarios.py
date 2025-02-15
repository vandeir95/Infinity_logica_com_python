
# ## Grupo 3: Classe `Funcionário`

# 1. **Exercício 11**: Crie uma classe `Funcionário` com um método `calcularSalario()` que retorna 0. 

# Crie uma classe `FuncionárioCLT` que herda de `Funcionário` e sobrescreve o método `calcularSalario()` para retornar um salário fixo.

# 2. **Exercício 12**: Crie uma classe `FuncionárioPJ` que herda de]
# `Funcionário` e sobrescreve o método `calcularSalario()` para retornar o valor de um contrato mensal.

# 3. **Exercício 13**: Adicione um atributo `nome` à classe `Funcionário` e um método `apresentar()` 
# que imprime "Eu sou [nome]". Sobrescreva esse método nas classes `FuncionárioCLT` e `FuncionárioPJ` para incluir o tipo de contrato.

# 4. **Exercício 14**: Crie uma classe `Estagiário` que herda de `Funcionário` e sobrescreve o método `calcularSalario()` 
# para retornar uma bolsa-auxílio.

# 5. **Exercício 15**: Crie uma lista de objetos do tipo `Funcionário` que contenha instâncias de `FuncionárioCLT`, `
# FuncionárioPJ` e `Estagiário`. Use um loop para chamar os métodos `calcularSalario()` e `apresentar()` de cada objeto,
# demonstrando polimorfismo.

class Funcionario():
    def __init__(self,nome):
        self.nome = nome

    def apresentar(self):
        return self.nome    


    def calcularSalario(self):
        pass   


class FuncionarioCLT(Funcionario):
    def __init__(self,nome,salario:float):
        super().__init__(nome)
        self.salario = salario 

    def apresentar(self):
        return f"Eu sou {self.nome},  funcionario CLT "
    
    def calcularSalario(self):
        return self.salario

class FuncionarioPJ(Funcionario):
    def __init__(self,nome,contratoMensal):
        super().__init__(nome)      
        self.contratoMensal =  contratoMensal  

    def apresentar(self):
        return f"Eu sou {self.nome}, funcionario contrato PJ"
    

    def calcularSalario(self):
        return self.contratoMensal

class Estagiario(Funcionario):
    def __init__(self,nome):
        super().__init__(nome) 
        

    def apresentar(self):
        return f"Eu sou {self.nome}, estagiario(a)"    


    def calcularSalario(self):
        return "bolsa-auxilio"    


paulo_jose = FuncionarioPJ("jose",100)
carlos_155 = FuncionarioCLT("Carlos miguel ", 5555)
ana_5757 = Estagiario("ana  maria")



lista_funcionarios = [paulo_jose,carlos_155,ana_5757]


for apresentar in lista_funcionarios:
    print(apresentar.apresentar())

for salario in lista_funcionarios:
        print(salario.calcularSalario())