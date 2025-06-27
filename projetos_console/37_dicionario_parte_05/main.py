# dicionário
usuario = {
    'nome': "Alex Machado",
    'idade': 40,
    'email': "alex@gmail.com"
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

# adicionando nova chave
usuario['profissão'] = input("Informe a profissão: ").strip()

print("-"*40)
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")