from datetime import datetime


def executar():
    """
    - solicitar os dados
    - chamar funcionalidade criar_conta
    - utilizar o retorno (booleano) da funcionalidade
    """
    print("**Informe os dados abaixo **")

    descricao = input("Qual é a descrição? ")
    valor = input("Qual é o valor? ")
    tipo = solicitar_tipo("Qual é o tipo? (d = débito, c = crédito) ")
    categoria = input("Qual é a categoria? ")
    data_vencimento = validar_data(input("Qual é a data de vencimento? (DD/MM/YYYY) "))
    # data_pagamento = validar_data(input("Qual é a data de pagamento? (DD/MM/YYYY) "))

    nova_conta = {
        "id": "",
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo,
        "categoria": categoria,
        "data_vencimento": data_vencimento,
        "data_pagamento": "",
        "status": "Pendente",
    }

    print(nova_conta)


def validar_data(data):
    if len(data) == 0:
        return datetime.today().strftime("%d/%m/%Y")
    return data


def solicitar_tipo(mensagem):
    tipo = ""
    while tipo not in ["débito", "crédito"]:
        entrada_usuario = input(mensagem)
        if entrada_usuario == "d":
            tipo = "débito"
        elif entrada_usuario == "c":
            tipo = "crédito"
        else:
            print("Tipo inválido")

    return tipo