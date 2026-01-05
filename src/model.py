import numpy as np
# Pure ML Fundamentals, NO sklearn. No shortcuts
np.random.seed(42) # Setting random seeds for consistent results
class LinearRegression:
  def __init__(self):
    self.weight = np.random.randn()
    self.bias = 0.0
    
  def predict(self, X):
    return self.weight * X + self.bias
    
  def update(self, dW, dB, lr):
    self.weight -= lr * dW
    self.bias -= lr * dB
    
  def save(self, MODEL_PATH = "/storage/emulated/0/projects/ml_playground/linear_model.npz"):
    np.savez(MODEL_PATH, weight=self.weight, bias=self.bias)
  def load(self, MODEL_PATH = "/storage/emulated/0/projects/ml_playground/linear_model.npz"):
    data = np.load(MODEL_PATH)
    self.weight = data["weight"].item()
    self.bias = data["bias"].item()