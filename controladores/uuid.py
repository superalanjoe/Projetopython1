import uuid
from datetime import datetime

class UIID:
    @staticmethod
    def gerar_uuid4():
        """
        Gera um ID único utilizando o UUID versão 4.
        """
        return str(uuid.uuid4())

    @staticmethod
    def gerar_sequencial(base="ID"):
        """
        Gera um ID sequencial baseado na data e hora atual.
        Exemplo: ID_20241126_142530_123456
        """
        agora = datetime.now()
        return f"{base}_{agora.strftime('%Y%m%d_%H%M%S_%f')}"

    @staticmethod
    def gerar_curto():
        """
        Gera um ID único mais curto usando apenas parte de um UUID.
        """
        return str(uuid.uuid4()).split('-')[0]

    @staticmethod
    def gerar_customizado(prefixo="", sufixo=""):
        """
        Gera um ID customizado com prefixo e/ou sufixo.
        """
        id_base = str(uuid.uuid4())
        return f"{prefixo}{id_base}{sufixo}"


# Teste básico
if __name__ == "__main__":
    print("UUID4:", UIID.gerar_uuid4())
    print("Sequencial:", UIID.gerar_sequencial())
    print("Curto:", UIID.gerar_curto())
    print("Customizado:", UIID.gerar_customizado(prefixo="PRE_", sufixo="_SUF"))