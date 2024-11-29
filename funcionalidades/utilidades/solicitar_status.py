def executar(mensagem = "Qual é o status?", aceita_vazio = False):
    status = ""
    while status not in ["pago", "pendente", "cancelado"]:
        entrada = input(f"{mensagem} (1 = pago, 2 = pendente, 3 = cancelado): ")
        
        if aceita_vazio and entrada == "":
            return ""
        
        if entrada == "1":
            status = "pago"
        elif entrada == "2":
            status = "pendente"
        elif entrada == "3":
            status = "cancelado"
        else:
            print("status inválido")
    
    return status