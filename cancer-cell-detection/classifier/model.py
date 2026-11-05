from functools import lru_cache
from pathlib import Path
import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

MODEL_PATH = Path(__file__).resolve().parent / "breast_cancer_demo.joblib"

@lru_cache(maxsize=1)
def get_model():
    if MODEL_PATH.exists():
        return joblib.load(MODEL_PATH)
    data = load_breast_cancer()
    # Dataset feature names are mean radius and mean texture.
    indices = [list(data.feature_names).index("mean radius"),
               list(data.feature_names).index("mean texture")]
    X = data.data[:, indices]
    y = data.target
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, random_state=42))
    model.fit(X, y)
    return model

def predict(mean_radius: float, mean_texture: float):
    model = get_model()
    prediction = int(model.predict([[mean_radius, mean_texture]])[0])
    probabilities = model.predict_proba([[mean_radius, mean_texture]])[0]
    # sklearn dataset target 0 = malignant, 1 = benign.
    return {
        "class": "malignant" if prediction == 0 else "benign",
        "dataset_label": int(prediction),
        "probability": float(probabilities[prediction]),
    }
