import tkinter as tk
images = {}

def image():

    background_img = tk.PhotoImage(file = "design\\background.png")
    images["background"] = background_img
    button1 = tk.PhotoImage(file = f"design\\button1.png")
    images["button1"] = button1
    button2 = tk.PhotoImage(file = f"design\\button2.png")
    images["button2"] = button2
    button3 = tk.PhotoImage(file = f"design\\button3.png")
    images["button3"] = button3
    piece7 = tk.PhotoImage(file = f"design\\7piece.png")
    images["piece7"] = piece7
    piece10 = tk.PhotoImage(file = f"design\\10_piece.png")
    images["piece10"] = piece10
    piece13 = tk.PhotoImage(file = f"design\\13_piece.png")
    images["piece13"] = piece13