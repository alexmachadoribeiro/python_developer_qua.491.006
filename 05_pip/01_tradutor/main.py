from deep_translator import GoogleTranslator
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    tradutor = GoogleTranslator(source="auto", target="pt")

    while True:
        try:
            print("1 - Traduzir texto.")
            print("2 - Sair do programa.")
            opcao = input("Informe a opção desejada: ").strip()
            limpar()
            match opcao:
                case "1":
                    texto_original = input("Digite o texto a ser traduzido: ")
                    texto_traduzido = tradutor.translate(texto_original)
                    print(f"Texto traduzido:\n{texto_traduzido}")
                case "2":
                    print("Programa encerrado.")
                    break
                case _:
                    print("Opção inválida.")
                    continue
        except Exception as e:
            print(f"Não foi possível traduzir. {e}.")
            continue

if __name__ == "__main__":
    main()