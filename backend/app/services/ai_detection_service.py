from backend.app.services.ai_engine import run_ai_models


def analyze_media(file_path):
    return run_ai_models(file_path)