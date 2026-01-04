class BaseModel:
  """
  A simple base class any ML models.
  Any future model should follow this structure
  """
  def __init__(self):
    self.is_trained = False
    
  def train(self, x, y):
    raise NotImplementedError("Train method not implemented")
  def predict(self, x, y):
    raise NotImplementedError("Predict method not implemented")