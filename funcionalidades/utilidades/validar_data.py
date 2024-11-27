from datetime import datetime
def executar(data):
    if len(data) == 0:
        return datetime.today().strftime("%d/%m/%Y")
    return data