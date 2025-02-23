class Usuario:
    def __init__(self,nome,id):
        self.nome = nome
        self.id = id
        self.livros_emprestado = []

    def receber_livros(self, livro):
        self.livros_emprestado.append(livro)
        livro.empresta()

    def devolver_livro(self,livro):
        self.livros_emprestado.remove(livro)    

    def __str__(self):
        return f"{self.nome} ID : {self.id}"    
    
class Professor(Usuario):
    def __init__(self, nome, id,departamento):
        super().__init__(nome, id)

        self.departamento = departamento

    def __str__(self):
        return f"{self.nome} ID : {self.id} departamento {self.departamento}"    


class Aluno(Usuario):
    def __init__(self, nome, id,curso):
        super().__init__(nome, id)
        self.curso = curso


    def __str__(self):
        return f"{self.nome} ID : {self.id} curso {self.curso} "    
    