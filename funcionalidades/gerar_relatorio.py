from servicos import obter_contas
def executar(mes):
    print(f"** Gerando relatório do mês {mes} **")

    contas = obter_contas.executar()
    dados_relatorio = {
        'valor_total_credito': 0,
        'valor_total_debito': 0,
        'quantidade_pago': 0,
        'quantidade_cancelado': 0,
        'quantidade_pendente': 0,
        'valor_total': 0,
        'contas_por_categoria': {

        },
    }

    