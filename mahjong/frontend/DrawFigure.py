import tkinter as tk
from . import Image

def draw_label(root, text_value, font_value, x_value, y_value):
    label = tk.Label(
        root,
        text = text_value,
        font = font_value,
        bg = "#F5F5F5"
    )
    label.place(x=x_value, y=y_value)

    return label