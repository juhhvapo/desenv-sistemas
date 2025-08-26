#criar uma lista com cadastro de usuario
#cadastrar
#alternar
#excluir                usar (função, lista, tryacepet, laços)
#listar


# Lista para armazenar os usuários
usuarios = []

# Função para cadastrar usuário
def cadastrar_usuario():
    try:
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        email = input("Digite o email do usuário: ")

        usuario = {"nome": nome, "idade": idade, "email": email}
        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")
    except ValueError:
        print("Erro: Idade deve ser um número.")

# Função para listar os usuários
def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("Lista de usuários:")
        for i, u in enumerate(usuarios):
            print("{i}: Nome: {u['nome']}, Idade: {u['idade']}, Email: {u['email']}")
        print()

# Função para editar (alternar) um usuário
def alternar_usuario():
    listar_usuarios()
    try:
        idx = int(input("Digite o índice do usuário que deseja alterar: "))
        if 0 <= idx < len(usuarios):
            nome = input("Novo nome: ")
            idade = int(input("Nova idade: "))
            email = input("Novo email: ")
            usuarios[idx] = {"nome": nome, "idade": idade, "email": email}
            print("✅ Usuário alterado com sucesso!\n")
        else:
            print("❌ Índice inválido.\n")
    except ValueError:
        print("❌ Erro: Entrada inválida.\n")

# Função para excluir usuário
def excluir_usuario():
    listar_usuarios()
    try:
        idx = int(input("Digite o índice do usuário que deseja excluir: "))
        if 0 <= idx < len(usuarios):
            usuarios.pop(idx)
            print("🗑️ Usuário excluído com sucesso!\n")
        else:
            print("❌ Índice inválido.\n")
    except ValueError:
        print("❌ Erro: Entrada inválida.\n")

# Menu principal
def menu():
    while True:
        print("==== MENU ====")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Alterar usuário")
        print("4 - Excluir usuário")
        print("5 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
            print()

            if opcao == 1:
                cadastrar_usuario()
            elif opcao == 2:
                listar_usuarios()
            elif opcao == 3:
                alternar_usuario()
            elif opcao == 4:
                excluir_usuario()
            elif opcao == 5:
                print("👋 Encerrando o programa.")
                break
            else:
                print("❌ Opção inválida.\n")
        except ValueError:
            print("❌ Erro: Digite um número válido.\n")

# Executar o menu
menu()