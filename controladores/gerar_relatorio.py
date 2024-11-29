from funcionalidades import gerar_relatorio
def executar():
    mes = input("Informe um mês entre 1 e 12: ")

    if not mes.isnumeric() or int(mes) < 1 or int(mes) > 12:
        print("Mês inválido\nOperação cancelada")
        return
    
    if len(mes) == 1:
        mes = "0" + mes 

    gerar_relatorio.executar(mes)