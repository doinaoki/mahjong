import tkinter as tk
from . import Image
import generate_mahjong.mahjong as gmm
from . import SelectQuestion
from . import Home
import ast
from . import MissResult
from . import CreateMissQuestion

class ListMissQuestion:

    #field
    #now_page_number = 現在表示のページ数
    #miss_list = ミスった問題集
    #canvas
    #root
    #now_button

    def delete_button_clicked(self, event):
        self.miss_list.pop(event.widget.cget("text"))
        self.now_page_number = 1
        self.canvas.delete("all")
        for i in self.now_button:
            i.destroy()
        for i in self.page_buttons:
            i.destroy()
        with open("../miss_question.txt", 'w' ) as ms:
            for k in self.miss_list:
                ms.write(f"{k[0]}:")
                ms.write(f"{k[1]}:")
                ms.write("\n")
        self.canvas.place_forget()
        self.show_list(self.canvas, self.root)


    def page_button_clicked(self, event):
        self.now_page_number = event.widget.cget("text")
        self.canvas.delete("all")
        for i in self.now_button:
            i.destroy()
        miss_background = self.canvas.create_image(
            506.5, 313.0,
            image=Image.images["missbackground"])
        self.show_piece()

    def back_button_clicked(self):
        self.canvas.delete("all")
        self.canvas.place_forget()
        for i in self.now_button:
            i.destroy()
        SelectQuestion.select_question(self.canvas, self.root)


    def answer_button_clicked(self, event):
        self.canvas.delete("all")
        self.canvas.place_forget()
        question = self.miss_list[event.widget.cget("text")][0]
        yaku = self.miss_list[event.widget.cget("text")][1]
        for i in self.now_button:
            i.destroy()
        for i in self.page_buttons:
            i.destroy()
        MissResult.miss_result(self.canvas, self.root, question, yaku)

    def create_button_clicked(self):
        self.canvas.delete("all")
        for i in self.now_button:
            i.destroy()
        for i in self.page_buttons:
            i.destroy()
        self.canvas.place_forget()
        cmq = CreateMissQuestion.CreateMissQuestion()
        cmq.create(self.canvas, self.root)
        
        

    def show_page(self):
        self.page_buttons = []
        miss_list_size = len(self.miss_list)
        miss_pages = (miss_list_size - 1) // self.show_page_piece + 1
        for i in range(miss_pages):
            button = tk.Button(
                self.root,
                text = i+1,
                font=("MSゴシック", "20", "bold")
            )
            button.bind("<ButtonPress>", self.page_button_clicked)
            button.place(
                x = i*60 + 100, y = 500,
                width = 45,
                height = 45)
            self.page_buttons.append(button)
        return

    def show_piece(self):
        self.now_button = []
        s = ["pin1", "pin2", "pin3", "pin4", "pin5", "pin6", "pin7", "pin8", "pin9"]
        for c in range((self.now_page_number-1)*self.show_page_piece, min(len(self.miss_list), (self.now_page_number)*self.show_page_piece)):
            question = self.miss_list[c][0]
            cc = c % self.show_page_piece
            t = 1
            for i in range(len(question)):
                p = s[i]
                for k in range(question[i]):
                    pin = Image.images[p]
                    self.canvas.create_image(
                        40+50*t, 120*cc + 70,
                        image=pin)
                    t += 1

            b = tk.Button(
                self.root,
                text = c,
                image = Image.images["deletebutton"],
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")
            b.place(
                x = 777, y = 120*cc + 70,
                width = 184,
                height = 38)
            b.bind("<ButtonPress>", self.delete_button_clicked)
            self.now_button.append(b)

            b = tk.Button(
                self.root,
                text = c,
                image = Image.images["answerbutton"],
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")
            b.place(
                x = 777, y = 120*cc + 27,
                width = 184,
                height = 38)
            b.bind("<ButtonPress>", self.answer_button_clicked)
            self.now_button.append(b)


    def show_list(self, canvas, root):
        self.show_page_piece = 4
        with open("../miss_question.txt", 'r' ) as ms:
            miss_questions = ms.read()
        
        self.miss_list = []
        for i in miss_questions.split("\n"):
            miss = []
            for k in i.split(":"):
                if len(k) != 0 and k[0] == "[":
                    miss.append(ast.literal_eval(k))
            if miss != []:
                self.miss_list.append(miss)

        new_canvas = tk.Canvas(
            root,
            bg = "#000000",
            height = 630,
            width = 1003,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        new_canvas.place(x = 0, y = 0)
        miss_background = new_canvas.create_image(
            506.5, 313.0,
            image=Image.images["missbackground"])

        self.now_page_number = 1
        self.canvas = new_canvas
        self.root = root
        self.show_page()
        self.show_piece()

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
        
        backpage = Image.images["createbutton"]
        backb = tk.Button(
            image = backpage,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.create_button_clicked(),
            relief = "flat",
            background="#F2F0F0")
        backb.place(
            x = 800, y = 558,
            width = 170,
            height = 43)
