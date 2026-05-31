import hashlib


def generate_file_hashes(file_path):

    sha256_hash = hashlib.sha256()
    md5_hash = hashlib.md5()

    with open(file_path, "rb") as f:

        for byte_block in iter(lambda: f.read(4096), b""):

            sha256_hash.update(byte_block)
            md5_hash.update(byte_block)

    return {
        "sha256": sha256_hash.hexdigest(),
        "md5": md5_hash.hexdigest()
    }