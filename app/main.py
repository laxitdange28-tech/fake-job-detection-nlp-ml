from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.predict import router


app = FastAPI(
    title="Fake Job Detection API",
    description="API for detecting fake and real job postings",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Router
app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Fake Job Detection API",
        "status": "Running"
    }


@app.get("/health")
def health_check():
    return {"status": "Healthy"}