from livro import Livro,LivroDidatico,LivroInfatil
from usuario import Aluno
from usuario import Usuario
from usuario import Professor
from biblioteca import Biblioteca

biblioteca = Biblioteca()


menu = ( "    -----meunu----- \n 1- **Adicionar Livro** \n 2- **Adicionar Usuário** \n 3- **Emprestar Livro**: \n 4- **Devolver Livro** \n 5- **Listar Livros** \n 6-**Listar Usuários** \n 7-**Sair** ")




     


print(menu)

while True:

    Opcao = int(input("Escolha uma opção: ")) 

    if Opcao == 1 :
        tipo_livro = int(input("Qual tipo de livro sera criado (1- Livro Didatico, 2- Livro Infantil)"))
        if tipo_livro == 1 :
            nome_livro = input("Digite o nome do livro: ")

            autor = str(input("digite o autor do livro: "))

            ano_livro = int(input("Digite o ano do livro: "))
            disciplina = str(input("Digite o nome da disciplina: "))
            livro = nome_livro
            livro = LivroDidatico(nome_livro,autor,ano_livro,disciplina) 
            biblioteca.adicionar_livro(livro)
            print(menu)

        if tipo_livro == 2 :
            nome_livro = input("Digite o nome do livro: ")

            autor = str(input("digite o autor do livro: "))

            ano_livro = int(input("Digite o ano do livro: "))

            
            faixa_etaria = int(input("Digite a Faixa etaria:"))
            livro = nome_livro
            livro = LivroInfatil(nome_livro,autor,ano_livro,faixa_etaria) 
            biblioteca.adicionar_livro(livro)
            print(menu)
        # Exibindo as informações do livro
       # print(str(livro))

    elif Opcao == 2: 
            tipo_usuario = int(input("Qual tipo de usuario sera criado ( 1- Aluno, 2- Professor) :"))
            if tipo_usuario == 1:

                nome_Aluno = str(input("Digite o nome do Aluno: "))

                id = int(input("digite id do Aluno: "))

                curso = str(input(("Digite o curso do aluno :")))
                
                aluno = nome_Aluno
                aluno= Aluno(nome_Aluno,id,curso) 

                biblioteca.adicionar_usuario(aluno)
                print(menu)
                # Exibindo as informações do livro
                #print(str(aluno))

            elif tipo_usuario == 2 :
                nome_pf = input("Digite o nome do professor: ")

                id_pf = str(input("digite id do usuario: "))

                departamento = str(input("Digite o departamento  do professor: "))
                
                professor = nome_pf

                professor = Professor(nome_pf,id_pf,departamento) 
                biblioteca.adicionar_usuario(professor)
                print(menu)
                # Exibindo as informações do livro
                #print(str(professor))


            
        
    elif Opcao == 3:
        id_usuario = int(input("digite o id do Usuario: "))
        Nome_livro  =  str(input("digite o nome do Livro: "))
        biblioteca.emprestar_livro(id_usuario, Nome_livro)
        print(menu)
        
    elif Opcao == 4:
         livro = input("digite o nome do livro a ser devolvido :")
         biblioteca.devolucao_livro()
         print(menu)

    elif Opcao == 5:
         print(biblioteca.listar_livros())  
         print(menu)

    elif Opcao == 6:
        print( biblioteca.listar_usuarios()) 
        print(menu)  
    elif Opcao == 7:
        print("programa encerrado")
         
        exit()
    




# usuario1 = professor("Carlos Souza", 1, "Ciência da Computação")
# usuario2 = Aluno("Ana Costa", 2, "Engenharia")