import torch
from torchvision.models import efficientnet_b0

MODEL_PATH = "models/image_models/efficientnet_b0_ffpp_c23.pth"

model = None


def load_model():

    global model

    if model is None:

        model = efficientnet_b0()

        model.classifier[1] = torch.nn.Linear(
            model.classifier[1].in_features,
            2
        )

        state_dict = torch.load(
            MODEL_PATH,
            map_location="cpu",
            weights_only=False
        )

        model.load_state_dict(state_dict)


        model.eval()

    return model