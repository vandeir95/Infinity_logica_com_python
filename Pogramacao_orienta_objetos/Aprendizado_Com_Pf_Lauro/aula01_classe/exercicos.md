# Exercícios de Programação Orientada a Objetos

## **Grupo 1: Classe `Pessoa`**

1. **Exercício 1**: Crie uma classe `Pessoa` com os atributos `nome` (string) e `idade` (int). Implemente um construtor para inicializar esses atributos.
2. **Exercício 2**: Adicione métodos `getNome()` e `getIdade()` para retornar os valores dos atributos `nome` e `idade`.
3. **Exercício 3**: Adicione métodos `setNome(string nome)` e `setIdade(int idade)` para modificar os valores dos atributos.
4. **Exercício 4**: Instancie dois objetos da classe `Pessoa` com valores diferentes e exiba seus atributos.
5. **Exercício 5**: Adicione um método `fazerAniversario()` que incrementa a idade da pessoa em 1. Teste o método com uma instância.
6. **Exercício 6**: Adicione um atributo `amigos` (lista de objetos `Pessoa`) e um método `adicionarAmigo(Pessoa amigo)` para adicionar um amigo à lista. Crie um método `listarAmigos()` que exibe os nomes dos amigos.
7. **Exercício 7**: Crie um método `removerAmigo(string nome)` que remove um amigo da lista pelo nome. Teste o método.

---

## **Grupo 2: Classe `Carro`**

8. **Exercício 8**: Crie uma classe `Carro` com os atributos `marca` (string), `modelo` (string) e `ano` (int). Implemente um construtor para inicializar esses atributos.
9. **Exercício 9**: Adicione métodos `getMarca()`, `getModelo()` e `getAno()` para retornar os valores dos atributos.
10. **Exercício 10**: Adicione métodos `setMarca(string marca)`, `setModelo(string modelo)` e `setAno(int ano)` para modificar os valores dos atributos.
11. **Exercício 11**: Instancie três objetos da classe `Carro` com valores diferentes e exiba seus atributos.
12. **Exercício 12**: Adicione um método `idadeCarro(int anoAtual)` que retorna a idade do carro com base no ano atual. Teste o método com uma instância.
13. **Exercício 13**: Adicione um atributo `proprietarios` (lista de objetos `Pessoa`) e um método `adicionarProprietario(Pessoa proprietario)` para adicionar um proprietário à lista. Crie um método `listarProprietarios()` que exibe os nomes dos proprietários.
14. **Exercício 14**: Crie um método `transferirProprietario(Pessoa novoProprietario)` que transfere o carro para um novo proprietário, adicionando-o à lista de proprietários. Teste o método.

---

## **Grupo 3: Classe `ContaBancaria`**

15. **Exercício 15**: Crie uma classe `ContaBancaria` com os atributos `numeroConta` (string), `saldo` (double) e `titular` (string). Implemente um construtor para inicializar esses atributos.
16. **Exercício 16**: Adicione métodos `getNumeroConta()`, `getSaldo()` e `getTitular()` para retornar os valores dos atributos.
17. **Exercício 17**: Adicione métodos `setNumeroConta(string numeroConta)`, `setSaldo(double saldo)` e `setTitular(string titular)` para modificar os valores dos atributos.
18. **Exercício 18**: Instancie dois objetos da classe `ContaBancaria` com valores diferentes e exiba seus atributos.
19. **Exercício 19**: Adicione métodos `depositar(double valor)` e `sacar(double valor)` para modificar o saldo da conta. Teste os métodos com uma instância.
20. **Exercício 20**: Adicione um atributo `transacoes` (lista de strings) que armazena o histórico de transações (depósitos e saques). Modifique os métodos `depositar` e `sacar` para registrar cada transação na lista.
21. **Exercício 21**: Crie um método `extrato()` que exibe o histórico completo de transações. Teste o método.

---

## **Grupo 4: Classe `Produto`**

22. **Exercício 22**: Crie uma classe `Produto` com os atributos `nome` (string), `preco` (double) e `quantidadeEmEstoque` (int). Implemente um construtor para inicializar esses atributos.
23. **Exercício 23**: Adicione métodos `getNome()`, `getPreco()` e `getQuantidadeEmEstoque()` para retornar os valores dos atributos.
24. **Exercício 24**: Adicione métodos `setNome(string nome)`, `setPreco(double preco)` e `setQuantidadeEmEstoque(int quantidade)` para modificar os valores dos atributos.
25. **Exercício 25**: Instancie três objetos da classe `Produto` com valores diferentes e exiba seus atributos.
26. **Exercício 26**: Adicione um método `vender(int quantidade)` que reduz a quantidade em estoque do produto. Se a quantidade for maior que o estoque, exiba uma mensagem de erro. Teste o método com uma instância.
27. **Exercício 27**: Adicione um atributo `compras` (lista de objetos `Pessoa`) que armazena os clientes que compraram o produto. Crie um método `registrarCompra(Pessoa cliente)` para adicionar um cliente à lista.
28. **Exercício 28**: Crie um método `listarClientes()` que exibe os nomes dos clientes que compraram o produto. Teste o método.

---

## **Grupo 5: Classe `Biblioteca`**

29. **Exercício 29**: Crie uma classe `Livro` com os atributos `titulo` (string), `autor` (string) e `anoPublicacao` (int). Implemente um construtor para inicializar esses atributos.
30. **Exercício 30**: Crie uma classe `Biblioteca` com um atributo `acervo` (lista de objetos `Livro`). Implemente um método `adicionarLivro(Livro livro)` para adicionar um livro ao acervo.
31. **Exercício 31**: Adicione um método `buscarLivroPorTitulo(string titulo)` que retorna um livro do acervo com base no título. Se não encontrar, exiba uma mensagem de erro.
32. **Exercício 32**: Adicione um método `listarLivros()` que exibe todos os livros do acervo. Teste o método.
33. **Exercício 33**: Adicione um método `removerLivro(string titulo)` que remove um livro do acervo pelo título. Teste o método.

---

## **Desafios maiores (boa sorte!)**

Suponha que você tem um programa que cria provas objetivas com gabarito utilizando o seguinte código:
``` pythhon
# Gabarito oficial da prova
gabarito_oficial = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B"]

# Respostas do aluno
respostas_aluno = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B"]

# Função para corrigir a prova
def corrigir_prova(gabarito, respostas):
    if len(gabarito) != len(respostas):
        return "Número de questões incorreto."
    
    nota = 0
    for i in range(len(gabarito)):
        if gabarito[i] == respostas[i]:
            nota += 1
    
    return nota

# Corrigindo a prova
nota_final = corrigir_prova(gabarito_oficial, respostas_aluno)
print(f"Nota do aluno: {nota_final}")
```

Refaça o código acima utilizando a Programação Orientada a Objetos. Crie uma classe `Prova` com o atributo `gabarito`(lista de strings) e um método `corrigir`, que deverá retornar a nota do aluno.
Além dela, crie a classe `Aluno`, com os atributos `nome`(string) e `respostas`(lista de strings) e o método `calcular nota`, que deverá utilizar o método `corrigir` criado na classe `Prova`,
comparando as suas `respostas` com o `gabarito da prova` pra determinar quantas questões ele acertou