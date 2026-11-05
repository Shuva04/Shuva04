# Breast Cancer Classification Demo

An educational binary-classification web application built with Django and scikit-learn. It predicts a dataset label using **mean radius** and **mean texture**.

> **Medical disclaimer:** This is a learning/demo project, not a medical device. It is not suitable for screening, diagnosis, treatment decisions or patient care. The model uses only two features and is not clinically validated.

## Features
- Train a reproducible Logistic Regression pipeline on scikit-learn's built-in Wisconsin Diagnostic Breast Cancer dataset.
- Input validation for mean radius and mean texture.
- Django page and JSON API.
- Clear educational disclaimer and model limitations.

## Requirements
Python 3.10+

## Setup
```bash
cd cancer-cell-detection
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Open http://127.0.0.1:8000.

## API
POST `/api/predict/` with JSON:
```json
{"mean_radius": 14.2, "mean_texture": 20.1}
```

## Model
The model is trained on two columns from the public dataset bundled with scikit-learn. Labels are mapped to human-readable dataset classes. Two features alone are insufficient for reliable real-world classification.

## Google Colab
You can run the same training script in Colab by uploading this folder or cloning the repository, installing requirements and running `python train_model.py`.

## Suggested caption
Built an educational breast-cancer classification demo using Python, scikit-learn and Django. The application explores how mean radius and mean texture can be used as model inputs, with a simple web interface and JSON API. This is a learning project only, not a clinical diagnostic system.
