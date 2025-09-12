import os
import math as m

while True:
    # menu
    print(f"{'-'*20} MENU {'-'*20}\n")
    print("1 - Calcular área de um círculo")
    print("2 - Calcular tamanho de uma circunferência")
    print("3 - Sair do programa")
    opcao = input("Informe sua opção: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    try:
        if opcao == "1" or opcao == "2":
            raio = float(input("Informe o valor do raio: ").replace(",", "."))
        else:
            pass
        os.system("cls" if os.name == "nt" else "clear")
        match opcao:
            case "1":
                area = m.pi*raio**2
                print(f"Área do círculo: {area}.")
                continue
            case "2":
                circunferencia = 2*m.pi*raio
                print(f"Tamanho da circunferência: {circunferencia}.")
                continue
            case "3":
                print("Programa encerrado.")
                break
            case _:
                print(f"Opção inválida.")
                continue
    except Exception as e:
        print(f"Não foi possível calcular. {e}.")
        continue
"""
# TODO - atividade: Crie um programa que faça as seguintes operações:
- Calcular área de um círculo
- Calcular tamanho de uma circunferência
- Sair do programa
# NOTE - para cada loop, o programa deverá limpar o terminal
"""