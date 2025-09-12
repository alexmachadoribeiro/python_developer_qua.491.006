# função
def mostrar_msg(nome):
    return f"Seja bem vindo, {nome}!"

# programa principal
nome = input("Informe o seu nome: ").strip().title()
print(mostrar_msg(nome))