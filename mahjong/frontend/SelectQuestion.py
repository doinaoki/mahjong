import tkinter as tk
from . import Image
import generate_mahjong.mahjong as gmm
from . import QuestionSetting
from . import Home
from . import ListMissQuestion
from . import ListPuzzledQuestion

widgits = []

def btn2_clicked(canvas, root):
    canvas.delete("all")
    canvas.place_forget()
    for i in widgits:
        i.destroy()
    print("btn2 clicked")
    q = QuestionSetting.QuestionSetting()
    q.question_setting(canvas, root)

def btn3_clicked(canvas, root):
    canvas.delete("all")
    canvas.place_forget()
    for i in widgits:
        i.destroy()
    l = ListMissQuestion.ListMissQuestion()
    l.show_list(canvas, root)
    print("btn3 clicked")

def btn4_clicked(canvas, root):
    canvas.delete("all")
    canvas.place_forget()
    for i in widgits:
        i.destroy()
    l = ListPuzzledQuestion.ListPuzzledQuestion()
    l.show_list(canvas, root)
    print("btn3 clicked")

def backb_clicked(canvas, root):
    canvas.delete("all")
    canvas.place_forget()
    for i in widgits:
        i.destroy()
    Home.home(root)
    print("back")


def select_question(canvas, root):
    global widgits
    widgits = []
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
        image=Image.images["background"])
    
    button2 = Image.images["button2"]
    b2 = tk.Button(
        image = button2,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:btn2_clicked(new_canvas, root),
        relief = "flat",
        background="#666571")
    b2.place(
        x = 352, y = 326,
        width = 295,
        height = 50)
    widgits.append(b2)
    
    button3 = Image.images["button3"]
    b3 = tk.Button(
        image = button3,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:btn3_clicked(new_canvas, root),
        relief = "flat",
        background="#666571")
    b3.place(
        x = 349, y = 396,
        width = 295,
        height = 50)
    widgits.append(b3)
    
    button4 = Image.images["button4"]
    b4 = tk.Button(
        image = button4,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:btn4_clicked(new_canvas, root),
        relief = "flat",
        background="#666571")
    b4.place(
        x = 349, y = 466,
        width = 295,
        height = 50)
    widgits.append(b4)
    
    backpage = Image.images["backpage"]
    backb = tk.Button(
        image = backpage,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:backb_clicked(new_canvas, root),
        relief = "flat",
        background="#666571")
    backb.place(
        x = 346, y = 536,
        width = 295,
        height = 50)
    widgits.append(backb)