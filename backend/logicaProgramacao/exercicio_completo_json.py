#Crie um sistema de gerenciamento de petshop.
#Deverá ter os campos: nome, raça, idade, sexo, nome_dono, telefone_dono.
#o nome do arquivo json deve ser "petshop.json"
#faça o crud completo
#ao terminar, demonstrar o exercício para o professor

import json
pets = []
#lendo o arquivo
try:
    with open("petshop.json", "r")as arquivo
        pets = json.load(arquivo)
    
except FileNotFoundError:
    print("Arquivo não encontrado")


try:
    id = int(input("Digite o id do pet: "))
    nome = int(input("Digite o nome do pet: "))
    raca = input("Digite a raça do pet: ")
    idade = input("Digite a idade do pet: ")
    sexo = input("Digite o sexo (M/F): ")
    nome_dono = input("Digite o nome do dono: ")
    telefone_dono = input("Digite o telefone do dono: ")

except ValueError:
    print("Digite os valores corretamente!")

#montar o produto
novo_pet = {"id": id,
            "nome": nome,
            "raca": raca,
            "idade": idade,
            "sexo": sexo,
            "nome_dono": nome_dono,
            "telefone_dono": telefone dono
            }

pets.append (novo_pet)
with open ("petshop.json", "w")as arquivo: 
    json.dump(pets, arquivo, indent=4)
   
    print("pet cadastrado com sucesso")


#---- Modificar pets ----
id_pets_modificar = int(input("Digite o id para modificar: "))
novo_nome = int(input("Digite o novo nome: "))
nova_raca = input("Digite a nova raça: ")
nova_idade = input("Digite a nova idade: ")
novo_sexo = input("Digite o novo sexo: ")
novo_nome_dono = input("Digite o novo nome do dono: ")
novo_telefone_dono = input("Digite o novo telefone do dono: ")

for pet in pets:
    if pets['id'] == id_pets_modificar:
        pet['nome'] = novo_nome
        pet['raca'] = nova_raca
        pet['idade'] = nova_idade
        pet['sexo'] = novo_sexo
        pet_encontrado = True
        break;

if not pet_encontrado:
    print("o pet com o id informado não foi encontrado")

else:
    with open ("petshop.json", "w") as arquivo:
        json.dump(inventario, arquivo, indent = 4)
    print("o arquivo foi alterado com sucesso!!")


#listar pet do arquivo json
    
try:
    with open ("petshop.json",'r') as arquivo:
        inventario= json.load(arquivo)

    if not inventario:
        print("O arquivo está vazio!")

    else:
        print("----- Lista de pets cadastrados -----")
        for pet in inventario:
            print(f"\n-- Pet {pet.get('id')} --")
            print(f"Nome: {pet.get('nome', 'n/a')}")
            print(f"Raça: {pet.get('raca', 'n/a')}")
            print(f"Sexo: {pet.get('sexo', 'n/a')}")
            print(f"Idade: {pet.get('idade', 0)} anos")
            print(f"Nome do dono: {pet.get('nome_dono', 'n/a')}")
            print(f"Telefone do dono: {pet.get('telefone_dono', 'n/a')}")

except FileNotFoundError:
    print("arquivo não encontrado")


#excluir pet no json

try:
    with open("petshop.json", "r") as arquivo:
        inventario = json.load(arquivo)

except FileNotFoundError:
    print("Arquivo não encontrado")


novo_inventario = []
pet_excluido = False

id_pet_excluir = int(input("digite o  id do pet para excluir: "))

for pet in inventario:
    if pet["id"] != id_pet_excluir:
    #se o id for diferente adicionamos  a nova lista 
        novo_inventario.append(pet)
    else:
        print("pet removido com sucesso!!")
        pet_excluido = True

else:
    with open('petshop.json', 'w') as arquivo:
        json.dump(novo_inventario, arquivo, indent=4)
        print('o arquivo foi atualizado, pet removido')


