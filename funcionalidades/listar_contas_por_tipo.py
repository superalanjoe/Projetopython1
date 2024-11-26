from servicos import obter_contas


def executar(tipo):
    contas = obter_contas.executar()

    if tipo != "todos":
        contas = [conta for conta in contas if conta.get("tipo", "") == tipo]


    for conta in contas:
        print("\n ------- // ------")
        for chave, valor in conta.items():
            print(f"{chave}: {"(vazio)" if len(valor) == 0 else valor}")