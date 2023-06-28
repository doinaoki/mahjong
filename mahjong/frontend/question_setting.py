import tkinter as tk
from . import image
import generate_mahjong.mahjong as gmm
from . import question

def btn3_clicked(radio_value):
    print(radio_value.get())

def btn2_clicked(canvas, root, radio_value):
    canvas.place_forget()
    question.question(canvas, root, radio_value)

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

    radio_value = tk.IntVar(value = 7)
    piece7 = image.images["piece7"]
    p7 = tk.Radiobutton(
        root,
        image = piece7,
        variable = radio_value,
        value = 7,
        command = lambda:btn3_clicked(radio_value),
        indicatoron = False
    )
    p7.place(
        x = 320, y = 200,
        width = 120,
        height = 40)
    
    piece10 = image.images["piece10"]
    p10 = tk.Radiobutton(
        root,
        image = piece10,
        variable = radio_value,
        value = 10,
        command = lambda:btn3_clicked(radio_value),
        indicatoron = False
    )
    p10.place(
        x = 440, y = 200,
        width = 120,
        height = 40)
    
    piece13 = image.images["piece13"]
    p13 = tk.Radiobutton(
        root,
        image = piece13,
        variable = radio_value,
        value = 13,
        command = lambda:btn3_clicked(radio_value),
        indicatoron = False
    )
    p13.place(
        x = 560, y = 200,
        width = 120,
        height = 40)
    
    button2 = image.images["button2"]
    b2 = tk.Button(
        image = button2,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:btn2_clicked(new_canvas, root, radio_value.get()),
        relief = "flat")
    b2.place(
        x = 385, y = 326,
        width = 202,
        height = 35)
    


