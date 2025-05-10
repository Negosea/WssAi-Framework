 # faz OCR e extrai texto bruto

import pytesseract
from PIL import Image

def extract_text_from_image(image):
    pil_img = Image.fromarray(image)
    text = pytesseract.image_to_string(pil_img, lang='por')
    return text