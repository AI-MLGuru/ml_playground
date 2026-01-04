import numpy as np
# Pure ML Fundamentals, NO sklearn. No shortcuts
class LinearRegression:
  def __init__(self):
    self.weight = np.random.randn()
    self.bias = 0.0
    
  def predict(self, X):
    return self.weight * X + self.bias
    
  def update(self, dW, dB, lr):
    self.weight -= lr * dW
    self.bias -= lr * dB