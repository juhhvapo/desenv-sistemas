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
    nome = input ("digite o nome do produto: ")
    quantidade = int(input("digite a quantidade: ")) 
    preco = float(input("digite o preço: "))

except ValueError:
    print("digite o valor corretamente")


#Montar o objeto
novo_produto = {"nome": nome,
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