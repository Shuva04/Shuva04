"""Train and save the two-feature educational classifier."""
from classifier.model import get_model, MODEL_PATH
import joblib

if __name__ == "__main__":
    model = get_model()
    joblib.dump(model, MODEL_PATH)
    print(f"Saved demo model to {MODEL_PATH}")
