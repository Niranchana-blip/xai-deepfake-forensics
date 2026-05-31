from fastapi import APIRouter, UploadFile, File
from backend.app.services.metadata_service import generate_file_hashes
import os
import shutil

router = APIRouter()

UPLOAD_DIR = "backend/uploads"


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # GENERATE HASHES
    hashes = generate_file_hashes(file_path)
    print("HASHES =", hashes)
    print(type(hashes))


    return {
        "filename": file.filename,
        "status": "uploaded successfully",
        "sha256": hashes["sha256"],
        "md5": hashes["md5"]
    }