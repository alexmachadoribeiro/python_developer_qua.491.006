# lista
nomes = [
    "Alex",
    "Joana",
    "João",
    "Mariana",
    "Mário",
    "Fernanda"
]

# exibe a lista
for nome in nomes:
    print(nome)

# usuário informa nome a ser acrescetado na lista
novo_nome = input("Informe o novo nome: ").title().strip()

# novo nome é inserido na lista
nomes.append(novo_nome)

# re-exibe a lista
for nome in nomes:
    print(nome)