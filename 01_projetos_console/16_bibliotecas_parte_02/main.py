# importa bibliotecas
import os
import time

try:
    n = int(input("Informe um número inteiro: "))
    while n >= 0:
        os.system("cls")
        print(f"{n}...")
        time.sleep(1)
        n -= 1

except Exception as e:
    print(f"Não foi possível executar a contagem. {e}.")
finally:
    os.system("cls")
    print("BOOOMMMMM!!!!!!")