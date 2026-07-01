from backend.app.services.efficientnet_detector import detect_deepfake


def run_ai_models(image_path):

    results = []

    results.append(
        detect_deepfake(image_path)
    )

    return {
        "models": results
    }