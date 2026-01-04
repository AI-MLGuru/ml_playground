from src.utils import load_dummy_data
from src.model import train_fake_model

def train_model():
  print("Loading data ...")
  X, y = load_dummy_data()
  
  print("Training model ...")
  model = train_fake_model(X, y)
  
  print("Training complete")
  print("Model:", model)