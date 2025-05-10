from typing import Dict, List
from helena_core.utils import load_additional_data
from helena_core.data_loader import extract_data_from_pdf

import sys
import os
import logging
import json

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CognitiveCore:
    """
    Núcleo Cognitivo da IA Helena.
    Analisa dados extraídos da planta e compara com normas técnicas.
    """

    def __init__(self):
        self.memory = []  # Memória de erros e improvisos

    def analyze_elements(self, planta_path: str) -> Dict:
        """
        Analisa elementos de uma planta (integração com data_loader).
        Args:
            planta_path (str): Caminho do PDF
        Returns:
            dict: Resultados da análise
        """
        if not os.path.exists(planta_path):
            logging.error(f"Arquivo não encontrado: {planta_path}")
            return {"erro": "Arquivo não encontrado."}

        logging.info(f"Iniciando análise para o arquivo: {planta_path}")

        # Extração de dados reais do PDF
        dados_extraidos = extract_data_from_pdf(planta_path)
        logging.info(f"Dados extraídos: {dados_extraidos}")

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

    def _load_norms(self) -> Dict:
        """
        Carrega normas técnicas de um arquivo JSON.
        Returns:
            dict: Normas carregadas
        """
        normas_path = os.path.join("data", "normas.json")
        try:
            with open(normas_path, "r") as file:
                normas = json.load(file)
                logging.info("Normas carregadas com sucesso.")
                return normas
        except FileNotFoundError:
            logging.error(f"Arquivo de normas não encontrado: {normas_path}")
            return {}
        except json.JSONDecodeError as e:
            logging.error(f"Erro ao carregar normas: {e}")
            return {}

    def _store(self, erros: List[str]) -> None:
        """
        Armazena erros na memória, garantindo unicidade.
        """
        for erro in erros:
            if erro not in self.memory:
                self.memory.append(erro)

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