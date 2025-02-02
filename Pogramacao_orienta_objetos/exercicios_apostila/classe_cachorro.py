class cachorro:

    def __init__(self,nome,raca,idade):
        self.nome = nome
        self.raca =  raca
        self.idade = idade
        

    def paciar(self): 

        return (f"levar {self.nome} para paciar")
    
    def dados(self):
        return (f"nome do animal: {self.nome} \n raça: {self.raca} \n idade : {self.idade} ")


meu_cachorro = cachorro("Bidu","pitibul",3)

print(meu_cachorro.nome)

meu_cachorro.paciar()   

print(meu_cachorro.idade)

print(meu_cachorro.dados())