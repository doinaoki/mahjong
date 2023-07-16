import tkinter as tk
from . import Image
import generate_mahjong.tenpaiCheck as gmt
import generate_mahjong.yakuCheck as gmy
import ast
from . import ListMissQuestion

class CreateMissQuestion:

    def create_button_clicked(self, input_pieces):
        #print(input_pieces.get())
        input_length = len(input_pieces.get())
        if input_length != 7 and input_length != 10 and input_length != 13:
            return
        question = [0 for _ in range(9)]
        pieces = [int(i) for i in input_pieces.get()]
        for i in pieces:
            question[i-1] += 1
        agari = gmt.check(question, input_length)
        yakus = gmy.check(question, agari)
        with open("../miss_question.txt", 'a' ) as ms:
            ms.write(f"{question}:")
            ms.write(f"{yakus}:")
            ms.write("\n")
        


    def back_button_clicked(self):
        self.canvas.delete("all")
        self.canvas.place_forget()
        '''
        with open("../miss_question.txt", 'a' ) as ms:
            for k in self.miss_list:
                ms.write(f"{k[0]}:")
                ms.write(f"{k[1]}:")
                ms.write("\n")
        '''
        lmq = ListMissQuestion.ListMissQuestion()
        lmq.show_list(self.canvas, self.root)
        print("back")

    def create(self, canvas, root):

        new_canvas = tk.Canvas(
            root,
            bg = "#000000",
            height = 630,
            width = 1003,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        new_canvas.place(x = 0, y = 0)
        self.canvas = new_canvas
        self.root = root

        label = tk.Label(
            root,
            text = "入力",
            font=("MSゴシック", "20", "bold"),
            bg = "#F5F5F5"
        )
        label.place(x=270, y=250)

        input_pieces = tk.StringVar()
        entry = tk.Entry(
            root,
            textvariable=input_pieces,
            width=300,
            font=("MSゴシック", "30", "bold")
        )
        entry.place(
            x = 370, y = 250,
            width = 300,
            height = 50)
        
        backpage = Image.images["createbutton"]
        backb = tk.Button(
            image = backpage,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.create_button_clicked(input_pieces),
            relief = "flat",
            background="#F2F0F0")
        backb.place(
            x = 800, y = 558,
            width = 170,
            height = 43)
        
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