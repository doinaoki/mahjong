import tkinter as tk
from . import image
import generate_mahjong.mahjong as gmm

def question_setting(canvas, root):
    new_canvas = tk.Canvas(
        root,
        bg = "#ffffff",
        height = 630,
        width = 1003,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    new_canvas.place(x = 0, y = 0)