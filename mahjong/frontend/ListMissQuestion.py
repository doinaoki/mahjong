import tkinter as tk
from . import Image
import generate_mahjong.mahjong as gmm
from . import QuestionSetting
from . import Home
import ast

class ListMissQuestion:
    def show_list(self, canvas, root):
        with open("../miss_question.txt", 'r' ) as ms:
            miss_questions = ms.read()
        
        miss_list = []
        for i in miss_questions.split("\n"):
            miss = []
            for k in i.split(":"):
                if len(k) != 0 and k[0] == "[":
                    miss.append(ast.literal_eval(k))
                if k == "Y":
                    miss = []
            if miss != []:
                miss_list.append(miss)
        print(miss_list)

        new_canvas = tk.Canvas(
            root,
            bg = "#000000",
            height = 630,
            width = 1003,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        new_canvas.place(x = 0, y = 0)
