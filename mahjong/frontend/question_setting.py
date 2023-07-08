import tkinter as tk
from . import image
import generate_mahjong.mahjong as gmm
from . import question
from . import select_question
from . import setting_information

class question_setting():

    def piece_clicked(self, radio_value):
        print(radio_value.get())

    def confilm_setting_clicked(self, canvas, root, radio_value, check_value):
        canvas.delete("all")
        canvas.place_forget()
        setting = self.normal_setting_information(radio_value, check_value)
        q = question.question()
        q.generate_question(setting)
        q.show_question(canvas, root)

    def tenpai_clicked(self, c):
        print(f"value = {c.get()} ckeck_button_clicked")

    def backb_clicked(self, canvas, root):
        canvas.delete("all")
        canvas.place_forget()
        select_question.select_question(canvas, root)
        print("back")

    def question_setting(self, canvas, root):
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
            command = lambda:self.piece_clicked(radio_value),
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
            command = lambda:self.piece_clicked(radio_value),
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
            command = lambda:self.piece_clicked(radio_value),
            indicatoron = False
        )
        p13.place(
            x = 560, y = 200,
            width = 120,
            height = 40)
        
        
        check_value1 = tk.BooleanVar(value = True)
        tenpai = tk.Checkbutton(
            root,
            image = image.images["tenpai"],
            command = lambda:self.tenpai_clicked(check_value1),
            variable = check_value1,
            indicatoron = False
        )
        tenpai.place(
            x = 315, y = 326,
            width = 155,
            height = 35)


        button2 = image.images["button2"]
        b2 = tk.Button(
            image = button2,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.confilm_setting_clicked(new_canvas, root, radio_value.get(), check_value1.get()),
            relief = "flat")
        b2.place(
            x = 385, y = 426,
            width = 202,
            height = 35)
        
        backpage = image.images["backpage"]
        backb = tk.Button(
            image = backpage,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.backb_clicked(new_canvas, root),
            relief = "flat")
        backb.place(
            x = 5, y = 550,
            width = 202,
            height = 35)
        

    class normal_setting_information(setting_information.setting_information):
        def __init__(self, number_piece, is_tenpai):
            super().__init__(number_piece, is_tenpai)
        
        #Override
        def back_question(self, root, canvas, setting, correct):
            q = question_setting()
            q.question_setting(canvas, root)
            print("back")
        
        #Override
        def again_question(self, root, canvas, setting, correct):
            q = question.question()
            q.generate_question(setting)
            q.show_question(canvas, root)
            print("again")