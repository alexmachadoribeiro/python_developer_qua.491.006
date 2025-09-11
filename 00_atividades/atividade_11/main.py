# função recursiva que calcula Fibonacci
def calcular_fibonacci(n):
    return n if n <= 1 else calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

# programa principal
n = int(input('Informe o número de sequências a ser calculada: '))
print(calcular_fibonacci(n))

"""
# TODO - atividade: crie um programa que receba do usuário um número inteiro e o programa calcula o valor da sequência de Fibonacci.
"""