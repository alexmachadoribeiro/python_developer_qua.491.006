import os
import calendar as c

try:
    while True:
        ano = int(input("Informe o ano: "))
        os.system("cls" if os.name == "nt" else "clear")
        if ano >= 1900:
            print(c.calendar(ano))
            while True:
                voltar = input("Deseja imprimir outro calendário? (s/n)").lower().strip()
                if voltar == "s" or voltar == "n":
                    break
                else:
                    print("Opção inválida.")
                    continue
            match voltar:
                case "s":
                    continue
                case "n":
                    break
        else:
            print("Calendário do ano não disponível.")
except Exception as e:
    print(f"Não foi possível imprimir o calendário. {e}")
"""
# TODO - atividade: Crie um programa em que o usuário informa um ano e o programa exibe todo o calendário do ano informado pelo usuário.
# NOTE - o usuário poderá informar qualquer ano a partir de 1900.
# NOTE - use a biblioteca 'calendar'
"""