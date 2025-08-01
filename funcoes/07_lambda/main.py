import os

# funções lambda
somar = lambda x, y: x+y
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

# algoritmo principal
if __name__ == "__main__":
    try:
        x = int(input("Informe o valor de x: "))
        y = int(input("Informe o valor de y: "))
        result = somar(x, y)

        limpar()
        print(f"O resultado da soma é {result}.")
    except Exception as e:
        print(f"Não foi possível somar. {e}.")