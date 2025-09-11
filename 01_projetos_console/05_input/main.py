# entrada de dados
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura em metros: ").replace(",", "."))

# saída de dados
print(f"Seja bem vindo ao curso de Python, {nome}!")
print(f"Idade do usuário: {idade}.")
print(f"Altura do usuário: {altura}.")

# verifica tipo de dados
print(f"{nome}: {type(nome)}.")
print(f"{idade}: {type(idade)}.")
print(f"{altura}: {type(altura)}.")