import torch
from torchvision import models


def load_model():

    model = models.efficientnet_b0(weights="DEFAULT")

    model.eval()

    return model