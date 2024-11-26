import funcionalidades
import funcionalidades.listar_contas_por_tipo

opcao_tipo = {
    "1": "crédito",
    "2": "débito",
    "3": "todos"
}

def executar():
    """
        - solicitar o filtro
        - chamar a funcionalidade
    """
    tipo = obter_tipo()
    funcionalidades.listar_contas_por_tipo.executar(tipo=tipo)

def obter_tipo():
    escolha = ""
    while escolha not in opcao_tipo:
        print("1 - Somente contas tipo crédito")
        print("2 - Somente contas tipo débito")
        print("3 - Todas as contas")

        escolha = input("Digite uma opção: ")
        if escolha in opcao_tipo:
            return opcao_tipo[escolha]
        print("\nOpção inválida")