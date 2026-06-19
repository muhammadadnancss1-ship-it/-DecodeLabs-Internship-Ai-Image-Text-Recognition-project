import cv2


def convert_to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def reduce_noise(gray_image):
    return cv2.GaussianBlur(gray_image, (5, 5), 0)


def apply_threshold(blurred_image):
    return cv2.adaptiveThreshold(
        blurred_image,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        11
    )


def prepare_for_ocr(image):
    gray_image = convert_to_gray(image)
    smooth_image = reduce_noise(gray_image)
    clean_image = apply_threshold(smooth_image)
    return clean_image
