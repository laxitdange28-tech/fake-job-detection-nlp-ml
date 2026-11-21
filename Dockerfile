# 1. Python base image
FROM python:3.14-slim

# 2. Working directory
WORKDIR /app

# 3. NLTK data location
ENV NLTK_DATA=/usr/local/share/nltk_data

# 4. Copy requirements
COPY requirements.txt .

# 5. Install Python dependencies
RUN pip install --no-cache-dir --default-timeout=120 --retries=10 -r requirements.txt

# 6. Download required NLTK resources
RUN python -m nltk.downloader -d /usr/local/share/nltk_data \
    stopwords \
    wordnet \
    punkt_tab \
    averaged_perceptron_tagger_eng \
    omw-1.4

# 7. Copy application files
COPY app/ ./app/
COPY models/ ./models/

# 8. Expose API port
EXPOSE 8000

# 9. Start FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]