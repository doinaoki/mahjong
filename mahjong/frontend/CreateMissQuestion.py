import tkinter as tk
from . import Image
import generate_mahjong.tenpaiCheck as gmt
import generate_mahjong.yakuCheck as gmy
import ast
from . import ListMissQuestion
from . import DrawFigure

class CreateMissQuestion:
    def show_piece(self):
        self.canvas.delete("all")
        s = ["pin1", "pin2", "pin3", "pin4", "pin5", "pin6", "pin7", "pin8", "pin9"]
        t = 1
        for i in range(len(self.input_pieces)):
            p = s[i]
            for k in range(self.input_pieces[i]):
                pin = Image.images[p]
                piece = self.canvas.create_image(
                    150+50*t, 350.0,
                    image=pin)
                t += 1
        return

    def create_piece_clicked(self, event):
        if sum(self.input_pieces) < 13:
            if self.input_pieces[event.widget.cget("text")] < 4:
                self.input_pieces[event.widget.cget("text")] += 1
        self.show_piece()

    def delete_piece_clicked(self, event):
        if sum(self.input_pieces) > 0:
            if self.input_pieces[event.widget.cget("text")] > 0:
                self.input_pieces[event.widget.cget("text")] -= 1
        self.show_piece()


    def create_button_pieces(self):
        self.now_button = []
        s = ["pin1", "pin2", "pin3", "pin4", "pin5", "pin6", "pin7", "pin8", "pin9"]

        for k in range(9):
            b = tk.Button(
                self.root,
                text = k,
                image = Image.images[s[k]],
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")
            b.place(
                x = 40+50*k, y = 150.0)
            b.bind("<ButtonPress>", self.create_piece_clicked)
            self.now_button.append(b)
        label = DrawFigure.draw_label(self.root, "入力ボタン", ("MSゴシック", "20", "bold"), 40, 90)
        return
    
    def delete_button_pieces(self):
        self.now_button = []
        s = ["pin1", "pin2", "pin3", "pin4", "pin5", "pin6", "pin7", "pin8", "pin9"]

        for k in range(9):
            b = tk.Button(
                self.root,
                text = k,
                image = Image.images[s[k]],
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")
            b.place(
                x = 530+50*k, y = 150.0)
            b.bind("<ButtonPress>", self.delete_piece_clicked)
            self.now_button.append(b)
        
        label = DrawFigure.draw_label(self.root, "削除ボタン", ("MSゴシック", "20", "bold"), 530, 90)
        return

    def create_button_clicked(self):
        input_length = sum(self.input_pieces)
        if input_length != 7 and input_length != 10 and input_length != 13:
            label = tk.Label(
                self.root,
                text = "入力が正確ではありません",
                font=("MSゴシック", "20", "bold"),
                bg = "#F5F5F5",
                relief = "ridge",
                foreground='red'
            )
            label.place(x=330, y=490)
            return
        question = self.input_pieces
        agari = gmt.check(question, input_length)
        yakus = gmy.check(question, agari)
        with open("../miss_question.txt", 'a' ) as ms:
            ms.write(f"{question}:")
            ms.write(f"{yakus}:")
            ms.write("\n")
        self.back_button_clicked()
        


    def back_button_clicked(self):
        self.canvas.delete("all")
        self.canvas.place_forget()
        for i in self.now_button:
            i.destroy()
        for i in self.widgits:
            i.destroy()
        lmq = ListMissQuestion.ListMissQuestion()
        lmq.show_list(self.canvas, self.root)

    def create(self, canvas, root):
        self.widgits = []
        new_canvas = tk.Canvas(
            root,
            bg = "#F5F5F5",
            height = 630,
            width = 1003,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        new_canvas.place(x = 0, y = 0)
        self.canvas = new_canvas
        self.root = root
        self.input_pieces = [0 for i in range(9)]
        

        create_question = tk.Button(
            image = Image.images["createbutton"],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.create_button_clicked(),
            relief = "flat",
            background="#F2F0F0")
        create_question.place(
            x = 800, y = 558,
            width = 170,
            height = 43)
        self.widgits.append(create_question)
        
        backpage = Image.images["missbackpage"]
        backb = tk.Button(
            image = backpage,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.back_button_clicked(),
            relief = "flat",
            background="#F2F0F0")
        backb.place(
            x = 11, y = 558,
            width = 170,
            height = 43)
        self.widgits.append(backb)
        
        self.create_button_pieces()
        self.delete_button_pieces()