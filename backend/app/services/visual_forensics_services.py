import cv2
import numpy as np


def analyze_image_visuals(file_path):

    image = cv2.imread(file_path)

    if image is None:
        return {
            "error": "Unable to read image"
        }

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    height, width = gray.shape

    brightness = float(np.mean(gray))
    contrast = float(np.std(gray))

    blur_score = float(
        cv2.Laplacian(gray, cv2.CV_64F).var()
    )

    return {
        "width": width,
        "height": height,
        "brightness": round(brightness, 2),
        "contrast": round(contrast, 2),
        "blur_score": round(blur_score, 2)
    }