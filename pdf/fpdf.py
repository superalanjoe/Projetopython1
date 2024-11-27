from fpdf import fpdf

class MeuPDF:
    def __init__(self, titulo="Documento"):
        """
        Inicializa a classe com um título opcional.
        """
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
        self.titulo = titulo
        self.adicionar_titulo()

    def adicionar_titulo(self):
        """
        Adiciona o título no topo do documento.
        """
        self.pdf.set_font("Arial", style="B", size=16)
        self.pdf.cell(200, 10, txt=self.titulo, ln=True, align="C")
        self.pdf.ln(10)

    def adicionar_texto(self, texto):
        """
        Adiciona um texto ao PDF.
        """
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, texto)

    def adicionar_linha(self, texto=""):
        """
        Adiciona uma linha de texto.
        """
        self.pdf.cell(0, 10, txt=texto, ln=True)

    def adicionar_tabela(self, dados, colunas_largura):
        """
        Adiciona uma tabela ao PDF.
        :param dados: Lista de listas com os dados da tabela.
        :param colunas_largura: Lista de larguras das colunas.
        """
        self.pdf.set_font("Arial", size=12)
        for linha in dados:
            for i, item in enumerate(linha):
                self.pdf.cell(colunas_largura[i], 10, str(item), border=1)
            self.pdf.ln(10)

    def salvar_pdf(self, nome_arquivo):
        """
        Salva o PDF no arquivo especificado.
        """
        self.pdf.output(nome_arquivo)
        print(f"PDF salvo como {nome_arquivo}")