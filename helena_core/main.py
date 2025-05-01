from analyzer import analyze_elements
from norm_checker import check_norms
from learning_engine import learn_from_errors
from interpreter import interpret_plant

def main(planta):
    """    from helena_core.analyzer import CognitiveCore
    from helena_core.data_loader import extract_data_from_pdf
    
    if __name__ == "__main__":
        # Caminho do PDF
        pdf_path = "data/planta_exemplo.pdf"
    
        # Extrair dados do PDF
        dados = extract_data_from_pdf(pdf_path)
    
        # Analisar os dados
        helena = CognitiveCore()
        resultado = helena.analyze(dados)
    
        # Exibir resultados
        print("Diagnóstico:")
        for item in resultado["diagnóstico"]:
            print("-", item)
    
        print("\nSugestões:")
        for item in resultado["sugestões"]:
            print("-", item)
    Função principal para executar o fluxo de trabalho do sistema Helena.
    
    Args:
        planta (str): Caminho para o arquivo da planta.
    
    Returns:
        dict: Resultados da execução do fluxo de trabalho.
    """
    # Interpretar a planta
    interpretacao = interpret_plant(planta)
    
    # Analisar os elementos da planta
    analise = analyze_elements(planta)
    
    # Verificar conformidade com normas
    conformidade = check_norms(planta)
    
    # Aprender com erros reais
    erros = []  # Lista de erros identificados (exemplo)
    melhorias = learn_from_errors(erros)
    
    # Compilar resultados
    resultados = {
        "interpretacao": interpretacao,
        "analise": analise,
        "conformidade": conformidade,
        "melhorias": melhorias,
    }
    
    return resultados