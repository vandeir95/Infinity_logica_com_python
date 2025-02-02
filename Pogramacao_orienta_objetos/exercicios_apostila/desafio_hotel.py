# DESAFIO PRÁTICO

# Aplicativo de hotelaria

# Crie uma classe Hotel que permita gerenciar
# funcionários, reservas e quartos de hotel. Os
# funcionários devem ter informações como nome,
# função e salário. O hotel deve ser capaz de
# receber reservas, atribuí-las a quartos e
# calcular a conta final.



class funcionario:
    def __init__(self,nome,funcao,salario):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario


    def dados(self):
        return (f"Nome :{self.nome},  função: {self.funcao}, salario R${self.salario}")    

jose = funcionario("jose", "garson", 1600.00)
#print(jose.dados())


class hospedi:
    def __init__(self,nome,diarias,quarto):
        self.nome = nome
        self.diarias = diarias
        self.quarto = quarto

    def dados(self):
        return (f"nome : {self.nome}, diarias: {self.diarias}, numero do quarto : {self.quarto} ")

    def total_diarias(self,preco_diari):
        total = preco_diari * self.diarias

        print(f"Total da diaria e igua a : R${total}")

    

carlos = hospedi("carlos miguel", 15, "103 B")

print(carlos.dados())



class hotel:
    
    def __init__(self,nome ):
        self.nome = nome
        self.funcionarios = []
        self.reservas = []

    def dados(self):
        return self.nome 
    
    def reseva(self, hospedi):
        self.reservas.append(hospedi.dados())

    def lista_resevas(self):
        print("lista de resevas")
        print(f"{self.reservas}")    
       
    def contratar(self,funcionario):
        self.funcionarios.append(funcionario.dados())    

    def lista_funcionarios(self):
        print(f"lista de funcionarios")
        print(self.funcionarios ) 


hotel_4k = hotel("hotel_4k")     

print(hotel_4k.dados())

hotel_4k.contratar(jose)

print(hotel_4k.lista_funcionarios())

hotel_4k.reseva(carlos)

print(hotel_4k.lista_resevas())

carlos.total_diarias(40)
