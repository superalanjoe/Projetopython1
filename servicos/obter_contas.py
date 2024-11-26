def executar():
    contas = []

    try:
        with open("dados/contas.csv", "r", encoding="utf8") as arquivo:
            linha_atual = 0
            for linha in arquivo:
                if linha_atual == 0:
                    linha_atual += 1
                else:
                    valores = linha.split(",")
                    conta = {
                        "id": valores[0].strip(),
                        "descricao": valores[1].strip(),
                        "valor": valores[2].strip(),
                        "tipo": valores[3].strip(),
                        "data_vencimento": valores[4].strip(),
                        "data_pagamento": valores[5].strip(),
                        "categoria": valores[6].strip(),
                        "status": valores[7].strip(),
                    }
                    contas.append(conta)
    except FileNotFoundError:
        print("Arquivo dados/contas.csv não encontrado")
    except Exception as erro:
        print("Ocorreu um erro desconhecido", erro)

    return contas