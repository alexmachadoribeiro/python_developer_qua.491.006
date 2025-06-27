# dicionário
usuario = {
    'nome': "Alex Machado",
    'idade': 40,
    'email': "alex@gmail.com",
    'profissão': "programador"
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
print("-"*40)

# usuário informa a chave que deseja alterar
chave = input("Informe a chave que deseja alterar: ").lower().strip()

# usuário informa o valor da chave
if chave in usuario:
    usuario[chave] = input(f"Informe o novo valor de {chave}: ").strip()
else:
    print("Chave inexistente.")

print("-"*40)
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")