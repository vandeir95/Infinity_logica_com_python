# ## **Grupo 5: Classe `Biblioteca`**

# 29. **Exercício 29**: Crie uma classe `Livro` com os atributos `titulo` (string), `autor` (string) e `anoPublicacao` (int).
# Implemente um construtor para inicializar esses atributos.
# 30. **Exercício 30**: Crie uma classe `Biblioteca` com um atributo `acervo` (lista de objetos `Livro`). 
# Implemente um método `adicionarLivro(Livro livro)` para adicionar um livro ao acervo.
# 31. **Exercício 31**: Adicione um método `buscarLivroPorTitulo(string titulo)
# ` que retorna um livro do acervo com base no título. Se não encontrar, exiba uma mensagem de erro.
# 32. **Exercício 32**: Adicione um método `listarLivros()` que exibe todos os livros do acervo. Teste o método.
# 33. **Exercício 33**: Adicione um método `removerLivro(string titulo)` que remove um livro do acervo pelo título. Teste o método.

# ---


class Livro:
    def __init__(self,titulo:str,autor:str,ano_Plublicacao:int):

        self.titulo = titulo
        self.autor = autor
        self.ano_Plublicacao = ano_Plublicacao

        # Método __str__ para representação legível do livro
    def __str__(self):
        return f"Nome: {self.titulo}, Autor: {self.autor}, Ano de publicação: {self.ano_Plublicacao}"

busca_pela_fe = Livro("busca pela Fé", "jose maria", 2012)


pela_fe = Livro(" pela Fé", "Vandeir", 2002)


Jesus = Livro("Jesu", "Beatris", 2022)



class Biblioteca:
    def __init__(self,nome):
        self.nome = nome
        self.acervo = []

    def listar_livros(self):
         for livro in self.acervo:
              print(livro)
    def remover_livro(self,livro):
         self.acervo.remove(livro)
                 

    def adicionar_livros(self,livro:Livro):
        self.acervo.append(livro)
        
    def buscar_livros(self,livro:Livro):
        
            if livro in self.acervo:
                print("Livro encontrado ", livro) 
            else: 
                print("livro não encontrado")
                return None


minha_biblioteca = Biblioteca("minha bibioteca")

minha_biblioteca.adicionar_livros(busca_pela_fe)

minha_biblioteca.adicionar_livros(Jesus)

minha_biblioteca.adicionar_livros(pela_fe)
minha_biblioteca.listar_livros()

print("remover livro")

minha_biblioteca.remover_livro(pela_fe)

minha_biblioteca.listar_livros()


# print(vars(busca_pela_fe))

# print("minha biblioteca ")


# minha_biblioteca.adicionar_livros(busca_pela_fe)

# # Listar os livros
# print("Livros na biblioteca:")
# minha_biblioteca.listar_livros()

# print(minha_biblioteca.listar_livros())



