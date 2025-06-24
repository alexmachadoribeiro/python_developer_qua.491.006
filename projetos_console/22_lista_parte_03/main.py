# lista
cidades = [
    "Brasília",
    "São Paulo",
    "Rio de Janeiro",
    "Teresina",
    "Belo Horizonte",
    "Palmas"
]

# exibe a lista e seus respectivos índices
for i in range(len(cidades)):
    print(f"Índice {i}: {cidades[i]}.")

# tratamento de exceção
try:
    # usuário informa o nome da nova cidade e a posição
    nova_cidade = input("Informe o nome da nova cidade: ").title().strip()
    i = int(input("Informe a posição da lista onde deseja inserir: "))

    if i >= 0 and i <= len(cidades):
        # insere novo item em uma posição na lista
        cidades.insert(i, nova_cidade)
        print("Cidade inserida com sucesso!")
    else:
        print("Índice inválido.")
except Exception as e:
    print(f"Não foi possível inserir item na lista. {e}.")
finally:
    # re-exibe a lista e suas posições
    for i in range(len(cidades)):
        print(f"Índice {i}: {cidades[i]}.")