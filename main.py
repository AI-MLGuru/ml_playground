from src.train import train_model
from src.model import LinearRegression
from src.utils import CONFIG
import numpy as np

np.random.seed(42) # Setting random seeds for consistent results
MODEL_PATH = "/storage/emulated/0/projects/ml_playground/linear_model.npz"

def run_training():
    print("Starting ML Pipeline")
    train_model(
      epochs=CONFIG["epochs"],
      lr=CONFIG["learning_rate"],
      MODEL_PATH=CONFIG["model_path"]
      )

def run_inference():
    model = LinearRegression()
    model.load(MODEL_PATH)

    X_new = np.array([0.5, 1.0, 1.5, 2.0])
    predictions = model.predict(X_new)

    print("Inference Results")
    for x, y in zip(X_new, predictions):
        print(f"x={x} → ŷ={y}")

if __name__ == "__main__":
    run_training()
    run_inference()