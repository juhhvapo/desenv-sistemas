#{} - Chaves: Definir um objeto - ficha de cadastro 
#[] - Colchete: Definir uma lista
#Chave/valor: chave descreve o valor Exemplo: chave: numero; Valor: 4499999-9999


#Sempre importar o json
import json 
inventario = []
#lendo o arquivo
try:
    with open ("loja.json", "r") as arquivo:
        inventario = json.load (arquivo)

except FileNotFoundError:
    print("arquivo não encontrado")


try:
    id = int(input("Digite o id do produto: "))
    nome = input ("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: ")) 
    preco = float(input("Digite o preço: "))

except ValueError:
    print("digite o valor corretamente")


#Montar o objeto
novo_produto = {"id": id,
                "nome": nome,
                "quantidade": quantidade,
                "preco": preco,
                "em_estoque": quantidade > 0 #expressão verdadeiro falso
                }


#Escrever o objeto no arquivo
inventario.append (novo_produto)
with open ("loja.json", "w")as arquivo: 
    json.dump (inventario, arquivo, indent=4)
    #indent - formatar o arquivo json

    print("produto cadastrado com sucesso")


#----- Modificar produto -----

id_produto_modificar = int(input("Digite o id para modificar: "))
nova_quantidade = int(input("Digite a nova quantidade: "))

try:
    with open("loja.json", "r") as arquivo:
        inventario = json.load(arquivo)

except FileNotFoundError:
    print("Arquivo não encontrado")

produto_encontrado = False

for produto in inventario:
    if produto['id'] == id_produto_modificar:
    #colocamos a nova quantidade
        produto['quantidade'] = nova_quantidade
        produto['em_estoque'] = nova_quantidade > 0
        produto_encontrado = True
        break;

if not produto_encontrado:
    print("O produto com o id informado não foi encontrado")

else:
    with open("loja.json", "w")as arquivo:
        json.dump(inventario, arquivo, indent=4)
    print("o arquivo foi alterado com sucesso!!")
    



