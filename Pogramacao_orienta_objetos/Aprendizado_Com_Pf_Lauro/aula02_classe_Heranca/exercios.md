# Exercícios Práticos de Programação Orientada a Objetos

## Grupo 1: Classe `Veículo`

1. **Exercício 1**: Crie uma classe `Veículo` com um método `mover()` que imprime "O veículo está se movendo". Crie uma classe `Carro` que herda de `Veículo` e sobrescreve o método `mover()` para imprimir "O carro está andando na estrada".

2. **Exercício 2**: Adicione um atributo `marca` à classe `Veículo` e um método `apresentar()` que imprime "Este veículo é da marca [marca]". Crie uma classe `Moto` que herda de `Veículo` e sobrescreve o método `apresentar()` para incluir "Esta moto é da marca [marca]".

3. **Exercício 3**: Crie uma classe `Caminhão` que herda de `Veículo` e sobrescreve o método `mover()` para imprimir "O caminhão está transportando carga". Adicione um método `carregar()` que imprime "Caminhão carregado!".

4. **Exercício 4**: Crie uma classe `Bicicleta` que herda de `Veículo` e sobrescreve o método `mover()` para imprimir "A bicicleta está pedalando". Adicione um método `parar()` que imprime "Bicicleta parada".

5. **Exercício 5**: Crie uma lista de objetos do tipo `Veículo` que contenha instâncias de `Carro`, `Moto`, `Caminhão` e `Bicicleta`. Use um loop para chamar o método `mover()` de cada objeto, demonstrando polimorfismo.

---

## Grupo 2: Classe `FormaGeométrica`

1. **Exercício 6**: Crie uma classe `FormaGeométrica` com um método `calcularArea()` que retorna 0. Crie uma classe `Quadrado` que herda de `FormaGeométrica` e sobrescreve o método `calcularArea()` para calcular a área de um quadrado (lado * lado).

2. **Exercício 7**: Crie uma classe `Círculo` que herda de `FormaGeométrica` e sobrescreve o método `calcularArea()` para calcular a área de um círculo (π * raio²). Use π = 3.14.

3. **Exercício 8**: Adicione um método `calcularPerimetro()` à classe `FormaGeométrica` que retorna 0. Sobrescreva esse método nas classes `Quadrado` e `Círculo` para calcular o perímetro de cada forma.

4. **Exercício 9**: Crie uma classe `Triângulo` que herda de `FormaGeométrica` e implementa os métodos `calcularArea()` e `calcularPerimetro()` para um triângulo equilátero.

5. **Exercício 10**: Crie uma lista de objetos do tipo `FormaGeométrica` que contenha instâncias de `Quadrado`, `Círculo` e `Triângulo`. Use um loop para chamar os métodos `calcularArea()` e `calcularPerimetro()` de cada objeto, demonstrando polimorfismo.

---

## Grupo 3: Classe `Funcionário`

1. **Exercício 11**: Crie uma classe `Funcionário` com um método `calcularSalario()` que retorna 0. Crie uma classe `FuncionárioCLT` que herda de `Funcionário` e sobrescreve o método `calcularSalario()` para retornar um salário fixo.

2. **Exercício 12**: Crie uma classe `FuncionárioPJ` que herda de `Funcionário` e sobrescreve o método `calcularSalario()` para retornar o valor de um contrato mensal.

3. **Exercício 13**: Adicione um atributo `nome` à classe `Funcionário` e um método `apresentar()` que imprime "Eu sou [nome]". Sobrescreva esse método nas classes `FuncionárioCLT` e `FuncionárioPJ` para incluir o tipo de contrato.

4. **Exercício 14**: Crie uma classe `Estagiário` que herda de `Funcionário` e sobrescreve o método `calcularSalario()` para retornar uma bolsa-auxílio.

5. **Exercício 15**: Crie uma lista de objetos do tipo `Funcionário` que contenha instâncias de `FuncionárioCLT`, `FuncionárioPJ` e `Estagiário`. Use um loop para chamar os métodos `calcularSalario()` e `apresentar()` de cada objeto, demonstrando polimorfismo.

---

## Grupo 4: Classe `Produto`

1. **Exercício 16**: Crie uma classe `Produto` com um método `calcularPreco()` que retorna 0. Crie uma classe `Livro` que herda de `Produto` e sobrescreve o método `calcularPreco()` para retornar o preço de um livro com 10% de desconto.

2. **Exercício 17**: Crie uma classe `Eletrônico` que herda de `Produto` e sobrescreve o método `calcularPreco()` para retornar o preço de um eletrônico com 5% de imposto.

3. **Exercício 18**: Adicione um atributo `nome` à classe `Produto` e um método `descrever()` que imprime "Este produto é um [nome]". Sobrescreva esse método nas classes `Livro` e `Eletrônico` para incluir detalhes específicos.

4. **Exercício 19**: Crie uma classe `Roupa` que herda de `Produto` e sobrescreve o método `calcularPreco()` para retornar o preço de uma roupa com 20% de desconto.

5. **Exercício 20**: Crie uma lista de objetos do tipo `Produto` que contenha instâncias de `Livro`, `Eletrônico` e `Roupa`. Use um loop para chamar os métodos `calcularPreco()` e `descrever()` de cada objeto, demonstrando polimorfismo.

---

Esses exercícios cobrem herança, sobrescrita de métodos e polimorfismo de forma gradual e prática. Eles podem ser adaptados conforme o nível dos seus alunos. Boa sorte com o bootcamp! 😊