import torch
from PIL import Image
from torchvision import transforms

from backend.app.services.model_loader import load_model

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = load_model()
model.to(device)
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


def detect_deepfake(image_path):

    image = Image.open(image_path).convert("RGB")

    image_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():

        outputs = model(image_tensor)

        probabilities = torch.softmax(outputs, dim=1)

        print("LOGITS:", outputs)
        print("SOFTMAX:", probabilities)

    fake_prob = probabilities[0][0].item()
    real_prob = probabilities[0][1].item()

    label = "FAKE" if fake_prob > real_prob else "REAL"

    margin = abs(outputs[0][0] - outputs[0][1]).item()

    if margin > 0.8:
        confidence = "HIGH"
    elif margin > 0.4:
        confidence = "MEDIUM"
    else:
        confidence = "LOW"

    return {
        "model": "efficientnet_b0_ffpp_c23",
        "label": label,
        "fake_probability": round(fake_prob * 100, 4),
        "real_probability": round(real_prob * 100, 4),
        "confidence_margin": round(margin, 2),
        "confidence": confidence
    }