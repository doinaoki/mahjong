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
             
    def btn1_clicked(self, canvas, root, wait_piece_answer, question, yaku):
        canvas.place_forget()
        result.result(canvas, root, wait_piece_answer, question, yaku, self.this_question)
        

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


    def question(self, canvas, root, piece, check_value, this_question):
        self.this_question = this_question
        self.piece = piece
        self.check_value = check_value
        self.question0(canvas, root)


    def question0(self, canvas, root):
        new_canvas = tk.Canvas(
            root,
            bg = "#000000",
            height = 630,
            width = 1003,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        new_canvas.place(x = 0, y = 0)
        g = gmm.mahjong(self.check_value, self.piece)
        question, yaku = g.generate_question()
        print(question, yaku)
        self.show_piece(question, new_canvas)

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
            command = lambda:self.btn1_clicked(new_canvas, root, wait_piece_answer.get(), question, yaku),
            relief = "flat")
        b1.place(
            x = 385, y = 426,
            width = 202,
            height = 35)