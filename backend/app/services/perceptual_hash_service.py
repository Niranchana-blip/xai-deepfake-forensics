from PIL import Image
import imagehash


def generate_perceptual_hashes(file_path):

    image = Image.open(file_path)

    return {
        "ahash": str(imagehash.average_hash(image)),
        "dhash": str(imagehash.dhash(image)),
        "phash": str(imagehash.phash(image))
    }