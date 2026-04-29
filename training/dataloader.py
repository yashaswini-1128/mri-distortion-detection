import os
import random
import cv2
import torch
from torch.utils.data import Dataset
from torchvision import transforms
from distortions import add_noise, add_blur

class MRIDataset(Dataset):
    def __init__(self, root_dir):
        self.paths = []

        for folder in ["healthy", "tumor"]:
            folder_path = os.path.join(root_dir, folder)
            for img in os.listdir(folder_path):
                self.paths.append(os.path.join(folder_path, img))

        self.transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize((224, 224)),
            transforms.ToTensor()
        ])

    def __len__(self):
        return len(self.paths)

    def __getitem__(self, idx):
        img = cv2.imread(self.paths[idx])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # 0: clean, 1: noise, 2: blur
        label = random.choice([0, 1, 2])

        if label == 1:
            img = add_noise(img)
        elif label == 2:
            img = add_blur(img)

        img = self.transform(img)
        return img.float(), torch.tensor(label)