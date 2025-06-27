usuarios = [
    {
        'nome': "Fulano",
        'idade': 18,
        'email': "fulano@gmail.com"
    },
    {
        'nome': "Cicrano",
        'idade': 25,
        'email': "cicrano@gmail.com"
    },
    {
        'nome': "Beltrano",
        'idade': 30,
        'email': "beltrano@gmail.com"
    }
]

# exibe os dados
for usuario in usuarios:
    print("-"*40)
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario.get(chave)}")