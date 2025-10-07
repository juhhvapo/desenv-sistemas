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



