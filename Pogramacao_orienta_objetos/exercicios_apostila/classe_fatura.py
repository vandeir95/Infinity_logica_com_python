# Crie uma classe chamada Fatura , a classe Fatura deve incluir
# os seguintes atributos o nome do item; o preço unitário do item;
# quantidade de item a ser faturado; valor total da fatura; Sua
# classe deve ter um construtor que inicialize todos os atributos
# menos o valor total da fatura. Forneça um método chamado
# gerar_fatura que calcula o valor da fatura 
# (isto é, multiplicar a quantidade pelo preço por item).


class fatura :
    def __init__(self,nome):
        self.nome = nome
        self.itens = []
        
    def compra(self,item) :
        self.itens.append(item)
        
    def exibir_fatura(self):
        for i in self.itens:
            print(i)

         

    def total_fatura(self):
        total= 0
        for i in self.itens:
            
            valor = sum(i.values())
            total+= valor
        print(f"Total da fattura e igua a R$ {total}  ")
       
        
           




            
cartao_inter = fatura('cartao_inter')    
cartao_inter.compra({"blusa":24.99})
cartao_inter.compra({"carteira":14.99})
cartao_inter.compra({"pedagio":4.99})

print(cartao_inter.exibir_fatura())
print(cartao_inter.total_fatura())