import tkinter as tk
from . import image
import generate_mahjong.mahjong as gmm

def show_piece(question, canvas):
    s = ["pin1", "pin2", "pin3", "pin4", "pin5", "pin6", "pin7", "pin8", "pin9"]
    t = 1
    for i in range(len(question)):
        p = s[i]
        for k in range(question[i]):
            pin = image.images[p]
            canvas.create_image(
                64+59*t, 160.0,
                image=pin)
            t += 1
   
    return


def question(canvas, root, piece):
    print(piece)
    new_canvas = tk.Canvas(
        root,
        bg = "#000000",
        height = 630,
        width = 1003,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    new_canvas.place(x = 0, y = 0)
    g = gmm.mahjong(1, piece)
    question, yaku = g.generate_question()
    print(question, yaku)
    show_piece(question, new_canvas)

    '''
    pin1 = image.images["pin1"]
    new_canvas.create_image(
        506.5, 313.0,
        image=pin1)
    '''