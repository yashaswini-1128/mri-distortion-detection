from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "MRI Distortion Detection API"
    API_PREFIX: str = "/api/v1"

    MODEL_PATH: str = "weights/best_model.pth"
    DEVICE: str = "cpu"
    IMG_SIZE: int = 224

    ALLOWED_ORIGINS: list[str] = ["*"]

    class Config:
        env_file = ".env"

settings = Settings()