from servicos import obter_contas, criar_relatorio_pdf

meses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
]

def executar(mes):
    # Validação do mês
    if not mes.isdigit() or int(mes) < 1 or int(mes) > 12:
        print("Erro: O mês informado é inválido. Insira um valor entre 1 e 12.")
        return

    mes_texto = meses[int(mes) - 1]
    print(f"** Gerando relatório do mês {mes_texto} **")

    # Obtendo as contas
    contas = obter_contas.executar()
    dados_relatorio = {
        'titulo': f'Relatório do mês {mes_texto}',
        'valor_total_credito': 0.0,
        'valor_total_debito': 0.0,
        'quantidade_pago': 0,
        'quantidade_cancelado': 0,
        'quantidade_pendente': 0,
        'valor_total': 0.0,
        'contas': []
    }

    for conta in contas:
        data_vencimento = conta.get("data_vencimento", "")
        if not data_vencimento:
            continue

        # Extraindo o mês de vencimento
        data_vencimento_lista = data_vencimento.split("/")
        if len(data_vencimento_lista) < 2:
            continue
        
        mes_vencimento = data_vencimento_lista[1]

        if mes_vencimento == mes:
            valor = float(conta.get("valor", 0))
            conta.update({"valor": "R$ {:.2f}".format(valor)})
            dados_relatorio['contas'].append(conta)

            # Acumulando os valores
            if conta.get("tipo") == "crédito":
                dados_relatorio['valor_total_credito'] += valor
            else:
                dados_relatorio['valor_total_debito'] += valor
            
            # Contabilizando os status
            status = conta.get("status", "").lower()
            if status == "pago":
                dados_relatorio['quantidade_pago'] += 1
            elif status == "pendente":
                dados_relatorio['quantidade_pendente'] += 1
            elif status == "cancelado":
                dados_relatorio['quantidade_cancelado'] += 1

    # Verificando se existem contas
    if not dados_relatorio['contas']:
        print(f"Nenhuma conta encontrada para o mês de {mes_texto}.")
        return

    # Calculando o total
    total = dados_relatorio['valor_total_credito'] - dados_relatorio['valor_total_debito']
    dados_relatorio.update({
        "valor_total": "R$ {:.2f}".format(total),
        "valor_total_credito": "R$ {:.2f}".format(dados_relatorio['valor_total_credito']),
        "valor_total_debito": "R$ {:.2f}".format(dados_relatorio['valor_total_debito']),
    })

    # Gerando o relatório em PDF
    nome_arquivo_criado = criar_relatorio_pdf.executar(
        dados=dados_relatorio,
        nome_arquivo=f"relatorio_de_{mes_texto}"
    )

    # Mensagem de sucesso ou erro
    if nome_arquivo_criado:
        print(f"O arquivo {nome_arquivo_criado} foi gerado com sucesso.")
    else:
        print("Não foi possível gerar o arquivo.")