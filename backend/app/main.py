from fastapi import FastAPI
from backend.app.api.upload import router as upload_router

app = FastAPI(
    title="XAI Deepfake Forensics API",
    version="1.0.0"
)

app.include_router(upload_router)

@app.get("/")
def root():
    return {
        "message": "XAI Deepfake Forensics API Running"
    }