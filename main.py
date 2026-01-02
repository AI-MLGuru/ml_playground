import tkinter as tk
from src.utils import get_app_config

def main():
  config = get_app_config()
  root = tk.Tk()
  root.title("ML Playground")
  root.geometry(f"{config['width']}x{config['height']}")
  
  label = tk.Label(
    root,
    text = config["welcome_text"],
    font = ("Arial", 14)
  )
  label.pack(expand=True)
  
  root.mainloop()
  
if __name__ == "__main__":
  main()