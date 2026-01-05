import numpy as np
from src.utils import generate_data
from src.model import LinearRegression

def train_model(epochs=100, lr=0.1):
  X, y = generate_data()
  # Forcing x and y to be 1D arrays
  X = np.array(X).flatten()
  y = np.array(y).flatten()
  print("X shape:", X.shape, "y shape:", y.shape) # debugging
  
  model = LinearRegression()
  
  for epoch in range(epochs):
    y_pred = model.predict(X)
    
    error = y_pred - y
    # Arithmetic Broadcasting  / Gradient calculation
    dW = (2 / len(X)) * np.sum(error * X)
    dB = (2 / len(X)) * np.sum(error)
    
    model.update(dW, dB, lr)
    
    if epoch % 10 == 0:
      loss = np.mean(error ** 2)
      print(f"Epoch {epoch} | Loss: {loss:.4f}")
      
  print("Training complete")
  print("Learned weight:", round(float(model.weight), 2), "bias:", round(float(model.bias), 2))
  
  # Model Evaluation metrics (MSE - Mean Squared Error)
  y_final_pred = model.predict(X)
  mse = np.mean((y - y_final_pred)**2)
  
  print("Evaluation Metrics")
  print("Mean Squared Error: ", mse)
  
  MODEL_PATH = "/storage/emulated/0/projects/ml_playground/linear_model.npz"
  model.save(MODEL_PATH)
  print("Model Saved Successfully to: ", MODEL_PATH)
  