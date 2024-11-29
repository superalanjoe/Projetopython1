def executar(mensagem, aceita_vazio = False):
    tipo = ""
    while tipo not in ["débito", "crédito"]:
        entrada_usuario = input(mensagem).lower()

        if aceita_vazio and entrada_usuario == "":
            return ""

        if entrada_usuario == "d":
            tipo = "débito"
        elif entrada_usuario == "c":
            tipo = "crédito"
        else:
            print("Tipo inválido")

    return tipo