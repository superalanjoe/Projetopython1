from servicos import obter_contas, atualizar_contas
from funcionalidades.utilidades import solicitar_tipo, solicitar_status

def executar(id_conta):
    contas = obter_contas.executar()
    posicao_encontrada = None

    for posicao, conta in enumerate(contas):
        if conta.get("id") == id_conta:
            posicao_encontrada = posicao
            break
    
    if posicao_encontrada is None:
        print(f"Nenhuma conta encontrada com esse ID {id_conta}")
        return
    
    print("\n-- Conta encontrada --")
    print("(prescione 'enter' para manter o valor atual)")
    for chave, valor in contas[posicao_encontrada].items():
        if chave == "id":
            continue

        novo_valor = ""
        mensagem = f"{chave} (atual: {valor})"

        if chave == "tipo":
            novo_valor = solicitar_tipo.executar(mensagem, aceita_vazio=True)
        elif chave == "status":
            novo_valor = solicitar_status.executar(mensagem, aceita_vazio=True)
        else:
            novo_valor = input(mensagem + ": ")
        
        contas[posicao_encontrada][chave] = novo_valor if len(novo_valor) > 0 else valor

    foi_atualizado = atualizar_contas.executar(contas)
    if foi_atualizado:
        print("Conta atualizada com sucesso")
        return
    
    print("Não foi possível atualizar a conta")