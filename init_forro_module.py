import os

# Diretórios a serem criados
directories = [
    "dataset/images_raw",
    "dataset/images_processed",
    "dataset/ocr_results",
    "dataset/label_maps",
    "dataset/training_data",
    "helena_core",
    "scripts"
]

# Arquivos a serem criados com conteúdo inicial
files = {
    "helena_core/ocr_engine.py": '''# OCR Engine - usa OpenCV + Tesseract
def run_ocr_on_image(image_path):
    import cv2
    import pytesseract

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text
''',

    "helena_core/extract_legenda.py": '''# Extrator de legenda por cor
def extract_legenda_from_image(image_path):
    # TODO: Implementar leitura de legenda com OpenCV + HSV
    return {}
''',

    "helena_core/build_dataset.py": '''# Monta dataset estruturado
def build_training_data():
    # TODO: Combina OCR com legenda para montar json/csv de treino
    pass
''',

    "helena_core/train_forro_model.py": '''# Treinamento da IA Helena
def train_model():
    # TODO: Inserir pipeline de classificação
    pass
''',

    "scripts/run_ocr_all.py": '''# Executa OCR em lote nas imagens da pasta
from helena_core.ocr_engine import run_ocr_on_image
import os

input_folder = "dataset/images_raw"
output_folder = "dataset/ocr_results"

os.makedirs(output_folder, exist_ok=True)

for img_file in os.listdir(input_folder):
    if img_file.lower().endswith((".png", ".jpg", ".jpeg")):
        path = os.path.join(input_folder, img_file)
        result = run_ocr_on_image(path)
        with open(os.path.join(output_folder, img_file + ".txt"), "w") as f:
            f.write(result)
''',

    "scripts/generate_report.py": '''# Gera relatório final da IA
def generate_helena_report():
    # TODO: Criar resumo da análise por planta
    pass
'''
}

# Criação dos diretórios
for d in directories:
    os.makedirs(d, exist_ok=True)

# Criação dos arquivos com conteúdo
for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

print("✅ Estrutura de OCR para forro criada com sucesso.")
