import Pessoa

def main():
    usuario = Pessoa.Pessoa(nome="Alex", idade=40)

    print(usuario)
    print(f"Idade: {len(usuario)}")
    del(usuario)

if __name__ == "__main__":
    main()