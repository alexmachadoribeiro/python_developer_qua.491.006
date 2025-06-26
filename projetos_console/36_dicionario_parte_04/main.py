# dicionário
usuario = dict(
    nome="Alex Machado", 
    idade=40, 
    email="alex@gmail.com"
)

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")