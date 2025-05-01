import pdfplumber

def test_pdfplumber():
    try:
        # Atualize o caminho para o arquivo PDF correto
        with pdfplumber.open("/home/sea/WssAi-Framework/dataset/plantas_digitalizadas/Ficha_Tecnica_Acesso_Seguranca.pdf") as pdf:
            for page in pdf.pages:
                print(page.extract_text())
    except FileNotFoundError:
        print("Arquivo PDF não encontrado.")
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")

# Executa o teste
test_pdfplumber()