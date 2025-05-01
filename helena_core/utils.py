# filepath: /home/sea/WssAi-Framework/helena_core/utils.py
import json
from typing import Dict

def load_additional_data(file_path: str) -> Dict:
    """
    Carrega dados adicionais de um arquivo JSON.
    Args:
        file_path (str): Caminho para o arquivo JSON.
    Returns:
        dict: Dados carregados do arquivo.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Erro ao decodificar JSON no arquivo: {file_path}")