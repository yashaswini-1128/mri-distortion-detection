import torch.nn as nn
from torchvision import models


class MRIModel(nn.Module):
    def __init__(self, num_classes=3):
        super().__init__()

        self.backbone = models.resnet18(weights="DEFAULT")

        # 🔥 MATCH TRAINING EXACTLY (256, not 512)
        self.backbone.fc = nn.Sequential(
            nn.Linear(self.backbone.fc.in_features, 256),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        return self.backbone(x)