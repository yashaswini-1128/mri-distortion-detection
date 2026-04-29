import cv2
import numpy as np

def add_noise(img):
    noise = np.random.normal(0, 20, img.shape)
    return np.clip(img + noise, 0, 255).astype(np.uint8)

def add_blur(img):
    return cv2.GaussianBlur(img, (7, 7), 0)