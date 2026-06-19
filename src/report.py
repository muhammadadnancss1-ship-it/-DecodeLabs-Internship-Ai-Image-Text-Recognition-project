from pathlib import Path
import cv2


def create_parent_folder(output_path):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)


def save_processed_image(image, output_path):
    create_parent_folder(output_path)
    cv2.imwrite(str(output_path), image)


def save_text_report(text, output_path):
    create_parent_folder(output_path)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("AI Image or Text Recognition Result\n")
        file.write("=" * 45)
        file.write("\n\n")

        if text.strip():
            file.write(text.strip())
        else:
            file.write("No readable text was detected.")

        file.write("\n")
