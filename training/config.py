import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "dataset")
IMG_SIZE = 224
BATCH_SIZE = 16
EPOCHS = 10
LR = 1e-4

DEVICE = "cuda" if os.environ.get("CUDA_VISIBLE_DEVICES") else "cpu"

SAVE_DIR = os.path.join(BASE_DIR, "weights")
os.makedirs(SAVE_DIR, exist_ok=True)

MODEL_PATH = os.path.join(SAVE_DIR, "best_model.pth")