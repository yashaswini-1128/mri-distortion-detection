import numpy as np
import cv2
from PIL import Image
import io
import torch
import torchvision.transforms as transforms


# ✅ Read image safely
def read_image_from_bytes(image_bytes):
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        return np.array(image)
    except Exception as e:
        raise ValueError(f"Invalid image file: {e}")


# ✅ Preprocessing for model
def preprocess(image):
    transform = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    image = transform(image).unsqueeze(0)  # add batch dimension
    return image