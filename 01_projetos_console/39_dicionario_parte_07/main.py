usuario = {
    'nome': "Alex Machado",
    'idade': 40,
    'email': "alex@gmail.com",
    'profissão': "programador"
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
print("-"*40)

# usuário informa a chave que deseja excluir
chave = input("Informe a chave que deseja excluir: ").lower().strip()

# verifica se a chave existe
if chave in usuario:
    # exclui a chave
    del usuario[chave]
else:
    print("Chave inexistente")

print("-"*40)
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")