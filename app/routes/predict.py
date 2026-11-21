import joblib
import pandas as pd

from pathlib import Path
from fastapi import APIRouter

from app.schemas.job import JobInput
from app.services.preprocessing import preprocess_text


router = APIRouter()

# Load trained model
BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE_DIR / "models" / "fake_job_model.pkl"

model = joblib.load(MODEL_PATH)


@router.post("/predict")
def predict_job(job: JobInput):

    # Convert input into dictionary
    job_data = job.model_dump()

    # Original text columns
    text_columns = [
        "title",
        "company_profile",
        "description",
        "requirements",
        "benefits"
    ]

    # Combine text
    combined_text = " ".join(
        str(job_data.get(column, "") or "")
        for column in text_columns
    )

    # Apply NLP preprocessing
    job_data["preprocessed_text"] = preprocess_text(combined_text)

    # Prepare DataFrame
    input_df = pd.DataFrame([job_data])

    # Predict
    prediction = int(model.predict(input_df)[0])

    result = "Fake Job" if prediction == 1 else "Real Job"

    return {
        "prediction": prediction,
        "result": result
    }