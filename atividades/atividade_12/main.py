import math
import os

area_circunferencia = lambda r: math.pi*r**2
comprimento_circunferencia = lambda r: 2*math.pi*r
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    try:
        r = float(input("Informe o valor do raio: ").replace(",", "."))
        a = area_circunferencia(r)
        comp = comprimento_circunferencia(r)

        limpar()
        print(f"Área da circunferência: {a:.2f}.")
        print(f"Comprimento da circunferência: {comp:.2f}.")
    except Exception as e:
        print(f"Não foi possível exibir os resultados. {e}.")

"""
# TODO - atividade: crie um programa que calcule a área e a circunferência de um círculo.
# NOTE - use lambda
"""