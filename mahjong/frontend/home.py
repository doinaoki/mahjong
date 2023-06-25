import tkinter as tk
from . import image
import generate_mahjong.mahjong as gmm


def btn_clicked(c,r):

    print("Button Clicked")
    c.place_forget()
    canvass = tk.Canvas(
        r,
        bg = "#ffffff",
        height = 630,
        width = 1003,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvass.place(x = 0, y = 0)
    background = canvass.create_image(
        506.5, 313.0,
        image=image.images["background"])



def home():
    print(gmm.mahjong().generate_question())

    root = tk.Tk()

    root.geometry("1003x630")  #アプリの位置調整
    root.configure(bg = "#123456")  #背景色
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

    image.image()
    background_img = image.images["background"]
    background = canvas.create_image(
        506.5, 313.0,
        image=background_img)

    img0 = image.images["img0"]
    b0 = tk.Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:btn_clicked(canvas, root),
        relief = "flat")
    print("b")
    b0.place(
        x = 385, y = 326,
        width = 202,
        height = 35)

    root.mainloop()