import tkinter as tk
from . import image
import generate_mahjong.mahjong as gmm
from . import question_setting
from . import home

def btn2_clicked(canvas, root):
    canvas.place_forget()
    print("btn2 clicked")
    question_setting.question_setting(canvas, root)

def btn3_clicked(canvas, root):
    print("btn3 clicked")

def backb_clicked(canvas, root):
    canvas.place_forget()
    home.home(root)
    print("back")


def select_question(canvas, root):
    new_canvas = tk.Canvas(
        root,
        bg = "#000000",
        height = 630,
        width = 1003,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    new_canvas.place(x = 0, y = 0)
    background = new_canvas.create_image(
        506.5, 313.0,
        image=image.images["background"])
    
    button2 = image.images["button2"]
    b2 = tk.Button(
        image = button2,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:btn2_clicked(new_canvas, root),
        relief = "flat")
    b2.place(
        x = 385, y = 326,
        width = 202,
        height = 35)
    
    button3 = image.images["button3"]
    b3 = tk.Button(
        image = button3,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:btn3_clicked(new_canvas, root),
        relief = "flat")
    b3.place(
        x = 385, y = 400,
        width = 202,
        height = 35)
    
    backpage = image.images["backpage"]
    backb = tk.Button(
        image = backpage,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:backb_clicked(new_canvas, root),
        relief = "flat")
    backb.place(
        x = 5, y = 550,
        width = 202,
        height = 35)