import json
from helena_core.normas_checker import verificar_execucao_drywall # type: ignore

DATASET_PATH = "dataset/light_construction_dataset.json"

def rodar_demo():
    try:
        with open(DATASET_PATH, "r") as f:
            projetos = json.load(f)
    except Exception as e:
        print(f"Erro ao carregar dataset: {e}")
        return

    print("\n=== DEMONSTRAÇÃO PÚBLICA — IA HELENA / WssAi-Framework ===\n")

    for idx, projeto in enumerate(projetos, start=1):
        print(f"\n🔹 PROJETO {idx}: {projeto['nome']}")
        print(f"📌 DESCRIÇÃO: {projeto['descricao']}\n")

        # Apresenta problemas listados (input humano ou IA)
        if projeto.get("problemas_identificados"):
            print("🚨 PROBLEMAS DETECTADOS:")
            for p in projeto["problemas_identificados"]:
                print(f"  - {p}")
        else:
            print("✅ Nenhum problema informado diretamente.")

        # IA Helena avalia e gera recomendações técnicas
        print("\n🧠 RECOMENDAÇÕES DA IA HELENA:")
        try:
            recomendacoes = verificar_execucao_drywall(projeto)
            for rec in recomendacoes:
                print(f"  - {rec}")
        except Exception as e:
            print(f"⚠️ Erro ao gerar recomendações técnicas: {e}")

        print("\n" + "-" * 60)

if __name__ == "__main__":
    rodar_demo()
