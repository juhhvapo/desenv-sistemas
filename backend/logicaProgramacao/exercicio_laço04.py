senhacorreta = input("Digite a senha correta:")
senha = input("Digite a senha:")
nome = input("Digite o seu nome:")
salario = float (input("Digite seu salario:"))

while senha!= senhacorreta: 
    print("senha incorreta")
    senha= input("Digite a senha novamente:")

    print("Bem-vindo", nome)

    salarioanual= salario * 12 

if(salarioanual > 1000000):
    print("rico")
else:
    print("Faz o L")