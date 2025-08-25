# Exemplo de uso do try/except em Python
# O try/except é usado para capturar e tratar exceções (erros) que possam ocorrer em um bloco de código.

# Explicação:
# - O bloco try contém o código que pode gerar um erro.
# - Se ocorrer um erro, o bloco except captura a exceção e permite que o programa continue a execução.
# - Podemos capturar exceções específicas ou uma exceção genérica (que captura todos os tipos de erro).

def exemplo_divisao(a, b):
    try:
        resultado = a / b  # Tenta realizar a divisão
    except ZeroDivisionError:  # Captura erro de divisão por zero
        return "Erro: Não é possível dividir por zero!"
    else:
        return resultado  # Retorna o resultado caso não haja erro

def exemplo_lista(lista, indice):
    try:
        return lista[indice]  # Tenta acessar um índice da lista
    except IndexError:  # Captura erro de índice fora do alcance da lista
        return "Erro: Índice fora do alcance da lista!"

def exemplo_int_convert(valor):
    try:
        return int(valor)  # Tenta converter uma string para inteiro
    except ValueError:  # Captura erro caso a conversão falhe
        return "Erro: Não foi possível converter para inteiro!"

# Exemplo 1: Divisão com try/except
print(exemplo_divisao(10, 2))  # Funciona normalmente
print(exemplo_divisao(10, 0))  # Gera erro de divisão por zero

# Exemplo 2: Acesso a elementos de uma lista com try/except
minha_lista = [1, 2, 3, 4, 5]
print(exemplo_lista(minha_lista, 2))  # Índice válido
print(exemplo_lista(minha_lista, 10))  # Índice fora do alcance

# Exemplo 3: Conversão de string para inteiro com try/except
print(exemplo_int_convert("123"))  # Conversão bem-sucedida
print(exemplo_int_convert("abc"))  # Gera erro de conversão
