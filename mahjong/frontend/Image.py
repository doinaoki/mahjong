import tkinter as tk
import os
from PIL import Image, ImageTk

images = {}

def image():
    #print(os.getcwd())
    images["background"] = ImageTk.PhotoImage(file = "design/back_ground.png")
    images["button1"] = ImageTk.PhotoImage(file = f"design/button1.png")
    images["button2"] = ImageTk.PhotoImage(file = f"design/button2.png")
    images["button3"] = ImageTk.PhotoImage(file = f"design/button3.png")
    images["button4"] = ImageTk.PhotoImage(file = f"design/puzzledbutton.png")

    #miss_page
    images["missbackground"] = ImageTk.PhotoImage(file = f"design/missbackground.png")
    images["missbackpage"] = ImageTk.PhotoImage(file = f"design/missbackpage.png")
    images["deletebutton"] = ImageTk.PhotoImage(file = f"design/deletebutton.png")
    images["answerbutton"] = ImageTk.PhotoImage(file = f"design/answerbutton.png")


    #setting_page

    images["settingbackground"] = ImageTk.PhotoImage(file = f"design/setting_background.png")

    images["piece7"] = ImageTk.PhotoImage(file = f"design/7piece.png")
    images["piece10"] = ImageTk.PhotoImage(file = f"design/10_piece.png")
    images["piece13"] = ImageTk.PhotoImage(file = f"design/13_piece.png")

    img = Image.open("design/1pin.png")
    (width, height) = (img.width // 2, img.height // 2)
    images["pin1"] = ImageTk.PhotoImage(Image.open("design/1pin.png").resize((width, height)))
    images["pin2"] = ImageTk.PhotoImage(Image.open("design/2pin.png").resize((width, height)))
    images["pin3"] = ImageTk.PhotoImage(Image.open("design/3pin.png").resize((width, height)))
    images["pin4"] = ImageTk.PhotoImage(Image.open("design/4pin.png").resize((width, height)))
    images["pin5"] = ImageTk.PhotoImage(Image.open("design/5pin.png").resize((width, height)))
    images["pin6"] = ImageTk.PhotoImage(Image.open("design/6pin.png").resize((width, height)))
    images["pin7"] = ImageTk.PhotoImage(Image.open("design/7pin.png").resize((width, height)))
    images["pin8"] = ImageTk.PhotoImage(Image.open("design/8pin.png").resize((width, height)))
    images["pin9"] = ImageTk.PhotoImage(Image.open("design/9pin.png").resize((width, height)))

    images["Ntenpai"] = ImageTk.PhotoImage(file = f"design/Ntenpai.png")
    images["Ytenpai"] = ImageTk.PhotoImage(file = f"design/Ytenpai.png")

    images["normal"] = ImageTk.PhotoImage(file = f"design/normal.png")
    images["difficult"] = ImageTk.PhotoImage(file = f"design/difficult.png")
    images["random"] = ImageTk.PhotoImage(file = f"design/random.png")

    images["startbutton"] = ImageTk.PhotoImage(file = f"design/start_button.png")
    images["backbutton"] = ImageTk.PhotoImage(file = f"design/back_button.png")
    images["createbutton"] = ImageTk.PhotoImage(file = f"design/createbutton.png")

    #question_page
    images["questionbackground"] = ImageTk.PhotoImage(file = f"design/question_background.png")
    images["decision"] = ImageTk.PhotoImage(file = f"design/decision.png")
    images["puzzledbutton"] = ImageTk.PhotoImage(file = f"design/puzzled.png")

    #result_page
    images["resultbackground"] = ImageTk.PhotoImage(file = f"design/result_background.png")
    images["uncorrect"] = ImageTk.PhotoImage(file = f"design/uncorrect.png")
    images["correct"] = ImageTk.PhotoImage(file = f"design/correct.png")

    images["backpage"] = ImageTk.PhotoImage(file = f"design/backpage.png")
    images["nextquestion"] = ImageTk.PhotoImage(file = f"design/nextquestion.png")
