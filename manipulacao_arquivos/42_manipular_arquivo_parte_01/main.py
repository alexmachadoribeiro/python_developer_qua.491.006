# leitura de arquivo
with open("texto.txt", "r", encoding="utf-8") as f:
    texto = f.read()

# saída de dados
print(texto)