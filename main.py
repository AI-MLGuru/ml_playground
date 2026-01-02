import tkinter as tk

def main():
  root = tk.Tk()
  root.title("ML Playground")
  root.geometry("400x300")
  
  label = tk.Label(
    root,
    text = "ML Playground\nFoundation step",
    font = ("Arial", 14)
  )
  label.pack(expand=True)
  
  root.mainloop()
  
if __name__ == "__main__":
  main()