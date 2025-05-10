import pdfplumber
import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
# tests/test_data_loader.py
from helena_core.data_loader import (
    convert_to_float,
    validate_data,
    process_image,
    preprocess_pdf,
    extract_data_from_pdf,
    DataLoaderError
)

class TestConvertToFloat(unittest.TestCase):
    def test_convert_valid_numbers(self):
        self.assertEqual(convert_to_float("1,5"), 1.5)
        self.assertEqual(convert_to_float("1.500,75"), 1500.75)
        self.assertEqual(convert_to_float("2.5"), 2.5)

class TestValidateData(unittest.TestCase):
    def test_valid_data(self):
        data = {
            "corridor_width": 1.5,
            "door_height": 2.1,
            "emergency_exit": True
        }
        self.assertTrue(validate_data(data))

class TestProcessImage(unittest.TestCase):
    @patch("PIL.Image.open")
    @patch("pytesseract.image_to_string")
    def test_success(self, mock_ocr, mock_open):
        mock_ocr.return_value = "texto extraído"
        result = process_image("dummy.jpg")
        self.assertEqual(result, "texto extraído")

class TestPreprocessPDF(unittest.TestCase):
    @patch("pdfplumber.open")
    def test_with_ocr_fallback(self, mock_pdf):
        mock_page = MagicMock()
        mock_page.extract_text.side_effect = ["texto", None]
        mock_pdf.return_value.__enter__.return_value.pages = [mock_page, mock_page]
        
        with patch("pytesseract.image_to_string", return_value="ocr text"):
            result = preprocess_pdf("dummy.pdf")
            self.assertIn("ocr text", result)

class TestExtractDataFromPDF(unittest.TestCase):
    @patch("backend.src.helena_core.data_loader.preprocess_pdf")
    def test_extraction(self, mock_preprocess):
        mock_preprocess.return_value = """
            Largura do corredor: 1,5m
            Altura da porta: 2.1m
            Saída de emergência: Sim
        """
        result = extract_data_from_pdf("dummy.pdf")
        self.assertEqual(result["corridor_width"], 1.5)
        self.assertTrue(result["emergency_exit"])

if __name__ == "__main__":
    unittest.main()
def test_pdfplumber():
    try:
        # Atualize o caminho para o arquivo PDF correto
        with pdfplumber.open("/home/sea/WssAi-Framework/dataset/plantas_digitalizadas/Ficha_Tecnica_Acesso_Seguranca.pdf") as pdf:
            for page in pdf.pages:
                print(page.extract_text())
    except FileNotFoundError:
        print("Arquivo PDF não encontrado.")
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")

# Executa o teste
test_pdfplumber()