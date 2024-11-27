from funcionalidades import deletar_conta 

def executar():
    id_conta = input("Informe o ID da conta (somente números): ")

    if not(id_conta.isnumeric()):
        print("ID inválido")
        return
    
    deletar_conta.executar(id_conta=id_conta)