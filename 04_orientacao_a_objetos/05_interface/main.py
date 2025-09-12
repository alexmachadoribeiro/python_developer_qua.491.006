import classes as c

def main():
    cc = c.ContaCorrente(
        titular="Fulano", 
        cpf="123.456.789-12", 
        agencia="1010-1", 
        conta="10101-1", 
        saldo=0.0
    )

    # NOTE: teste
    cc.consultar_dados()
    print(f"Saldo: R$ {cc.depositar(100)}")
    print(f"Saldo: R$ {cc.sacar(25)}")
    # TODO: continuem com a construção do programa

if __name__ == "__main__":
    main()