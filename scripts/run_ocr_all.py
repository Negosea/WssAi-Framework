# Executa OCR em lote nas imagens da pasta
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
