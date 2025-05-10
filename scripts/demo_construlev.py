# arquivo: demo_construlev.py
import json
import os
from extract_forro_data import extrair_dados_planta # type: ignore

# Importe a função ou módulo do normas_checker
# Exemplo fictício:
# from normas_checker import verificar_execucao_drywall

def carregar_dataset(dataset_path: str) -> list:
    with open(dataset_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_dataset(dataset: list, dataset_path: str):
    with open(dataset_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=4)

def gerar_laudo(projeto: dict) -> str:
    # Exemplo de lógica utilizando normas_checker para "verificar_execucao_drywall"
    # Aqui assumimos que a função retorna um dicionário com problemas detectados e recomendações.
    # laudo = verificar_execucao_drywall(projeto)
    # Para a simulação, criaremos um laudo de exemplo:
    laudo = {
        "projeto": projeto.get("nome", "Projeto Desconhecido"),
        "descricao": projeto.get("descricao", "Sem descrição disponível"),
        "problemas_detectados": [
            "Ausência de pendural em vãos críticos",
            "Falta de espaçador entre perfis"
        ],
        "recomendacoes": [
            "Adicionar pendural a cada 1,20m para estabilidade",
            "Verificar espaçamento conforme NBR 15.575"
        ]
    }
    
    # Formatação do laudo para exibição
    laudo_formatado = (
        f"PROJETO: {laudo['projeto']}\n"
        f"DESCRIÇÃO: {laudo['descricao']}\n\n"
        "PROBLEMAS DETECTADOS:\n"
        + "\n".join(f"- {p}" for p in laudo["problemas_detectados"]) +
        "\n\nRECOMENDAÇÕES DA IA HELENA:\n"
        + "\n".join(f"- {r}" for r in laudo["recomendacoes"])
    )
    return laudo_formatado

def main():
    # Ajuste os caminhos conforme necessário:
    dataset_path = os.path.join("dataset", "light_construction_dataset.json")
    pdf_path = os.path.join("dataset", "planta_forro_drywall.pdf")  # Exemplo: pdf incluído no dataset

    # Etapa 1: Carregar o dataset
    projetos = carregar_dataset(dataset_path)
    
    # Etapa 2: Extrair dados da planta do forro (se disponível)
    print("Extraindo dados da planta de forro...")
    dados_planta = extrair_dados_planta(pdf_path)
    # Aqui você pode realizar análises específicas dos dados extraídos:
    # Exemplo: integrar informações à descrição do projeto
    if dados_planta:
        for projeto in projetos:
            # Se o projeto for relacionado a forro, adicione informações extraídas
            if "forro" in projeto.get("categoria", "").lower():
                projeto["dados_planta"] = dados_planta[:500]  # Exemplo: armazenando os primeiros 500 caracteres
    else:
        print("[WARNING] Dados da planta não foram extraídos.")

    # Etapa 3: Simular a verificação e gerar laudos para cada projeto
    for projeto in projetos:
        print("=============================================")
        print(gerar_laudo(projeto))
        print("=============================================\n")
    
    # Opcional: Salvar atualizações no dataset, se necessário
    # salvar_dataset(projetos, dataset_path)

if __name__ == "__main__":
    main()
