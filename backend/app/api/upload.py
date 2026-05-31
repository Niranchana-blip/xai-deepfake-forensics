from fastapi import APIRouter, UploadFile, File
from backend.app.services.hash_service import generate_file_hashes
from backend.app.utils.validators import validate_file
from backend.app.services.metadata_service import extract_metadata
from backend.app.services.malware_scan import scan_file
from backend.app.services.preprocessing_service import preprocess_image
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

    scan_result = scan_file(file_path)
    if not scan_result["safe"]:
        return {
            "status": "rejected",
            "reason": scan_result["message"]
        }
        

    # GENERATE HASHES
    hashes = generate_file_hashes(file_path)
    metadata = extract_metadata(file_path)
    preprocessing = preprocess_image(file_path)
    print("HASHES =", hashes)
    print(type(hashes))
    


    return {
    "filename": file.filename,
    "status": "uploaded successfully",
    "sha256": hashes["sha256"],
    "md5": hashes["md5"],
    "malware_scan": scan_result,
    "metadata": metadata,
    "preprocessing": preprocessing
}