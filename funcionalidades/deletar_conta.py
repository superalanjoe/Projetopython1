from servicos import obter_contas, atualizar_contas

def executar(id_conta):
    contas = obter_contas.executar()
    conta_encontrada = None

    for conta in contas:
        if conta.get("id") == id_conta:
            conta_encontrada = conta

    if conta_encontrada is None:
        print(f"Nenhuma conta foi encontrada com o ID {id_conta}")
        return

    print("\n-- Conta Encontrada --")
    for chave, valor in conta_encontrada.items():
        print(f"{chave}: {"(vazio)" if len(valor) == 0 else valor}")

    escolha = input("\nDeseja excluir essa conta? (s/n): ")

    if escolha.lower() != "s":
        print("Operação cancelada")
        return
    
    contas_filtrada = [conta for conta in contas if conta.get("id") != id_conta]

    foi_deletado = atualizar_contas.executar(contas_filtrada)
    
    if foi_deletado:
        print("Conta excluída com sucesso")
    else:
        print("Conta não foi excluída")