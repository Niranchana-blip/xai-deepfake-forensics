from fastapi import APIRouter, UploadFile, File
from backend.app.utils.validators import validate_file
import os
import shutil

router = APIRouter()

UPLOAD_DIR = "backend/uploads"


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    # VALIDATE FILE FIRST
    await validate_file(file)

    # SAVE FILE
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "status": "uploaded successfully"
    }