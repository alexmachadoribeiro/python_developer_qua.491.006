import Pessoa

def main():
    usuario = Pessoa.Pessoa(nome="Alex", idade=40)

    print(usuario)
    print(f"Idade: {len(usuario)}")

    # destruição do objeto
    del(usuario)

    # print(usuario)

if __name__ == "__main__":
    main()