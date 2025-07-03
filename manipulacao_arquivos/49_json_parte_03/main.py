import json

try:
    # usuário informa o arquivo
    arquivo = input("Informe o arquivo: ").strip().lower()

    # lê json e desserializa para dicionário
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        lista = json.load(f)
    
    # aplica as conversões
    for dado in lista:
        dado['altura'] = dado['altura'].replace(",", ".")
        dado['altura'] = float(dado['altura'])
        dado['peso'] = float(dado['peso'])
    
    # serializa o dicionário em json e grava o arquivo
    with open(f"{arquivo}.json", "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)
    
    # confirmação
    print("Conversão gravada com sucesso.")
except Exception as e:
    print(f"Não foi possível converter. {e}.")