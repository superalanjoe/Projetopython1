def executar(mensagem = "Qual é o status?"):
    status = ""
    while status not in ["pago", "pendente", "cancelado"]:
        entrada = input(f"{mensagem} (1 = pago, 2 = pendente, 3 = cancelado): ")

        if entrada == "1":
            status = "pago"
        elif entrada == "2":
            status = "pendente"
        elif entrada == "3":
            status = "cancelado"
        else:
            print("status inválido")
    
    return status