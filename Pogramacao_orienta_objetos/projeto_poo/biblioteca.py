
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
       
       if id_usuario in  self.usuarios:
          id_usuario.receber_livros(titulo_livro)
          titulo_livro.disponivel = False
       else:
           return "Usuario inesistente"

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
            if livro.disponivel:
                print(livro)
        

