from pathlib import Path
import pytesseract


TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def configure_tesseract():
    tesseract_file = Path(TESSERACT_PATH)

    if tesseract_file.exists():
        pytesseract.pytesseract.tesseract_cmd = str(tesseract_file)


def read_text_from_image(image):
    configure_tesseract()

    config = "--oem 3 --psm 6"

    try:
        return pytesseract.image_to_string(image, config=config)
    except pytesseract.TesseractNotFoundError:
        return (
            "Tesseract OCR is not installed or not added to PATH.\n"
            "Install Tesseract OCR first, then run the project again.\n"
            "Common Windows path: C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        )
