class Cliente :
    def __init__(self, nome, cpf):
        self.__nome = nome 
        self.__cpf = cpf 
        self.__produtos_comprados = []
    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf 
    def comprar_produtos(self, produto):
        self.__produtos_comprados.append(produto)
        print(f"{self.get_nome} comprou {produto.__class__.__name__} por  R${produto.preco}")

    def listar_produtos_comprados(self):
        if len(self.__produtos_comprados) == 0:
            print(f"{self.__nome} não comprou nenhum produto ainda ")
        else:
            print(f"Produtos comprados por {self.__nome}: ")
            for produto in self.__produtos_comprados:
                print(f" { produto.__class__.__name__} (R$ {produto.preco})")        
          
    





class Produto:
    def __init__(self,preco,fornecedor):

        self.preco = preco
        self.fornecedor = fornecedor
    def desconto_no_pix(self,porcentagem):
        print("no pix, custa", self.preco*porcentagem)    
        

class Batedeira(Produto):
    def __init__(self, preco, fornecedor,potencia):
        super().__init__(preco, fornecedor)     
        self.potencia = potencia   


  



class Cigarro(Produto):
    def __init__(self, preco, fornecedor,sabor):
        super().__init__(preco, fornecedor)

        self.sabor = sabor

    def desconto_no_pix(self):
        print(f"Não tem desconto no PIX")


 


class Chocolate(Produto):
    def __init__(self, preco, fornecedor,ao_leite):
        super().__init__(preco, fornecedor)

        self.ao_leite = ao_leite

    def desconto_no_pix(self):
        print(f"Não tem desconto no PIX")



marlbora = Cigarro(15,"Souza Cruz","laramja")  
meu_chocolate = Chocolate(15.99,"Nestle",True) 
Nova_batedeira = Batedeira(499,"itatiaia","250 vw") 

cliente1 = Cliente("Lauro", "123456789-00")
print(vars(cliente1))


cliente1.comprar_produtos(marlbora)
cliente1.comprar_produtos(meu_chocolate)
cliente1.comprar_produtos(Nova_batedeira)

print(cliente1.listar_produtos_comprados())
  

        