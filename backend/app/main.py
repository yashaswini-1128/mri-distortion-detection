from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.routes import router
from app.core.config import settings

app = FastAPI(
    title="MRI Distortion Detection System",
    docs_url="/docs",      # 🔥 Swagger opens at root
    redoc_url=None     # optional (removes /redoc)
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(router, prefix=settings.API_PREFIX)

# Health check
@app.get("/")
def root():
    return {"message": "MRI Backend Running"}

@app.get("/health")
def health():
    return {"status": "OK"}

# Global error handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": str(exc)}   # 🔥 shows real error
    )