# Projeto Orientação a objetos
Bem vindos ao projeto de orientação a objetos. Aqui, você irá criar um 
sistema de biblioteca universitária. O sistema deve permitir adicionar livros, 
usuários, e realizar empréstimos e devoluções de livros. Vamos usar os conceitos 
de POO para modelar as entidades e suas interações.

---

## Exemplo de Uso

```python
# Criando alguns livros
livro1 = Livro("1984", "George Orwell", 1949)
livro2 = LivroDidatico("Matemática Básica", "João Silva", 2010, "Matemática")

# Criando alguns usuários
usuario1 = Professor("Carlos Souza", 1, "Ciência da Computação")
usuario2 = Aluno("Ana Costa", 2, "Engenharia")

# Criando a biblioteca e adicionando livros e usuários
biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_usuario(usuario1)
biblioteca.adicionar_usuario(usuario2)

# Realizando empréstimos
biblioteca.emprestar_livro(1, "1984")
biblioteca.emprestar_livro(2, "Matemática Básica")

# Listando livros e usuários
biblioteca.listar_livros()
biblioteca.listar_usuarios()
```

## Criando as classes
Crie as seguintes classes com os seguintes atributos **em arquivos separados** (`livro.py`, `usuario.py`, `biblioteca.py`):

***as classes herdeiras e as suas instâncias devem estar dentro desses arquivos***

### 1. Classe `Livro`
Representa um livro na biblioteca.

#### Atributos:
- `titulo` (string): Título do livro.
- `autor` (string): Autor do livro.
- `ano_publicacao` (int): Ano de publicação do livro.
- `disponivel` (bool): Indica se o livro está disponível para empréstimo.

#### Métodos:
- `emprestar()`: Marca o livro como indisponível.
- `devolver()`: Marca o livro como disponível.
- `__str__()`: Retorna uma representação legível do livro.

---

### 2. Classe `Usuario`
Representa um usuário da biblioteca.

#### Atributos:
- `nome` (string): Nome do usuário.
- `id` (int): ID único do usuário.
- `livros_emprestados` (lista de `Livro`): Lista de livros emprestados pelo usuário.

#### Métodos:
- `emprestar_livro(livro)`: Adiciona um livro à lista de livros emprestados.
- `devolver_livro(livro)`: Remove um livro da lista de livros emprestados.
- `__str__()`: Retorna uma representação legível do usuário.

---

### 3. Classe `Biblioteca`
Gerencia os livros e usuários da biblioteca.

#### Atributos:
- `livros` (lista de `Livro`): Lista de livros cadastrados.
- `usuarios` (lista de `Usuario`): Lista de usuários cadastrados.

#### Métodos:
- `adicionar_livro(livro)`: Adiciona um livro à biblioteca.
- `adicionar_usuario(usuario)`: Adiciona um usuário à biblioteca.
- `emprestar_livro(id_usuario, titulo_livro)`: Realiza o empréstimo de um livro para um usuário.
- `devolver_livro(id_usuario, titulo_livro)`: Realiza a devolução de um livro por um usuário.
- `listar_livros()`: Lista todos os livros da biblioteca.
- `listar_usuarios()`: Lista todos os usuários da biblioteca.
- `listar_livros_emprestados()`: Lista todos os livros que um usuário tem atualmente.

---

### 4. Classe `LivroDidatico` (Herda de `Livro`)
Representa um livro didático.

#### Atributos Adicionais:
- `disciplina` (string): Disciplina à qual o livro pertence.

#### Métodos:
- `__str__()`: Sobrescreve o método para incluir a disciplina.

---

### 5. Classe `LivroInfantil` (Herda de `Livro`)
Representa um livro infantil.

#### Atributos Adicionais:
- `faixa_etaria` (string): Faixa etária recomendada para o livro.

#### Métodos:
- `__str__()`: Sobrescreve o método para incluir a faixa etária.

---

### 6. Classe `Professor` (Herda de `Usuario`)
Representa um professor usuário da biblioteca.

#### Atributos Adicionais:
- `departamento` (string): Departamento ao qual o professor pertence.

#### Métodos:
- `__str__()`: Sobrescreve o método para incluir o departamento.

---

### 7. Classe `Aluno` (Herda de `Usuario`)
Representa um aluno usuário da biblioteca.

#### Atributos Adicionais:
- `curso` (string): Curso no qual o aluno está matriculado.

#### Métodos:
- `__str__()`: Sobrescreve o método para incluir o curso.

---

### [boa sorte!] 8. Classe `LivroDidaticoInfantil` (Herança Múltipla de `LivroDidatico` e `LivroInfantil`)
Representa um livro didático infantil.

#### Métodos:
- `recomendar()`: Imprime uma mensagem recomendando o livro para crianças da faixa etária especificada.

---

## [boa sorte!] Menu de Interação

O sistema possui um menu interativo onde o usuário pode escolher entre as seguintes opções:

1. **Adicionar Livro**: Adiciona um livro normal, didático ou infantil.
2. **Adicionar Usuário**: Adiciona um usuário normal, professor ou aluno.
3. **Emprestar Livro**: Realiza o empréstimo de um livro para um usuário.
4. **Devolver Livro**: Realiza a devolução de um livro por um usuário.
5. **Listar Livros**: Lista todos os livros cadastrados na biblioteca.
6. **Listar Usuários**: Lista todos os usuários cadastrados na biblioteca.
7. **Sair**: Encerra o programa.

---

## Como Usar

1. Execute o programa.
2. Escolha uma opção do menu digitando o número correspondente.
3. Siga as instruções para adicionar livros, usuários, realizar empréstimos, devoluções ou listar dados.