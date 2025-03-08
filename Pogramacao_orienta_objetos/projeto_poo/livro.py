class Livro:
    def __init__(self,titulo,autor,ano_publicacao,):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self,):

        self.disponivel = False
        return

    def devolver (self):

         self.disponivel = True 

         return

    def __str__(self):
        return f"{self.titulo} {self.autor} ano de publicaçaõ {self.ano_publicacao} disponivel {self.disponivel}"       


class LivroDidatico(Livro):
    def __init__(self, titulo, autor, ano_publicacao,diciplina):
        super().__init__(titulo, autor, ano_publicacao)

        self.diciplina = diciplina
        self.disponivel = True

    def __str__(self):
        return f"{self.titulo} {self.autor} ano de publicaçaõ {self.ano_publicacao} disponivel {self.disponivel}, diciplina {self.diciplina}"       
    
class LivroInfatil(Livro):
    def __init__(self, titulo, autor, ano_publicacao,faixa_etaria):
        super().__init__(titulo, autor, ano_publicacao)    
        self.faixa_etaria = faixa_etaria
        self.disponivel = True
    def __str__(self):
        return f"{self.titulo} {self.autor} ano de publicaçaõ {self.ano_publicacao} disponivel {self.disponivel}, faixa etaria {self.faixa_etaria}"       
    