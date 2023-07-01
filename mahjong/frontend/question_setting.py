import tkinter as tk
from . import image
import generate_mahjong.mahjong as gmm
from . import question

def btn3_clicked(radio_value):
    print(radio_value.get())

def btn2_clicked(canvas, root, radio_value, check_value):
    canvas.place_forget()
    q = question.question()
    q.question(canvas, root, radio_value, check_value, q)

def cb1_clicked(c):
    print(f"value = {c.get()} ckeck_button_clicked")

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
    
    
    check_value1 = tk.BooleanVar(value = True)
    cb1 = tk.Checkbutton(
        root,
        image = image.images["tenpai"],
        command = lambda:cb1_clicked(check_value1),
        variable = check_value1,
        indicatoron = False
    )
    cb1.place(
        x = 315, y = 326,
        width = 155,
        height = 35)


    button2 = image.images["button2"]
    b2 = tk.Button(
        image = button2,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:btn2_clicked(new_canvas, root, radio_value.get(), check_value1.get()),
        relief = "flat")
    b2.place(
        x = 385, y = 426,
        width = 202,
        height = 35)