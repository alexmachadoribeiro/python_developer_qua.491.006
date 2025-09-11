# lista
cidades = [
    "Brasília",
    "Goiânia",
    "Curitiba",
    "Florianópolis",
    "São Paulo",
    "Rio de Janeiro",
    "Brasília",
    "Teresina",
    "São Paulo",
    "Florianópolis",
    "Brasília"
]

# usuário informa o nome da cidade a ser pesquisada
cidade_pesquisada = input("Informe o nome da cidade: ").title().strip()

# programa conta quantas vezes ocorre o item pesquisado
qtde = cidades.count(cidade_pesquisada)

# programa indica quantas vezes o item foi encontrado
print(f"{cidade_pesquisada} foi encontrado {qtde} vezes na lista.")