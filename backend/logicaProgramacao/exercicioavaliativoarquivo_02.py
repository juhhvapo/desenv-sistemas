#02 sou o dono de uma concessionaria e vi o sistema do dono da padaria. gostaria de um sistema igual para meus carros.

carros = []

def mostrar_menu():
    print("MENU CONCESSIONÁRIA")
    print("1. Cadastrar carro")
    print("2. Listar carros")
    print("3. Alterar carro")
    print("4. Excluir carro")
    print("5. Sair")

def cadastrar():
    nome = input("Nome do carro: ")
    carros.append(nome)
    print("Carro cadastrado com sucesso!")

def listar():
    if not carros:
        print("Nenhum carro cadastrado.")
        return
    print("\n--- Lista de carros ---")
    for i, nome in enumerate(carros):
        print("{i} - {nome}")

def alterar():
    listar()
    try:
        i = int(input("Digite o índice do carro que deseja alterar: "))
        if 0 <= i < len(carros):
            novo_nome = input("Digite o novo nome do carro: ")
            carros[i] = novo_nome
            print("Carro alterado com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def excluir():
    listar()
    try:
        i = int(input("Digite o índice do carro que deseja excluir: "))
        if 0 <= i < len(carros):
            carros.pop(i)
            print("Carro excluído com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

while True:
    mostrar_menu()
    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            alterar()
        elif opcao == 4:
            excluir()
        elif opcao == 5:
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 5.")
    except ValueError: