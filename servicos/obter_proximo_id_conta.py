from servicos import obter_contas

def executar():
    contas = obter_contas.executar()

    if len(contas) == 0:
        return '1'

    ultima_conta = contas[-1]
    proximo_id = int(ultima_conta.get("id", 0)) + 1
    return str(proximo_id)