#01 eu, como dono de uma padaria quero um sistema de onde eu possa cadastrar meus produtos,alem de poder listar, alterar em caso de error, 
#e excluir quando acabar o estoque.Quero tambem que tenha um menu onde eu possa ver as opções possiveis

produtos = []

def menu():                                             #FAZ ESSE "DEF" PRA APARECER O MENU QUANDO EXECUTAR
    print("MENU")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Alterar produto")
    print("4. Excluir produto")
    print("5. Sair")

def cadastrar():                                        #FAZ ESSE "DEF" PRA APARECER O MENU CADASTRAR QUANDO EXECUTAR DEPOIS ELE VAI TE PEDIR O NOME COM O INPUT
    nome = input("Nome do produto: ")
    produtos.append(nome)                               #é um método da lista em Python que adiciona um item no final da lista.
    print("Produto cadastrado!")

def listar():                                           #FAZ ESSE "DEF" PRA APARECER O MENU CADASTRAR QUANDO EXECUTAR DEPOIS ELE VAI TE PEDIR O NOME COM O INPUT
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
    for i, nome in enumerate(produtos):             #Esse é um laço for com enumerate(), usado para percorrer a lista de produtos.
        print(f"{i} - {nome}")                      #Mostra o índice (ID) e o nome do produto

def alterar():
    listar()                                             #Chama a função listar() antes de tudo, para mostrar ao usuário quais produtos existem e seus respectivos IDs (índices)
    try:
    i = int(input("ID do produto para alterar: "))  #Pede ao usuário para digitar o ID (índice) do produto que ele quer alterar.
    if 0 <= i < len(produtos):                      #Verifica se o ID digitado está dentro do intervalo válido da lista:
    novo_nome = input("Novo nome: ")            #Se o ID for válido, o programa pede ao usuário para digitar o novo nome do produto.
    produtos[i] = novo_nome                     #produtos[i] acessa o produto na posição i da lista.
        print("Produto alterado!")
else:
    print("ID inválido.")
except ValueError:                                      #ocorre quando uma função recebe um argumento com o tipo de dado correto, mas com um valor inadequado para a operação
    print("Por favor, digite um número válido.")

def excluir():
    listar()
    try:
    i = int(input("ID do produto para excluir: "))   #Pede ao usuário que digite o ID (índice) do produto que ele deseja excluir.
    if 0 <= i < len(produtos):                       #Verifica se o número digitado (i) está dentro de uma faixa válida de índices da lista produtos.
    produtos.pop(i)                              #Remove o produto da lista produtos na posição i.
        print("Produto excluído!")
    else:                                              #Se o número digitado não for um índice válido (menor que 0 ou maior/igual ao tamanho da lista), essa mensagem será exibida.
        print("ID inválido.")
    except ValueError:                                      #ocorre quando uma função recebe um argumento com o tipo de dado correto, mas com um valor inadequado para a operação
        print("Por favor, digite um número válido.")

while True:                                         #Isso cria um laço infinito, ou seja, o programa vai continuar rodando até que o usuário escolha sair
    menu()
    opcao = input("Opção: ")
    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        listar()
    elif opcao == '3':
        alterar()
    elif opcao == '4':
        excluir()
    elif opcao == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Digite um número de 1 a 5.")
        except ValueError:
