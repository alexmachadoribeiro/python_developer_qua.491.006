import pyautogui as auto

def tirar_credenciais():
    auto.write(f"git config --global --unset-all user.name")
    auto.press("enter")
    auto.write(f"git config --global --unset-all user.email")
    auto.press("enter")

def main():
    auto.PAUSE = 0.5

    usuario = input("Informe o user.name: ").strip().lower()
    email = input("Informe o user.email: ").strip().lower()
    commit = input("Informe a frase de commit: ")

    tirar_credenciais()

    auto.write('cd..')
    auto.press("enter")
    auto.write(f'git config --global user.name "{usuario}"')
    auto.press("enter")
    auto.write(f'git config --global user.email "{email}"')
    auto.press("enter")
    auto.write("git add .")
    auto.press("enter")
    auto.write(f'git commit -m "{commit}"')
    auto.press("enter")
    auto.write("git push")
    auto.press("enter")

    tirar_credenciais()

if __name__ == "__main__":
    main()