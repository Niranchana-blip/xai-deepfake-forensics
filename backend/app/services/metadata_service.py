import hashlib


def generate_file_hashes(file_path):

    sha256 = hashlib.sha256()
    md5 = hashlib.md5()

    with open(file_path, "rb") as f:

        while chunk := f.read(4096):
            sha256.update(chunk)
            md5.update(chunk)

    return {
        "sha256": sha256.hexdigest(),
        "md5": md5.hexdigest()
    }