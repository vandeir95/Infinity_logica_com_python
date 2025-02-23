from livro import Livro,LivroDidatico
from usuario import Aluno
from usuario import Usuario
from usuario import Professor
from biblioteca import Biblioteca

# # Criando alguns livros
# livro1 = Livro("1984", "George Orwell", 1949)
# livro2 = LivroDidatico("Matemática Básica", "João Silva", 2010, "Matemática")

# # Criando alguns usuários
# usuario1 = professor("Carlos Souza", 1, "Ciência da Computação")
# usuario2 = Aluno("Ana Costa", 2, "Engenharia")  

biblioteca = Biblioteca()
# biblioteca.adicionar_livro(livro1)
# biblioteca.adicionar_livro(livro2)
# biblioteca.adicionar_usuario(usuario1)
# biblioteca.adicionar_usuario(usuario2)

# print(biblioteca.listar_livros())
# print(biblioteca.listar_usuarios())


# usuario2.emprestar_livros(livro1)

# print(usuario2)

# print("lista de livros")

# print(biblioteca.listar_livros())

# print("lista de livros emprestado")

# print(biblioteca.listar_livros_emprestados())


print("------menu--------\n")
print( "1- **Adicionar Livro**")
print("2- **Adicionar Usuário** ")
print ("3- **Emprestar Livro**:")
print("4- **Devolver Livro**")
print("5- **Listar Livros**")
print("6-**Listar Usuários**")
print("7-**Sair**")


     



while True:

    Opcao = int(input("Escolha uma opção: ")) 

    if Opcao == 1 :
        nome_livro = input("Digite o nome do livro: ")

        autor = str(input("digite o autor do livro: "))

        ano_livro = int(input("Digite o ano do livro: "))

        livro= Livro(nome_livro,autor,ano_livro) 
        biblioteca.adicionar_livro(livro)

        # Exibindo as informações do livro
       # print(str(livro))

    elif Opcao == 2: 
            tipo_usuario = int(input("Qual tipo de usuario sera criado ( 1- Aluno, 2- Professor) :"))
            if tipo_usuario == 1:

                nome_Aluno = str(input("Digite o nome do Aluno: "))

                id = int(input("digite id do Aluno: "))

                curso = str(input(("Digite o curso do aluno")))

                aluno= Aluno(nome_Aluno,id,curso) 
                biblioteca.adicionar_usuario(aluno)
                # Exibindo as informações do livro
                #print(str(aluno))

            elif tipo_usuario == 2 :
                nome_pf = input("Digite o nome do professor: ")

                id_pf = str(input("digite id do usuario: "))

                departamento = str(input("Digite o departamento  do professor: "))

                professor = Professor(nome_pf,id_pf,departamento) 
                biblioteca.adicionar_usuario(professor)
                # Exibindo as informações do livro
                #print(str(professor))


            
        
    elif Opcao == 3:
        id_usuario = int(input("digite o id do Usuario: "))
        Nome_livro  =  str(input("digite o nome do Livro: "))
        biblioteca.emprestar_livro(id_usuario, Nome_livro)
        
    elif Opcao == 4:
         livro = input("digite o nome do livro a ser devolvido ")
         biblioteca.devolucao_livro()

    elif Opcao == 5:
         print(biblioteca.listar_livros())  

    elif Opcao == 6:
        print( biblioteca.listar_usuarios())   
    elif Opcao == 7:
        print("programa encerrado")
         
        exit()
    




# usuario1 = professor("Carlos Souza", 1, "Ciência da Computação")
# usuario2 = Aluno("Ana Costa", 2, "Engenharia")