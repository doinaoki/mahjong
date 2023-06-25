import tkinter as tk
images = {}

def image():

    background_img = tk.PhotoImage(file = "design\\background.png")
    images["background"] = background_img
    img0 = tk.PhotoImage(file = f"design\\img0.png")
    images["img0"] = img0