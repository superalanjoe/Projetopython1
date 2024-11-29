from funcionalidades import atualizar_conta

def executar():
    id_conta = input("Informe o ID da conta (somente números): ")

    # if id_conta.isnumeric() == False:
    if not id_conta.isnumeric():
        print("ID inválido")
        return
    atualizar_conta.executar(id_conta)