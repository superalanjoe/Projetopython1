def executar(nova_conta):
    try:
        with open("dados/contas.csv", "a", encoding="utf8") as arquivo:
            linha = "\n" + ",".join([
                nova_conta["id"],
                nova_conta["descricao"],
                nova_conta["valor"],
                nova_conta["tipo"],
                nova_conta["data_vencimento"],
                nova_conta["data_pagamento"],
                nova_conta["categoria"],
                nova_conta["status"],
            ])
            arquivo.write(linha)
        return True
    except Exception as erro:
        print("\n Erro: ", erro)
        return False