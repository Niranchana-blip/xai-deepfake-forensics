from fastapi import UploadFile, HTTPException

ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png"]
ALLOWED_VIDEO_TYPES = ["video/mp4", "video/quicktime"]

MAX_IMAGE_SIZE = 10 * 1024 * 1024      # 10 MB
MAX_VIDEO_SIZE = 100 * 1024 * 1024     # 100 MB


async def validate_file(file: UploadFile):

    # CHECK FILE TYPE
    if file.content_type not in (
        ALLOWED_IMAGE_TYPES + ALLOWED_VIDEO_TYPES
    ):
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type"
        )

    # READ FILE CONTENT
    contents = await file.read()

    # GET FILE SIZE
    file_size = len(contents)
    print(file_size)

    # RESET POINTER
    file.file.seek(0)

    # IMAGE SIZE CHECK
    if file.content_type in ALLOWED_IMAGE_TYPES:
        if file_size > MAX_IMAGE_SIZE:
            raise HTTPException(
                status_code=400,
                detail="Image exceeds 10MB limit"
            )

    # VIDEO SIZE CHECK
    if file.content_type in ALLOWED_VIDEO_TYPES:
        if file_size > MAX_VIDEO_SIZE:
            raise HTTPException(
                status_code=400,
                detail="Video exceeds 100MB limit"
            )

    return True