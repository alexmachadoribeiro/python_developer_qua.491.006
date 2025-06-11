# declaração de variáveis
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

# ternário
result = "é maior de idade." if idade >= 18 else "é menor de idade."

# saída
print(f"{nome} {result}")