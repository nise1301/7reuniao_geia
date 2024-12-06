# Sistema de Gerenciamento de Biblioteca

# Dicionário para armazenar os livros
biblioteca = {}

# Função para adicionar livros
def adicionar_livro(titulo, autor, quantidade):
    biblioteca[titulo] = {'autor': autor, 'quantidade': quantidade}

    """aqui estamos colocando um dicionario dentro
    do outro a chave titulo tem como valor o dicionario com as chaves autor e quantidade, 
    aqui é possivel usar autor e quantidade ao mesmo tempo como chaves e valores, é como um comportamento misto,
    flexibilidade do python para esse tipo de operação"""

    print(f"Livro '{titulo}' adicionado com sucesso!")


# Função para buscar livros
def buscar_livro(titulo):
    if titulo in biblioteca:
        livro = biblioteca[titulo]
        """atibui a chamada ao dicionario biblioteca com titulo como chave a variavel local livro,
         a finalidade disso é evitar tá chamando esse dicionario aninhado do mesmo jeito como chamariamos
          uma matriz, algo como [] []"""
        print(f"Título: {titulo}\nAutor: {livro['autor']}\nQuantidade de Exemplares: {livro['quantidade']}")

        """ ficaria horrivel e pouco legivel digitar biblioteca[titulo][autor] por exemplo"""
    else:
        print(f"Livro '{titulo}' não encontrado.")


# Função para empréstimo de livro
#chamada sem criar variavel local ;P
"""def emprestar_livro(titulo):
    if titulo in biblioteca:
        if biblioteca[titulo]['quantidade'] > 0:
            biblioteca[titulo]['quantidade'] -= 1
            print(f"Livro '{titulo}' emprestado com sucesso!")
        else:
            print(f"Livro '{titulo}' indisponível para empréstimo.")
    else:
        print(f"Livro '{titulo}' não encontrado.")"""

def emprestar_livro(titulo):
    if titulo in biblioteca:
        livro = biblioteca[titulo]  # E vamos criar  a variável local para o dicionário aninhado ser acessado de um jeito mais clean :D
        if livro['quantidade'] > 0:
            livro['quantidade'] -= 1
            print(f"Livro '{titulo}' emprestado com sucesso!")
        else:
            print(f"Livro '{titulo}' indisponível para empréstimo.")
    else:
        print(f"Livro '{titulo}' não encontrado.")

# Função para devolução de livro
def devolver_livro(titulo):
    if titulo in biblioteca:
        livro = biblioteca[titulo]
        livro['quantidade'] += 1
        print(f"Livro '{titulo}' devolvido com sucesso!")
    else:
        print(f"Livro '{titulo}' não encontrado.")


# Função para listar todos os livros
def listar_livros():
    if biblioteca:
        """Aqui eu só mudei o nome do dicionario aninhado de livro para info, livro fazia sentido nas outras funções,
        mas aqui eu não estou interessada em acessar um livro (onde há momentos que preciso acessar  autor e quantidade como chave)
        no dicionario, mas ele me interessa enquanto valor do dicionario principal. Então atribuir a uma variavel
        local chamada info, de informação, pareceu mais adequado """

        for titulo, info in biblioteca.items():
            """Novamente uso items() para desempacotar o dicionario e quebra-lo nos pares chave/ valor, totulo e info
             são variaveis locais e eu já expliquei o comportamento do info ai mais acima"""
            print(f"Título: {titulo}\nAutor: {info['autor']}\nQuantidade de Exemplares: {info['quantidade']}\n")
    else:
        print("Nenhum livro encontrado na biblioteca.")


# Função para o menu interativo
def menu():
    """ eu não lembro se já falei em outra reunião, mas chamadas a funções sem parametro geralmente são usadas
     só para exibir algo, não precisa de retorno pra mandar o terminal exibir algo"""
    while True:
        """Aqui temos um loop infinito. Depois que o menu é chamado ele fica repetindo o codigo até que a pessoa
         escolha o break , que é o 6 """

        print("\nSistema de Gerenciamento de Biblioteca")
        print("1. Adicionar Livro")
        print("2. Buscar Livro")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Listar Todos os Livros")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Título do Livro: ")
            autor = input("Autor do Livro: ")
            quantidade = int(input("Quantidade de Exemplares: "))
            adicionar_livro(titulo, autor, quantidade)
        elif escolha == '2':
            titulo = input("Título do Livro: ")
            buscar_livro(titulo)
        elif escolha == '3':
            titulo = input("Título do Livro: ")
            emprestar_livro(titulo)
        elif escolha == '4':
            titulo = input("Título do Livro: ")
            devolver_livro(titulo)
        elif escolha == '5':
            listar_livros()
        elif escolha == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Chama o menu para iniciar o sistema
menu()

"""No exercicio dos contatos, experimentei colocar o dicionario no escopo local da função menu, 
enquanto aqui coloquei dentro do escopo global, mas isso teve a ver com a forma como organizei o menu no sistema biblioteca
É que na biblioteca me pareceu mais organizado e viavel pedir um input ao usuario para ele dizer qual titulo queria se 
referir para chamar cada função. Se o escopo do dicionario biblioteca fosse local, toda vida que eu fosse colocar o titulo
como parametro lá ia eu colocar também o biblioteca, já que eu teria que especificar que titulo era uma chave daquele dicionario,
então isso me pareceu contraproducente. Nada disso é necessario em contatos por que aquele menu é estático. O único input do usuario
é a escolha, ele não tem que escrever mais nada depois de escolher o comando, diferente do sistema biblioteca.
"""

# e fim :D

