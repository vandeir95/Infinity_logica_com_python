## **Grupo 3: Classe `ContaBancaria`**

# 15. **Exercício 15**: Crie uma classe `ContaBancaria` com os atributos `numeroConta` (string), `saldo` (double) e `titular` (string).
# Implemente um construtor para inicializar esses atributos.
# 16. **Exercício 16**: Adicione métodos `getNumeroConta()`, `getSaldo()` e `getTitular()` para retornar os valores dos atributos.
# 17. **Exercício 17**: Adicione métodos `setNumeroConta(string numeroConta)`, `setSaldo(double saldo)` e `setTitular(string titular)` 
# para modificar os valores dos atributos.
# 18. **Exercício 18**: Instancie dois objetos da classe `ContaBancaria` com valores diferentes e exiba seus atributos.
# 19. **Exercício 19**: Adicione métodos `depositar(double valor)` e `sacar(double valor)` para modificar o saldo da conta.
# Teste os métodos com uma instância.
# 20. **Exercício 20**: Adicione um atributo `transacoes` (lista de strings) que armazena o histórico de transações (depósitos e saques).
# Modifique os métodos `depositar` e `sacar` para registrar cada transação na lista.
# 21. **Exercício 21**: Crie um método `extrato()` que exibe o histórico completo de transações. Teste o método.
class ContaBancaria:
    def __init__(self,numeroConta,saldo:float,titular):
    
        self.numeroConta = numeroConta
        self.titular = titular
        self.saldo = saldo
        self.transacoes = []
    def __str__(self):
        return f"numeroConta :{self.numeroConta},  saldo: {self.saldo}, titular {self.titular}" 


    def deposito(self,deposito):
        self.saldo = self.saldo + deposito
        self.transacoes.append(["DEPOSITO", deposito])
    def saque(self,saque):
        self.saldo = self.saldo - saque
        self.transacoes.append(["SAQUE",saque])

    def getNumeroConta(self):   

        return self.numeroConta 
    def extrato(self):
        print("EXTRATO DA CONTA :", self.numeroConta)
        for i in self.transacoes:
            print(i)
    def getTitular(self):   

        return self.titular
    
    def getSaldo(self):   

        return (f"R${self.saldo}" )
    
    def setNumeroConta(self,Novo_numero):   

         self.numeroConta =  Novo_numero
    
    def setTitular(self,Noovo_Titular):   

         self.titular = Noovo_Titular
    
    def setSaldo(self,Novo_Saldo):   

         self.saldo = Novo_Saldo


minha_conta = ContaBancaria("105-65", 1500, "vandeir") 

print(vars(minha_conta))

print(minha_conta.getSaldo())

minha_conta.setTitular("vandeir Souza")

minha_conta.saque(1000)

minha_conta.deposito(2500)

minha_conta.deposito(100)

minha_conta.deposito(6600)

minha_conta.deposito(3500)

print(minha_conta.extrato())

print("Novo saldo ")

print(minha_conta.getSaldo())