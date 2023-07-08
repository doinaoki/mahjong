import tkinter as tk
from . import Image
import generate_mahjong.mahjong as gmm
from . import Question
from . import SelectQuestion
from . import SettingInformation

class QuestionSetting():

    def piece_clicked(self, radio_value):
        print(radio_value.get())

    def confilm_setting_clicked(self, canvas, root, radio_value, check_value):
        canvas.delete("all")
        canvas.place_forget()
        setting = self.normal_setting_information(radio_value, check_value)
        q = Question.question()
        q.generate_question(setting)
        q.show_question(canvas, root)

    def tenpai_clicked(self, c):
        print(f"value = {c.get()} ckeck_button_clicked")

    def backb_clicked(self, canvas, root):
        canvas.delete("all")
        canvas.place_forget()
        SelectQuestion.select_question(canvas, root)
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
        piece7 = Image.images["piece7"]
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
        
        piece10 = Image.images["piece10"]
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
        
        piece13 = Image.images["piece13"]
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
            image = Image.images["tenpai"],
            command = lambda:self.tenpai_clicked(check_value1),
            variable = check_value1,
            indicatoron = False
        )
        tenpai.place(
            x = 315, y = 326,
            width = 155,
            height = 35)


        button2 = Image.images["button2"]
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
        
        backpage = Image.images["backpage"]
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
        

    class normal_setting_information(SettingInformation.setting_information):
        def __init__(self, number_piece, is_tenpai):
            super().__init__(number_piece, is_tenpai)
        
        #Override
        def back_question(self, root, canvas, setting, correct):
            q = QuestionSetting()
            q.question_setting(canvas, root)
            print("back")
        
        #Override
        def again_question(self, root, canvas, setting, correct):
            q = Question.question()
            q.generate_question(setting)
            q.show_question(canvas, root)
            print("again")