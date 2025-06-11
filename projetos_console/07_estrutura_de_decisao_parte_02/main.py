# declaração de variáveis
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura em metros: ").replace(",", "."))

# estrutura de decisão
if idade >= 12 and altura >= 1.15:
    print(f"{nome} está autorizado a entrar.")
else:
    print(f"{nome} não foi autorizado a entrar.")