nota = int(input("Digite sua nota: "))

if (nota >= 80):
    print("Parabéns.")
elif (nota < 80 and nota > 60):
    print("Pode melhorar.")
elif(nota > 60):
    print("Recuperação")