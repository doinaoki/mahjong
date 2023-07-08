import tkinter as tk
from . import image
import generate_mahjong.mahjong as gmm
from . import result

class question:
    '''
    def check_answer(self, wait_piece_answer, yaku):
        print(wait_piece_answer)
        if wait_piece_answer != []:
            answer_piece = []
            for i in yaku:
                answer_piece.append(i[0]+1)
            answer_piece = sorted(list(set(answer_piece)))
            wait_piece_answer = sorted([int(i) for i in wait_piece_answer.split(",")])
            if answer_piece == wait_piece_answer:
                print("正解!")
            else:
                print("不正解")
        else:
            print("入力しろ")
    '''

    #field
    #question
    #yaku
    #setting
             
    def confilm_answer_clicked(self, canvas, root, wait_piece_answer):
        canvas.delete("all")
        canvas.place_forget()
        result.result(canvas, root, wait_piece_answer, self.question, self.yaku, self.setting)
        

    def show_piece(sef, question, canvas):
        s = ["pin1", "pin2", "pin3", "pin4", "pin5", "pin6", "pin7", "pin8", "pin9"]
        t = 1
        for i in range(len(question)):
            p = s[i]
            for k in range(question[i]):
                pin = image.images[p]
                canvas.create_image(
                    64+59*t, 160.0,
                    image=pin)
                t += 1
    
        return

    def generate_question(self, setting):
        g = gmm.mahjong(setting.is_tenpai, setting.number_piece)
        question, yaku = g.generate_question()
        self.question = question
        self.yaku = yaku
        self.setting = setting

    def register_question(self, question, yaku, setting):
        self.question = question
        self.yaku = yaku
        self.setting = setting

    def show_question(self, canvas, root):
        print(self.question, self.yaku)

        new_canvas = tk.Canvas(
            root,
            bg = "#000000",
            height = 630,
            width = 1003,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        new_canvas.place(x = 0, y = 0)
        self.show_piece(self.question, new_canvas)

        wait_piece_answer = tk.StringVar()
        entry = tk.Entry(
            root,
            textvariable=wait_piece_answer,
            width=100
        )
        entry.place(
            x = 200, y = 326,
            width = 100,
            height = 35)

        button3 = image.images["button3"]
        b1 = tk.Button(
            image = button3,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.confilm_answer_clicked(new_canvas, root, wait_piece_answer.get()),
            relief = "flat")
        b1.place(
            x = 385, y = 426,
            width = 202,
            height = 35)