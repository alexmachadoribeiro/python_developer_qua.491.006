# importa biblioteca
import math as m

# exibe o número do pi
print(f"Número do pi: {m.pi}.")

# raíz quadrada
try:
    n = int(input("Informe um número inteiro: "))
    print(f"A raíz quadrada de {n} é {m.sqrt(n):.2f}.")
except Exception as e:
    print(f"Não foi possível calcular a raíz quadrada. {e}.")