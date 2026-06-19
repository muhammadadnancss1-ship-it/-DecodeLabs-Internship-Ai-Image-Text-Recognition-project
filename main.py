from pathlib import Path

from src.image_loader import get_image_path, load_image
from src.preprocess import prepare_for_ocr
from src.recognizer import read_text_from_image
from src.report import save_processed_image, save_text_report


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_IMAGE = r"E:\New folder (6)\ai_image_text_recognition_project\ai_image_text_recognition_project\data\samples\sample_text.png"
OUTPUT_DIR = BASE_DIR / "outputs"


def show_header():
    print("AI Image or Text Recognition")
    print("Basic OCR Pipeline with OpenCV and Tesseract")
    print("-" * 60)


def main():
    show_header()

    image_path = get_image_path(DEFAULT_IMAGE)
    original_image = load_image(image_path)

    processed_image = prepare_for_ocr(original_image)
    recognized_text = read_text_from_image(processed_image)

    save_processed_image(processed_image, OUTPUT_DIR / "processed_image.png")
    save_text_report(recognized_text, OUTPUT_DIR / "recognized_text.txt")

    print("\nRecognition completed.\n")
    print("Recognized Text:")
    print("-" * 60)

    if recognized_text.strip():
        print(recognized_text.strip())
    else:
        print("No clear text was detected. Try a sharper image.")

    print("-" * 60)
    print("Processed image saved at:", OUTPUT_DIR / "processed_image.png")
    print("Text report saved at:", OUTPUT_DIR / "recognized_text.txt")


if __name__ == "__main__":
    main()
