import os
from helena_core.data_loader import extract_data_from_pdf

def test_extract_data_from_valid_pdf():
    """
    Testa a extração de dados de um PDF válido.
    """
    pdf_path = os.path.join("dataset", "plantas_digitalizadas", "Ficha_Tecnica_Acesso_Seguranca.pdf")
    extracted_data = extract_data_from_pdf(pdf_path)
    
    # Verifique se os dados extraídos estão corretos
    assert extracted_data["corridor_width"] == 1.50
    assert extracted_data["door_height"] == 2.20
    assert extracted_data["emergency_exit"] is True

def test_extract_data_from_invalid_pdf():
    """
    Testa a extração de dados de um PDF inexistente.
    """
    pdf_path = os.path.join("dataset", "plantas_digitalizadas", "arquivo_inexistente.pdf")
    extracted_data = extract_data_from_pdf(pdf_path)
    
    # Verifique se os valores padrão são retornados
    assert extracted_data["corridor_width"] == 0.0
    assert extracted_data["door_height"] == 0.0
    assert extracted_data["emergency_exit"] is False