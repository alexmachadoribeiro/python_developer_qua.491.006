# dicionário
usuario = {
    'nome': "Alex Machado",
    'idade': 40,
    'email': "alex@gmail.com",
    'profissão': "programador"
}

# exibe os valores
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")