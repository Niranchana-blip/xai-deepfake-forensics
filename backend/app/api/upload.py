from fastapi import APIRouter, UploadFile, File
from backend.app.services.hash_service import generate_file_hashes
from backend.app.utils.validators import validate_file
from backend.app.services.metadata_service import extract_metadata
import os
import shutil

router = APIRouter()

UPLOAD_DIR = "backend/uploads"


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    validate_file(file)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # GENERATE HASHES
    hashes = generate_file_hashes(file_path)
    metadata = extract_metadata(file_path)
    print("HASHES =", hashes)
    print(type(hashes))
    


    return {
    "filename": file.filename,
    "status": "uploaded successfully",
    "sha256": hashes["sha256"],
    "md5": hashes["md5"],
    "metadata": metadata
}