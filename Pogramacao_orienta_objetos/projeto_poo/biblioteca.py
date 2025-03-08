
class Biblioteca:
    from usuario import Usuario,Aluno,Professor
    from livro import Livro,LivroDidatico,LivroInfatil
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self,livro):
        self.livros.append(livro)    

    def adicionar_usuario(self,Usuario):
        self.usuarios.append(Usuario) 

    def devolucao_livro(self,livro):
        for livro in self.livros:
            livro.devolver()   

    def emprestar_livro(self,id_usuario, titulo_livro):
       
        for usuario in self.usuarios  :
            if usuario.id == id_usuario: 
             titulo_livro.emprestar()
             usuario.receber_livros(titulo_livro)  
            
             
            
               
               
             
              
           
          
       

    # def devolver_livro(self,id_usuario, titulo_livro):  
    #     pass

    def listar_livros(self):
        for i in self.livros:
              return(str(i))
        
    def listar_usuarios(self):
        for i in self.usuarios:
            return i    
        
    def listar_livros_emprestados(self):
        for livro in self.livros:
            if livro.disponivel == False:
                return livro
            
    
        
        
        

from livro import Livro,LivroDidatico
from usuario import Aluno
from usuario import Usuario
from usuario import Professor
from biblioteca import Biblioteca

# # Criando alguns livros
# livro1 = Livro("1984", "George Orwell", 1949)
# livro2 = LivroDidatico("Matemática Básica", "João Silva", 2010, "Matemática")

# # Criando alguns usuários
# usuario1 = Professor("Carlos Souza", 1, "Ciência da Computação")
# usuario2 = Aluno("Ana Costa", 2, "Engenharia")  

# biblioteca = Biblioteca()

# biblioteca.adicionar_livro(livro1)
# biblioteca.adicionar_livro(livro2)
# biblioteca.adicionar_usuario(usuario1)
# biblioteca.adicionar_usuario(usuario2)


# print("biblioteca empresta o livro")
# biblioteca.emprestar_livro(2,livro1) 
# biblioteca.emprestar_livro(2,livro2)

# print(biblioteca.listar_livros_emprestados())


# #livro1.emprestar()
# # print(biblioteca.listar_livros())
# # print(biblioteca.listar_usuarios())

# # print(biblioteca.listar_usuarios())
    



# usuario2.emprestar_livros(livro1)

# print(usuario2)

# print("lista de livros")

# print(biblioteca.listar_livros())

# print("lista de livros emprestado")

# print(biblioteca.listar_livr