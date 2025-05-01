from typing import Dict, List
from helena_core.utils import load_additional_data

import sys
import os

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class CognitiveCore:
    """
    Núcleo Cognitivo da IA Helena.
    Analisa dados extraídos da planta e compara com normas técnicas.
    """

    def __init__(self):
        self.memory = []  # Memória de erros e improvisos

    def analyze_elements(self, planta_path: str) -> Dict:
        """
        Analisa elementos de uma planta (simulação).
        Args:
            planta_path (str): Caminho do PDF (simulado por enquanto)
        Returns:
            dict: Resultados da análise
        """
        # Simulação de extração de dados da planta
        dados_extraidos = {
            "corridor_width": 1.00,
            "door_height": 2.00,
            "emergency_exit": False
        }

        resultado = self.process(dados_extraidos)
        return resultado

    def process(self, input_data: Dict) -> Dict:
        """
        Pipeline principal de análise cognitiva
        """
        analise = self._analyze(input_data)
        self._store(analise)
        sugestao = self._suggest()
        return {
            "diagnóstico": analise,
            "sugestão": sugestao
        }

    def _analyze(self, data: Dict) -> List[str]:
        erros = []

        if data.get("corridor_width", 0) < 1.20:
            erros.append("Corredor fora da norma: largura < 1.20m.")

        if data.get("door_height", 0) < 2.10:
            erros.append("Altura da porta abaixo do mínimo: < 2.10m.")

        if not data.get("emergency_exit", False):
            erros.append("Ausência de saída de emergência.")

        return erros

    def _store(self, erros: List[str]) -> None:
        if erros:
            self.memory.extend(erros)

    def _suggest(self) -> List[str]:
        """
        Gera sugestões com base nos erros armazenados na memória.

        Este método analisa as mensagens de erro armazenadas e fornece uma lista
        de sugestões para resolver os problemas identificados. As sugestões são
        deduplicadas antes de serem retornadas.

        Returns:
            List[str]: Lista de sugestões para resolver os erros identificados.
        """
        sugestões = []

        if any("Corredor fora" in erro for erro in self.memory):
            sugestões.append("Recomenda-se largura mínima de 1.20m para corredores.")

        if any("Altura da porta" in erro for erro in self.memory):
            sugestões.append("Portas devem ter altura mínima de 2.10m.")

        if any("saída de emergência" in erro for erro in self.memory):
            sugestões.append("Adicionar saída de emergência conforme norma NR-23.")

        # Remover duplicatas
        return list(set(sugestões))


if __name__ == "__main__":
    helena = CognitiveCore()  # type: ignore
    planta_exemplo = "data/planta_exemplo.pdf"  # Simulação de caminho para a planta
    resultado = helena.analyze_elements(planta_exemplo)

    print("Diagnóstico:")
    for item in resultado["diagnóstico"]:
        print("-", item)

    print("\nSugestões:")
    for item in resultado["sugestão"]:
        print("-", item)