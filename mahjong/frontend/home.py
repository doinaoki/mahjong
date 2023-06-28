import tkinter as tk
from . import image
import generate_mahjong.mahjong as gmm
from . import select_question

def btn_clicked(canvas,root):

    print("Button Clicked")
    canvas.place_forget()
    select_question.select_question(canvas, root)

def start():
    root = tk.Tk()
    root.geometry("1003x630")  #アプリの位置調
    image.image()
    home(root)
    root.configure(bg = "#123456")  #背景色
    root.mainloop()

def home(root):
    #print(gmm.mahjong().generate_question())  
    #print(os.path.abspath(""))

    canvas = tk.Canvas(
        root,
        bg = "#000000",
        height = 630,
        width = 1003,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)


    background_img = image.images["background"]
    background = canvas.create_image(
        506.5, 313.0,
        image=background_img)

    button1 = image.images["button1"]
    b0 = tk.Button(
        image = button1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:btn_clicked(canvas, root),
        relief = "flat")
    b0.place(
        x = 385, y = 326,
        width = 202,
        height = 35)

