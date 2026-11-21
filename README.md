# Fake Job Detection using NLP & Machine Learning

An end-to-end Machine Learning project that detects whether a job posting is **Real or Fake** using Natural Language Processing (NLP) and Machine Learning.

## Live Demo

- **Frontend:** https://fake-job-detection-nlp-ml-1.onrender.com
- **Backend API:** https://fake-job-detection-nlp-api.onrender.com
- **API Documentation:** https://fake-job-detection-nlp-api.onrender.com/docs

## Project Overview

Fake job postings can mislead job seekers and cause financial losses.

This project analyzes job descriptions and predicts whether a job posting is genuine or fraudulent.

## Technologies Used

- Python
- Pandas & NumPy
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Linear Support Vector Machine (Linear SVM)
- FastAPI
- HTML, CSS & JavaScript
- Docker
- Git & GitHub
- Render

## Machine Learning Model

The project uses a Linear SVM classifier with TF-IDF text features.

| Metric | Score |
|---|---:|
| Accuracy | 98.57% |
| Precision | 84.27% |
| Recall | 86.71% |
| F1 Score | 85.47% |

*These scores are from the project's evaluation dataset.*

## Features

- Detects real and fraudulent job postings.
- NLP-based text preprocessing.
- TF-IDF feature extraction.
- Machine Learning prediction.
- FastAPI prediction endpoint.
- Web-based user interface.
- Docker containerization.
- Cloud deployment using Render.

## Project Structure

```text
fake-job-detection-nlp-ml/
│
├── app/
│   ├── main.py
│   ├── routes/
│   ├── schemas/
│   └── services/
│
├── data/
│   └── raw/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── models/
│   └── fake_job_model.pkl
│
├── notebooks/
├── Dockerfile
├── requirements.txt
└── README.md
```

## API Endpoint

**POST** `/predict`

The API accepts job description text and returns a prediction.

API documentation:

https://fake-job-detection-nlp-api.onrender.com/docs

## Run Locally

1. Clone the repository:

```bash
git clone https://github.com/laxitdange28-tech/fake-job-detection-nlp-ml.git
```

2. Open the project:

```bash
cd fake-job-detection-nlp-ml
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the environment:

```bash
source .venv/bin/activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

7. Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

## Dataset

Dataset: Real or Fake Job Posting Prediction

Source: Kaggle — shivamb

## Author

GitHub: https://github.com/laxitdange28-tech
```

**Step 3:** Save karo (`Ctrl + S`), phir terminal mein:

```bash
git add README.md
git commit -m "Update project README"
git push
```

