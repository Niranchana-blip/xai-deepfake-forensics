from PIL import Image
import os


def preprocess_image(file_path):

    image = Image.open(file_path)

    image = image.convert("RGB")

    image = image.resize((224, 224))

    base, ext = os.path.splitext(file_path)
    processed_path = f"{base}_processed{ext}"

    image.save(processed_path)

    return {
        "processed_file": processed_path,
        "width": 224,
        "height": 224
    }