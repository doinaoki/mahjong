import tkinter as tk
from . import Image
import generate_mahjong.mahjong as gmm
from . import Question
from . import SelectQuestion
from . import SettingInformation

class QuestionSetting():

    def piece_clicked(self, radio_value):
        pass

    def confilm_setting_clicked(self, canvas, root, radio_value, check_value, difficulty):
        canvas.delete("all")
        canvas.place_forget()
        for i in self.widgits:
            i.destroy()
        self.widgits = []
        setting = self.normal_setting_information(radio_value, check_value, difficulty)
        q = Question.question()
        q.generate_question(setting, difficulty)
        q.show_question(canvas, root)

    def tenpai_clicked(self, c):
        pass

    def backb_clicked(self, canvas, root):
        canvas.delete("all")
        canvas.place_forget()
        for i in self.widgits:
            i.destroy()
        self.widgits = []
        SelectQuestion.select_question(canvas, root)

    def question_setting(self, canvas, root):
        self.widgits = []
        new_canvas = tk.Canvas(
            root,
            bg = "#ffffff",
            height = 630,
            width = 1003,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        new_canvas.create_image(
            506.5, 313.0,
            image=Image.images["settingbackground"])
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
            x = 447, y = 190,
            width = 140,
            height = 46)
        
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
            x = 585, y = 190,
            width = 137,
            height = 46)
        
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
            x = 713, y = 190,
            width = 124,
            height = 46)
        self.widgits.append(p7)
        self.widgits.append(p10)
        self.widgits.append(p13)
        
        

        tenpai_value = tk.BooleanVar(value = True)
        Yes_tenpai = tk.Radiobutton(
            root,
            image = Image.images["Ytenpai"],
            command = lambda:self.tenpai_clicked(tenpai_value),
            value = True,
            variable = tenpai_value,
            indicatoron = False
        )
        Yes_tenpai.place(
            x = 447, y = 296,
            width = 145,
            height = 48)
        
        No_tenpai = tk.Radiobutton(
            root,
            image = Image.images["Ntenpai"],
            command = lambda:self.tenpai_clicked(tenpai_value),
            value = False,
            variable = tenpai_value,
            indicatoron = False
        )
        No_tenpai.place(
            x = 592, y = 296,
            width = 145,
            height = 48)
        self.widgits.append(Yes_tenpai)
        self.widgits.append(No_tenpai)


        difficulty_value = tk.IntVar(value = 0)
        normal = tk.Radiobutton(
            root,
            image = Image.images["normal"],
            command = lambda:self.tenpai_clicked(difficulty_value),
            value = 0,
            variable = difficulty_value,
            indicatoron = False
        )
        normal.place(
            x = 447, y = 399,
            width = 145,
            height = 46)
        
        difficult = tk.Radiobutton(
            root,
            image = Image.images["difficult"],
            command = lambda:self.tenpai_clicked(difficulty_value),
            value = 1,
            variable = difficulty_value,
            indicatoron = False
        )
        difficult.place(
            x = 585, y = 399,
            width = 145,
            height = 48)
        
        random = tk.Radiobutton(
            root,
            image = Image.images["random"],
            command = lambda:self.tenpai_clicked(difficulty_value),
            value = 2,
            variable = difficulty_value,
            indicatoron = False
        )
        random.place(
            x = 713, y = 399,
            width = 145,
            height = 48)
        self.widgits.append(normal)
        self.widgits.append(difficult)
        self.widgits.append(random)


        start_button = tk.Button(
            image = Image.images["startbutton"],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.confilm_setting_clicked(new_canvas, root, radio_value.get(), tenpai_value.get(), difficulty_value.get()),
            relief = "flat")
        start_button.place(
            x = 400, y = 540,
            width = 204,
            height = 49)
        
        backpage = Image.images["backbutton"]
        backb = tk.Button(
            image = backpage,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.backb_clicked(new_canvas, root),
            relief = "flat")
        backb.place(
            x = 5, y = 577,
            width = 146,
            height = 47)
        self.widgits.append(start_button)
        self.widgits.append(backb)
        

    class normal_setting_information(SettingInformation.setting_information):
        def __init__(self, number_piece, is_tenpai, difficulty):
            super().__init__(number_piece, is_tenpai, difficulty)
        
        #Override
        def back_question(self, root, canvas, setting, correct):
            q = QuestionSetting()
            q.question_setting(canvas, root)
        
        #Override
        def again_question(self, root, canvas, setting, correct):
            q = Question.question()
            q.generate_question(setting, self.difficulty)
            q.show_question(canvas, root)
        