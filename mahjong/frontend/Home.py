import tkinter as tk
from . import Image
import generate_mahjong.mahjong as gmm
from . import SelectQuestion

def btn_clicked(canvas,root):

    canvas.delete("all")
    canvas.place_forget()
    SelectQuestion.select_question(canvas, root)

def start():
    root = tk.Tk()
    root.geometry("1003x630")  #アプリの位置調
    Image.image()
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


    background_img = Image.images["background"]
    background = canvas.create_image(
        506.5, 313.0,
        image=background_img)

    button1 = Image.images["button1"]
    b0 = tk.Button(
        image = button1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:btn_clicked(canvas, root),
        relief = "flat",)
    b0.place(
        x = 352, y = 326,
        width = 295,
        height = 50)
    b0["bg"] = "black"
    b0["border"] = "0"

