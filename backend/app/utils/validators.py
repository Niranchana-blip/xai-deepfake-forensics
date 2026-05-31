from fastapi import HTTPException
import os

ALLOWED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".mp4",
    ".avi",
    ".mov"
}

MAX_FILE_SIZE = 100 * 1024 * 1024  # 100 MB


def validate_file(file):

    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type"
        )

    file.file.seek(0, 2)
    size = file.file.tell()
    file.file.seek(0)

    if size == 0:
        raise HTTPException(
            status_code=400,
            detail="Empty file"
        )

    if size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File exceeds 100 MB limit"
        )