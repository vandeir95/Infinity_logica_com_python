class Livro:
    def __init__(self,titulo,autor,ano_publicacao,):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self,):

        self.disponivel = False

    def devolver (self):

        self.disponivel = True 

    def __str__(self):
        return f"{self.titulo} {self.autor} ano de publicaçaõ {self.ano_publicacao} disponivel {self.disponivel}"       


class LivroDidatico(Livro):
    def __init__(self, titulo, autor, ano_publicacao,diciplina):
        super().__init__(titulo, autor, ano_publicacao)

        self.diciplina = diciplina
        

    def __str__(self):
        return f"{self.titulo} {self.autor} ano de publicaçaõ {self.ano_publicacao} disponivel {self.disponivel}, diciplina {self.diciplina}"       
    
class LivroInfatil(Livro):
    def __init__(self, titulo, autor, ano_publicacao, disponivel,faixa_etaria):
        super().__init__(titulo, autor, ano_publicacao, disponivel)    
        self.faixa_etaria = faixa_etaria

    def __str__(self):
        return f"{self.titulo} {self.autor} ano de publicaçaõ {self.ano_publicacao} disponivel {self.disponivel}, faixa etaria {self.faixa_etaria}"       
    