import numpy as np

CONFIG = {
    "epochs": 100,
    "learning_rate": 0.1,
    "seed": 42,
    "model_path": "/storage/emulated/0/projects/ml_playground/linear_model.npz"
}
def generate_data(n_samples=100):
  X = np.random.rand(n_samples, 1)
  y = 2 * X + 1 + (0.1 * np.random.randn(n_samples, 1)) # y = 2x + 1 + noise
  return X, y