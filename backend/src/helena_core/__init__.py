


# backend/src/helena_core/__init__.py
from .data_loader import (
    process_image,
    extract_data_from_pdf,
    validate_data,
    convert_to_float
)
__all__ = [
    'process_image',
    'extract_data_from_pdf',
    'validate_data',
    'convert_to_float'
]


from typing import Dict, List
#
from .data_loader import process_image, preprocess_pdf

__all__ = ['process_image', 'preprocess_pdf']
class CognitiveCore:
    """
    Núcleo Cognitivo da IA Helena.
    Processa dados e gera diagnósticos e sugestões.
    """

    def __init__(self):
        self.memory = []  # Memória de erros e improvisos

    def analyze(self, data: Dict) -> Dict:
        """
        Analisa os dados fornecidos.
        Args:
            data (Dict): Dados extraídos de uma planta ou obra.
        Returns:
            Dict: Diagnóstico e sugestões.
        """
        analise = self._analyze(data)
        self._store(analise)
        sugestoes = self._suggest()
        return {
            "diagnóstico": analise,
            "sugestões": sugestoes
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
        sugestões = []

        if any("Corredor fora" in erro for erro in self.memory):
            sugestões.append("Recomenda-se largura mínima de 1.20m para corredores.")

        if any("Altura da porta" in erro for erro in self.memory):
            sugestões.append("Portas devem ter altura mínima de 2.10m.")

        if any("saída de emergência" in erro for erro in self.memory):
            sugestões.append("Adicionar saída de emergência conforme norma NR-23.")

        return list(set(sugestões))