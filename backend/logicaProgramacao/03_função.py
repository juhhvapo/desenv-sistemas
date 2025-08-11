#Criar função de menu de opções e pedir a opção desejada do usuário
#Criar função de depósito
#Criar função de saque
#Criar função de ver saldo
#Ao digitar "sair" encerrar o programa

saldo = 0  # saldo inicial

def deposito():
    global saldo
    valor = float(input("Digite o valor para depósito: R$"))
    if valor > 0:
        saldo += valor
        print("Depósito realizado com sucesso.")
    else:
        print("Valor inválido.")

def saque():
    valor = float(input("Digite o valor para saque: R$"))
    if valor > 0 and valor <= saldo:
        saldo -= valor
        print("Saque realizado com sucesso.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        print("Valor inválido.")

while True:
    print("Menu:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Ver Saldo")
    print("Digite 'sair' para encerrar.")

    opçao = input("Escolha uma opção: ")