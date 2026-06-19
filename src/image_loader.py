from pathlib import Path
import cv2


def get_image_path(default_image):
    print("\nEnter image path for recognition.")
    print("Press Enter to use the default sample image.")
    print("Default:", default_image)

    user_path = input("\nImage path: ").strip().strip('"')

    if not user_path:
        return Path(default_image)

    return Path(user_path)


def load_image(image_path):
    image_path = Path(image_path)

    if not image_path.exists():
        raise FileNotFoundError(f"Image file not found: {image_path}")

    image = cv2.imread(str(image_path))

    if image is None:
        raise ValueError("The selected file could not be opened as an image.")

    return image