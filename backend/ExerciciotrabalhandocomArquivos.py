#exercicio crie um arquivo de nome alunos.txt
#adicione 5 alunos no arquivo - in para quebrar a linha
#confira abrindo o arquivo se escreveu
#leia o arquivo e faça o print de cada aluno no terminal

with open("aluno.txt", "w") as dados:
    dados.write("Maria\n")
    dados.write("Livia\n")
    dados.write("julia\n")
    dados.write("Jorge\n")
    dados.write("Aline\n")
   
   with open("aluno.txt", "r") as dados:
    for alunos in dados:
        print("aluno:", alunos.strip()) 