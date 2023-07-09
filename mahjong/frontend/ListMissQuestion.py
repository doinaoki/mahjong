import tkinter as tk
from . import Image
import generate_mahjong.mahjong as gmm
from . import QuestionSetting
from . import Home
import ast

class ListMissQuestion:

    #field
    #now_page_number = 現在表示のページ数
    #miss_list = ミスった問題集
    #canvas
    #root
    #now_button

    def delete_button_clicked(self, event):
        print(event.widget.cget("text"))
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
        print("delete")


    def page_button_clicked(self, event):
        self.now_page_number = event.widget.cget("text")
        self.canvas.delete("all")
        for i in self.now_button:
            i.destroy()
        self.show_piece()


    def show_page(self):
        self.page_buttons = []
        miss_list_size = len(self.miss_list)
        miss_pages = miss_list_size // 5 + 1
        for i in range(miss_pages):
            button = tk.Button(
                self.root,
                text = i+1,
                font=("MSゴシック", "20", "bold")
            )
            button.bind("<ButtonPress>", self.page_button_clicked)
            button.place(
                x = i*60 + 60, y = 530,
                width = 50,
                height = 50)
            self.page_buttons.append(button)
        return

    def show_piece(self):
        self.now_button = []
        s = ["pin1", "pin2", "pin3", "pin4", "pin5", "pin6", "pin7", "pin8", "pin9"]
        for c in range((self.now_page_number-1)*5, min(len(self.miss_list), (self.now_page_number)*5)):
            question = self.miss_list[c][0]
            cc = c % 5
            t = 1
            for i in range(len(question)):
                p = s[i]
                for k in range(question[i]):
                    pin = Image.images[p]
                    self.canvas.create_image(
                        40+59*t, 100*cc + 60,
                        image=pin)
                    t += 1
            b = tk.Button(
                self.root,
                text = c,
                image = Image.images["button3"],
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")
            b.place(
                x = 800, y = 100*cc + 60,
                width = 202,
                height = 35)
            b.bind("<ButtonPress>", self.delete_button_clicked)
            self.now_button.append(b)

        print("show")

    def show_list(self, canvas, root):
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
        #print(self.miss_list)

        new_canvas = tk.Canvas(
            root,
            bg = "#000000",
            height = 630,
            width = 1003,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        new_canvas.place(x = 0, y = 0)

        self.now_page_number = 1
        self.canvas = new_canvas
        self.root = root
        self.show_page()
        self.show_piece()