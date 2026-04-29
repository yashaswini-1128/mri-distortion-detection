from pydantic import BaseModel

class PredictionResponse(BaseModel):
    label: str
    confidence: float
    heatmap_image: str
    localized_image: str