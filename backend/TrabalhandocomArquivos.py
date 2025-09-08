with open ('compras.txt', "w")
#w --- abrir o arquivo no modo escrita - apaga
#a --- "" "" "" adição - adiciona
#r --- "" "" "" leitura

with open("tarefas.txt", "w") as arquivo:
    arquivo.write("lavar a louça /n")
    arquivo.write("lavar quintal")

#ler o arquivo
with open("compras.txt", "r") as arquivo:
    conteudo = arquivo.read() 
    print(conteudo)

#ler o arquivo linha por linha
with open("compras.txt" "r") as arquivo:
    for produto in compras:
        print("produto:"produto.strip())

#acrescentar dados ao final
with open("compras.txt", "a")as arquivo:
    arquivo.write("arroz")