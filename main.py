from src.train import train_model
from src.model import LinearRegression

def main():
  print("Starting ML Pipeline")
  train_model()
  model = LinearRegression()
  MODEL_PATH = "/storage/emulated/0/projects/ml_playground/linear_model.npz"
  model.load(MODEL_PATH)
  print("Loaded Model Parameters")
  print("Weight:", model.weight, "Bias:", model.bias)

if __name__ == "__main__":
  main()