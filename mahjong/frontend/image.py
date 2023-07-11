import tkinter as tk

images = {}

def image():

    images["background"] = tk.PhotoImage(file = "design\\back_ground.png")
    images["button1"] = tk.PhotoImage(file = f"design\\button1.png")
    images["button2"] = tk.PhotoImage(file = f"design\\button2.png")
    images["button3"] = tk.PhotoImage(file = f"design\\button3.png")

    #setting_page

    images["settingbackground"] = tk.PhotoImage(file = f"design\\setting_background.png")

    images["piece7"] = tk.PhotoImage(file = f"design\\7piece.png")
    images["piece10"] = tk.PhotoImage(file = f"design\\10_piece.png")
    images["piece13"] = tk.PhotoImage(file = f"design\\13_piece.png")

    images["pin1"] = tk.PhotoImage(file = f"design\\1pin.png").subsample(2,2)
    images["pin2"] = tk.PhotoImage(file = f"design\\2pin.png").subsample(2,2)
    images["pin3"] = tk.PhotoImage(file = f"design\\3pin.png").subsample(2,2)
    images["pin4"] = tk.PhotoImage(file = f"design\\4pin.png").subsample(2,2)
    images["pin5"] = tk.PhotoImage(file = f"design\\5pin.png").subsample(2,2)
    images["pin6"] = tk.PhotoImage(file = f"design\\6pin.png").subsample(2,2)
    images["pin7"] = tk.PhotoImage(file = f"design\\7pin.png").subsample(2,2)
    images["pin8"] = tk.PhotoImage(file = f"design\\8pin.png").subsample(2,2)
    images["pin9"] = tk.PhotoImage(file = f"design\\9pin.png").subsample(2,2)

    images["Ntenpai"] = tk.PhotoImage(file = f"design\\Ntenpai.png")
    images["Ytenpai"] = tk.PhotoImage(file = f"design\\Ytenpai.png")

    images["normal"] = tk.PhotoImage(file = f"design\\normal.png")
    images["difficult"] = tk.PhotoImage(file = f"design\\difficult.png")
    images["random"] = tk.PhotoImage(file = f"design\\random.png")

    images["startbutton"] = tk.PhotoImage(file = f"design\\start_button.png")
    images["backbutton"] = tk.PhotoImage(file = f"design\\back_button.png")

    #question_page

    images["backpage"] = tk.PhotoImage(file = f"design\\backpage.png")
    images["nextquestion"] = tk.PhotoImage(file = f"design\\nextquestion.png")
