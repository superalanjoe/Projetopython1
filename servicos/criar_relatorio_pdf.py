from jinja2 import Environment, FileSystemLoader
import pdfkit
from datetime import datetime

configuracao = pdfkit.configuration(
    wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
)

def executar(dados, nome_arquivo):
    try:
        ambiente = Environment(loader=FileSystemLoader("templates"))
        
        template = ambiente.get_template("relatorio.html")
        html_renderizado = template.render(dados)

        agora = datetime.now()

        # Corrigido uso de aspas simples para a f-string
        caminho_pdf = f"relatorios/{nome_arquivo}_{agora.strftime('%d%m%Y%H%M%S')}.pdf"
        pdfkit.from_string(
            input=html_renderizado, 
            output_path=caminho_pdf, 
            configuration=configuracao
        )
        return caminho_pdf
    except Exception as erro:
        print("Ocorreu um erro ao tentar criar o PDF", erro)
        return ""