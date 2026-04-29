import torch
import cv2
import numpy as np

from app.models.cnn import MRIModel
from app.core.config import settings
from app.services.gradcam import GradCAM
from app.services.localization import apply_localization
from app.utils.image import preprocess
from app.core.logger import logger


class InferenceEngine:
    def __init__(self):
        self.device = settings.DEVICE

        # Load model
        self.model = MRIModel(num_classes=3)
        self.model.load_state_dict(
            torch.load(settings.MODEL_PATH, map_location=self.device)
        )
        self.model.to(self.device)
        self.model.eval()

        print("✅ Model loaded successfully")

        # 🔥 IMPORTANT: correct layer (ResNet)
        self.gradcam = GradCAM(self.model, self.model.backbone.layer4)

        self.labels = ["Clean", "Noise", "Blur"]
        logger.info("Model loaded successfully")

    def predict(self, image_np):
        try:
            # Preprocess
            input_tensor = preprocess(image_np).to(self.device)

            # Forward
            with torch.no_grad():
                output = self.model(input_tensor)
                probs = torch.softmax(output, dim=1)

            pred = torch.argmax(probs).item()
            confidence = float(torch.max(probs).cpu().numpy())

            # GradCAM
            heatmap = self.gradcam.generate(input_tensor, pred)

            # Resize heatmap
            heatmap_resized = cv2.resize(
                heatmap, (image_np.shape[1], image_np.shape[0])
            )

            # Convert to color
            heatmap_color = cv2.applyColorMap(
                np.uint8(255 * heatmap_resized),
                cv2.COLORMAP_JET
            )

            # 🔥 Better overlay
            overlay = cv2.addWeighted(image_np, 0.5, heatmap_color, 0.5, 0)

            # Localization
            localized = apply_localization(image_np.copy(), heatmap)

            return {
                "label": self.labels[pred],
                "confidence": confidence,
                "gradcam": overlay,
                "localized": localized
            }

        except Exception as e:
            return {"error": str(e)}
        