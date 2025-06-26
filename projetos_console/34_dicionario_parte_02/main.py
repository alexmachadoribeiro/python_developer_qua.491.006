# dicionário
pessoa = {
    'nome': "Fulano de Tal",
    'idade': 18,
    'email': "fulano@gmail.com",
    'profissão': "DBA"
}

# exibe os valores
print(f"Nome: {pessoa.get('nome')}")
print(f"Idade: {pessoa.get('idade')}")
print(f"E-mail: {pessoa.get('email')}")
print(f"Profissão: {pessoa.get('profissão')}")
print(f"Gênero: {pessoa.get('gênero')}")