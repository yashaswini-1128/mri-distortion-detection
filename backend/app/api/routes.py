from fastapi import APIRouter, UploadFile, File
from app.services.inference import InferenceEngine
from app.utils.image import read_image_from_bytes
from app.utils.encoder import encode_image

router = APIRouter()
engine = InferenceEngine()


@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    # ✅ Step 1: read uploaded file
    image_bytes = await file.read()

    # ✅ Step 2: convert bytes → numpy image
    image_np = read_image_from_bytes(image_bytes)

    # ✅ Step 3: run model
    result = engine.predict(image_np)

    # ✅ Step 4: convert images → base64 (for API response)
    result["gradcam"] = "data:image/png;base64," + encode_image(result["gradcam"])
    result["localized"] = "data:image/png;base64," + encode_image(result["localized"])

    return result