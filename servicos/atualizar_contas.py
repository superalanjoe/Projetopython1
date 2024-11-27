def executar(novas_contas):
    linhas = []
    for conta in novas_contas:
        linha = "\n" + ",".join(
            [
                conta["id"],
                conta["descricao"],
                conta["valor"],
                conta["tipo"],
                conta["data_vencimento"],
                conta["data_pagamento"],
                conta["categoria"],
                conta["status"],
            ]
        )
        linhas.append(linha)
    
    primeira_linha = "id, descricao, valor, tipo, data vencimento, data pagamento, categoria, status"
    linhas.insert(0, primeira_linha)

    try:
        with open("dados/contas.csv", "w", encoding="utf8") as arquivo:
            arquivo.writelines(linhas)
        return True
    except Exception as erro:
        print("Ocorreu um erro desconhecido ao tentar atualizar os dados", erro)
        return False