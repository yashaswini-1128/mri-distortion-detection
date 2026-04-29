import torch
import numpy as np
import cv2


class GradCAM:
    def __init__(self, model, target_layer):
        self.model = model
        self.target_layer = target_layer

        self.gradients = None
        self.activations = None

        self.target_layer.register_forward_hook(self.save_activation)
        self.target_layer.register_full_backward_hook(self.save_gradient)

    def save_activation(self, module, input, output):
        self.activations = output.detach()

    def save_gradient(self, module, grad_input, grad_output):
        self.gradients = grad_output[0].detach()

    def generate(self, input_tensor, class_idx):
        output = self.model(input_tensor)

        self.model.zero_grad()
        loss = output[0, class_idx]
        loss.backward()

        grads = self.gradients[0]         # (C,H,W)
        activations = self.activations[0]

        weights = torch.mean(grads, dim=(1, 2))

        cam = torch.zeros(activations.shape[1:], dtype=torch.float32)

        for i, w in enumerate(weights):
            cam += w * activations[i]

        cam = torch.relu(cam)

        cam = cam.cpu().numpy()

        # 🔥 Normalize
        cam = cam - np.min(cam)
        cam = cam / (np.max(cam) + 1e-8)

        return cam