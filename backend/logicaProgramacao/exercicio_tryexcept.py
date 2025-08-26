#1.Usando(laços~, função e try/except, 
#crie um sistema para receber as 3 notas de um aluno e calcule a média anual 
#se digitar algo sem ser número, tratar o erro)

#2. Usando (lista,função, laços, try/except), você deverá criar uma lista com números e mensagens.
#Se for número, adicionar a uma lista a parte.
#se for mensagem, tratar com o erro de tipo. Ao final, mostrar a lista só com os números

#1
def media():
    try:

        nota1 = float(input("Nota da Prova 1: ")) 
        nota2 = float(input("Nota da Prova 2: ")) 
        nota3 = float(input("Nota da Prova 3: ")) 


        media = nota1 + nota2 + nota3 /3
        print("soma:", media)
       
    except TypeError:
        print("Erro: - Não é possível somar tipos incompatíveis.")

    except ValueError:
        print("Erro: você digitou algo que não é um número.")

    except NameError:
        print("Erro: - Variável não definida.")


media()

#2
def filtrar_numeros(lista_mista):
    numeros = []
    
    for item in lista_mista:
        try:
           
            resultado = item * 1
            numeros.append(item)
        except TypeError:
            print(f"Ignorando valor não numérico: '{item}'")
    
    return numeros

lista_original = [10, "Olá", 25, "Erro", 42, "Mensagem", -7, 3.14, "Fim"]

lista_numeros = filtrar_numeros(lista_original)

print("Lista com apenas números:", lista_numeros)

