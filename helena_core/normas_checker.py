# helena_core/normas_checker.py

# arquivo: extract_forro_data.py
import pdfplumber

def extrair_dados_planta(pdf_path: str) -> str:
    """
    Extrai o texto completo do PDF da planta de forro de drywall.
    
    Parâmetros:
        pdf_path (str): Caminho para o arquivo PDF.
        
    Retorna:
        str: Texto extraído do PDF.
    """
    texto_completo = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for pagina in pdf.pages:
                texto_pagina = pagina.extract_text() or ""
                texto_completo += texto_pagina + "\n"
    except Exception as e:
        print(f"[ERROR] Falha ao processar o PDF: {e}")
    return texto_completo

# Exemplo de uso
if __name__ == "__main__":
    caminho_pdf = "caminho/para/sua/planta_forro_drywall.pdf"
    dados = extrair_dados_planta(caminho_pdf)
    print("Dados extraídos da planta:")
    print(dados)


def verificar_execucao_drywall(projeto):
    """
    Valida tecnicamente uma execução de drywall com base em padrões técnicos e práticas de campo.
    :param projeto: dicionário com campos 'problemas_detectados' e 'itens'
    :return: lista de recomendações técnicas
    """
    relatorio = []

    if "sem reforço para armário" in projeto.get("problemas_detectados", []):
        relatorio.append("Adicionar madeira entre montantes a cada 40cm para carga suspensa.")

    if "fora de esquadro" in " ".join(projeto.get("problemas_detectados", [])):
        relatorio.append("Corrigir esquadro com cunha técnica ou ajuste da guia base.")

    if not relatorio:
        relatorio.append("Execução conforme normas detectadas.")

    return relatorio


# Exemplo de teste rápido (execução direta do arquivo)
if __name__ == "__main__":
    exemplo_projeto = {
        "problemas_detectados": [
            "sem reforço para armário",
            "fora de esquadro no eixo leste"
        ],
        "itens": ["montante", "guia", "placa ST"]
    }

    resultado = verificar_execucao_drywall(exemplo_projeto)
    print("\nRelatório Técnico da IA Helena:")
    for linha in resultado:
        print(f"- {linha}")
