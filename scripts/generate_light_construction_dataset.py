# scripts/generate_light_construction_dataset.py

import os
import json

# Caminho absoluto (ajustado para seu sistema)
dataset_path = "/home/sea/WssAi-Framework/dataset"
output_file = os.path.join(dataset_path, "light_construction_dataset.json")

# Cria o diretório /dataset se não existir
os.makedirs(dataset_path, exist_ok=True)

# Exemplo técnico real de drywall com erro e recomendação
exemplo = {
    "projeto": "Divisória de quarto em drywall 3x3m",
    "descricao": "Parede com placas ST, ausência de reforço para armário suspenso e fora de esquadro 2cm.",
    "itens": ["placa ST", "perfil montante", "parafuso PH", "guia", "cantoneira"],
    "problemas_detectados": ["sem reforço para armário", "fora de esquadro no eixo leste"],
    "recomendacoes": [
        "Inserir madeira 3x5cm entre montantes a cada 40cm",
        "Ajustar esquadro com cunha técnica no perfil guia"
    ],
    "tags": ["drywall", "quarto", "reforço estrutural", "execução incorreta"]
}

# Escreve o arquivo JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump([exemplo], f, ensure_ascii=False, indent=4)

print(f"Dataset salvo com sucesso em: {output_file}")
