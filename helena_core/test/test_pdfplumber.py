import pdfplumber

def test_pdfplumber():
    """
    Testa a funcionalidade básica do pdfplumber para extrair texto de um PDF.
    """
    try:
        # Substitua "data/planta_exemplo.pdf" pelo caminho do seu PDF real
        with pdfplumber.open("data/planta_exemplo.pdf") as pdf:
            for page in pdf.pages:
                print(page.extract_text())
    except FileNotFoundError:
        print("Arquivo PDF não encontrado.")
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")

# Executa o teste
test_pdfplumber()