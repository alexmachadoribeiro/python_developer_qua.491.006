import ContaCorrente as cc

# função main
def main():
    # instancia do objeto
    conta = cc.ContaCorrente(
        nome="", cpf="", email="", profissao="", telefone="", endereco="", salario=0.0, agencia="", numero="", saldo=0.0
    )

    conta.exibir_dados()

# impede a importação
if __name__ == "__main__":
    main()