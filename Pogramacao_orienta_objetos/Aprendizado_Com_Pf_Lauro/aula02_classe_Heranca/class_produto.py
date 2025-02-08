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


Nova_batedeira = Batedeira(499,"itatiaia","250 vw")    

print(vars(Nova_batedeira))

Nova_batedeira.desconto_no_pix(0.3)

class Cigarro(Produto):
    def __init__(self, preco, fornecedor,sabor):
        super().__init__(preco, fornecedor)

        self.sabor = sabor

    def desconto_no_pix(self):
        print(f"Não tem desconto no PIX")


marlbora = Cigarro(15,"Souza Cruz","laramja")   

print(vars(marlbora))

marlbora.desconto_no_pix()
        