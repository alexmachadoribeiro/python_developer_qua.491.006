# lista
nomes = [
    "Alex",
    "Fernanda",
    "Alexandre",
    "José",
    "Maria",
    "João",
    "Renata",
    "Ricardo",
    "Jason",
    "Marta"
]

# exibe a lista
for i in range(len(nomes)):
    print(f"{i}: {nomes[i]}.")

# tratamento de exceção
try:
    i = int(input("Informe a posição do nome na lista: "))
    if i >= 0 and i < len(nomes):
        # exclui nome da lista
        del(nomes[i])
        print("Nome excluído com sucesso!")
    else:
        print("Posição inválida.")
except Exception as e:
    print(f"Não foi possível excluir o nome da lista. {e}.")
finally:
    for i in range(len(nomes)):
        print(f"{i}: {nomes[i]}.")