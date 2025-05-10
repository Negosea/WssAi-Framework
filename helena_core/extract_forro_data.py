import pdfplumber
import re

def extrair_dados_forro(pdf_path):
    termos_relevantes = {
        "perfis": [],
        "pendurais": [],
        "vãos": [],
        "observações": []
    }

    # Exemplo de dados estruturados (caso queira processar ou armazenar)
    projeto_exemplo = {
        "projeto": "Divisória de quarto em drywall 3x3m",
        "descricao": "Parede com placas ST, ausência de reforço para armário suspenso e fora de esquadro 2cm.",
        "itens": [
            "placa ST",
            "perfil montante",
            "parafuso PH",
            "guia",
            "cantoneira"
        ],
        "problemas_detectados": [
            "sem reforço para armário",
            "fora de esquadro no eixo leste"
        ],
        "recomendacoes": [
            "Inserir madeira 3x5cm entre montantes a cada 40cm",
            "Ajustar esquadro com cunha técnica no perfil guia"
        ],
        "tags": [
            "drywall",
            "quarto",
            "reforço estrutural",
            "execução incorreta"
        ]
    }

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    texto = texto.lower()  # Normalizar para minúsculas
                    # Encontrar perfis
                    perfis = re.findall(r'\b(f530|guia|cantoneira|montante|perfil t|perfil)\b', texto)
                    termos_relevantes["perfis"].extend(perfis)
                    
                    # Verificar se há pendurais
                    if "pendural" in texto or "pendural" in texto:
                        termos_relevantes["pendurais"].append("detectado")

                    # Capturar vãos (dimensões)
                    vaos = re.findall(r'(\d{1,2},\d{1,2}\s?m|\d{3,4}\s?mm|\d+\s?cm)', texto)
                    termos_relevantes["vãos"].extend(vaos)

                    # Observações
                    if "reforço" in texto:
                        termos_relevantes["observações"].append("possível necessidade de reforço")
                    if "luminária" in texto:
                        termos_relevantes["observações"].append("possível ponto de carga luminosa")

    except Exception as e:
        print(f"Erro ao processar PDF: {e}")

    return termos_relevantes

if __name__ == "__main__":
    caminho_pdf = "dataset/planta_forro_drywall.pdf"  # Ajuste o caminho para o seu PDF
    dados = extrair_dados_forro(caminho_pdf)
    print("\n=== DADOS EXTRAÍDOS DA PLANTA DE FORRO ===")
    for chave, valores in dados.items():
        print(f"{chave.upper()}: {valores}")
