from funcionalidades.utilidades import solicitar_tipo, validar_data, solicitar_status
from servicos import obter_proximo_id_conta, salvar_conta

def executar():
    print("**Informe os dados abaixo **")

    descricao = input("Qual é a descrição? ")
    valor = input("Qual é o valor? ")
    tipo = solicitar_tipo.executar("Qual é o tipo? (d = débito, c = crédito) ")
    categoria = input("Qual é a categoria? ")
    data_vencimento = validar_data.executar(input("Qual é a data de vencimento? (DD/MM/YYYY) "))
    data_pagamento = validar_data.executar(input("Qual é a data de pagamento? (DD/MM/YYYY) "))
    status = solicitar_status.executar()

    nova_conta = {
        "id": obter_proximo_id_conta.executar(),
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo,
        "categoria": categoria,
        "data_vencimento": data_vencimento,
        "data_pagamento": data_pagamento,
        "status": status,
    }

    foi_persistido = salvar_conta.executar(nova_conta)

    if foi_persistido:
        print("Nova conta salva com sucesso")
    else:
        print("Não foi possível salvar a conta")