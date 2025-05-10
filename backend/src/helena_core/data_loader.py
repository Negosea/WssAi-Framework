import logging
import re
from typing import Dict, Optional, Union
from pathlib import Path
import pdfplumber
import pytesseract
from PIL import Image, UnidentifiedImageError
from pdf2image import convert_from_path
from pdf2image.exceptions import PDFInfoNotInstalledError

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data_processing.log'),
        logging.StreamHandler()
    ]
)

class DataLoaderError(Exception):
    """Exceção customizada para erros no carregamento de dados"""
    pass

def convert_to_float(value: Union[str, float, int]) -> float:
    """
    Converte strings numéricas com formatos internacionais para float.
    
    Args:
        value: Valor a ser convertido (pode ser string com ',' ou '.', ou número)
    
    Returns:
        float: Valor convertido ou 0.0 em caso de falha
    
    Examples:
        >>> convert_to_float("1,500.75")
        1500.75
        >>> convert_to_float("1.500,75")
        1500.75
        >>> convert_to_foat("invalid")
        0.0
    """
    if isinstance(value, (int, float)):
        return float(value)
        
    try:
        # Remove caracteres não numéricos exceto , e .
        cleaned = re.sub(r"[^\d.,-]", "", str(value))
        if ',' in cleaned and '.' in cleaned:
            # Decide qual é o separador decimal baseado na posição
            if cleaned.rfind(',') > cleaned.rfind('.'):
                cleaned = cleaned.replace('.', '').replace(',', '.')
            else:
                cleaned = cleaned.replace(',', '')
        elif ',' in cleaned:
            cleaned = cleaned.replace(',', '.')
            
        return float(cleaned) if cleaned else 0.0
    except (ValueError, AttributeError):
        logging.warning(f"Falha na conversão de valor: '{value}'")
        return 0.0

def validate_data(data: Dict) -> bool:
    """
    Valida a estrutura e valores dos dados extraídos.
    
    Args:
        data: Dicionário com os dados a validar
    
    Returns:
        bool: True se os dados são válidos
    
    Raises:
        DataLoaderError: Se a estrutura dos dados é inválida
    """
    required_keys = {
        "corridor_width": (float, lambda x: x > 0),
        "door_height": (float, lambda x: x > 0),
        "emergency_exit": (bool, None)
    }
    
    missing = [key for key in required_keys if key not in data]
    if missing:
        raise DataLoaderError(f"Chaves obrigatórias faltantes: {missing}")
    
    for key, (type_, validator) in required_keys.items():
        if not isinstance(data[key], type_):
            raise DataLoaderError(f"Tipo inválido para {key}. Esperado: {type_}")
        if validator and not validator(data[key]):
            raise DataLoaderError(f"Valor inválido para {key}: {data[key]}")
    
    return True

def process_image(
    image_path: Union[str, Path],
    lang: str = "por",
    config: str = "--oem 3 --psm 6"
) -> str:
    """
    Processa imagem com OCR usando Tesseract.
    
    Args:
        image_path: Caminho para o arquivo de imagem
        lang: Idioma para OCR (padrão: 'por')
        config: Configuração do Tesseract
    
    Returns:
        str: Texto extraído
    
    Raises:
        DataLoaderError: Se o arquivo não puder ser processado
    """
    try:
        with Image.open(image_path) as img:
            return pytesseract.image_to_string(
                img,
                lang=lang,
                config=config
            ).strip()
    except (UnidentifiedImageError, pytesseract.TesseractError) as e:
        error_msg = f"Falha ao processar imagem {image_path}: {str(e)}"
        logging.error(error_msg)
        raise DataLoaderError(error_msg) from e

def preprocess_pdf(
    pdf_path: Union[str, Path],
    lang: str = "por",
    dpi: int = 300,
    apply_ocr: bool = True
) -> str:
    """
    Extrai texto de PDF com fallback para OCR quando necessário.
    
    Args:
        pdf_path: Caminho para o arquivo PDF
        lang: Idioma para OCR
        dpi: Resolução para conversão de imagem
        apply_ocr: Se False, ignora páginas sem texto extraível
    
    Returns:
        str: Texto concatenado de todas as páginas
    
    Raises:
        DataLoaderError: Se o PDF não puder ser processado
    """
    full_text = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                if text := page.extract_text():
                    full_text.append(text)
                elif apply_ocr:
                    try:
                        images = convert_from_path(
                            pdf_path,
                            first_page=page.page_number,
                            last_page=page.page_number,
                            dpi=dpi
                        )
                        full_text.extend(
                            pytesseract.image_to_string(img, lang=lang)
                            for img in images
                        )
                    except PDFInfoNotInstalledError as e:
                        raise DataLoaderError("Poppler não instalado") from e
    except Exception as e:
        error_msg = f"Falha ao processar PDF {pdf_path}: {str(e)}"
        logging.error(error_msg)
        raise DataLoaderError(error_msg) from e
    
    return "\n".join(full_text)

def extract_data_from_pdf(pdf_path: Union[str, Path]) -> Dict:
    """
    Extrai dados estruturados de um PDF.
    
    Args:
        pdf_path: Caminho para o arquivo PDF
    
    Returns:
        Dict: Dados extraídos no formato:
            {
                "corridor_width": float,
                "door_height": float,
                "emergency_exit": bool
            }
    
    Raises:
        DataLoaderError: Se a extração falhar
    """
    patterns = {
        "corridor_width": r"(?i)largura\D*(\d+[.,]?\d*)",
        "door_height": r"(?i)altura\D*(\d+[.,]?\d*)",
        "emergency_exit": r"(?i)emerg[êe]ncia:\s*(sim|n[ãa]o)"
    }
    
    try:
        text = preprocess_pdf(pdf_path)
        result = {
            "corridor_width": 0.0,
            "door_height": 0.0,
            "emergency_exit": False
        }
        
        # Extração com regex
        if width_match := re.search(patterns["corridor_width"], text):
            result["corridor_width"] = convert_to_float(width_match.group(1))
        
        if height_match := re.search(patterns["door_height"], text):
            result["door_height"] = convert_to_float(height_match.group(1))
        
        if exit_match := re.search(patterns["emergency_exit"], text):
            result["emergency_exit"] = exit_match.group(1).lower().startswith('s')
        
        validate_data(result)
        return result
        
    except Exception as e:
        error_msg = f"Falha na extração de dados: {str(e)}"
        logging.error(error_msg)
        raise DataLoaderError(error_msg) from e