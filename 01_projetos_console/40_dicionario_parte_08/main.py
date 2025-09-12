chaves = ("Nome", "Idade", "E-mail", "Telefone", "Profissão")
usuario = {
    chaves[0]: "Alex Machado",
    chaves[1]: 40,
    chaves[2]: "alex@gmail.com",
    chaves[3]: "(61) 98765-4321",
    chaves[4]: "programador"
}

for chave in chaves:
    print(f"{chave}: {usuario.get(chave)}")