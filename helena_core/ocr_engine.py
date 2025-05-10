# OCR Engine - usa OpenCV + Tesseract
def run_ocr_on_image(image_path):
    import cv2
    import pytesseract

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text
