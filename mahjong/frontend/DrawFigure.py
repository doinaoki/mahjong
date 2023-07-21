import tkinter as tk
from . import Image

def draw_label(root, text_value, font_value, x_value, y_value):
    label = tk.Label(
        root,
        text = text_value,
        font = font_value,
    )
    label.config(bg="black")
    label.place(x=x_value, y=y_value)

    return label