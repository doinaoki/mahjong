import tkinter as tk
from . import image
import generate_mahjong.mahjong as gmm
from . import question
from . import question_setting

def check_answer(wait_piece_answer, yaku):
    answer_piece = []
    for i in yaku:
        answer_piece.append(i[0]+1)
    answer_piece = sorted(list(set(answer_piece)))
    if wait_piece_answer == "":
        wait_piece_answer = []
    else:
        wait_piece_answer = sorted([int(i) for i in wait_piece_answer.split(",")])
    if answer_piece == wait_piece_answer:
        print("正解")
        return True
    else:
        print("不正解")
        return False


def show_piece(question, canvas):
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

def backb_clicked(canvas, root):
    canvas.place_forget()
    q = question_setting.question_setting()
    q.question_setting(canvas, root)
    print("back")

def nextb_clicked(canvas, root, this_question):
    canvas.place_forget()
    this_question.question0(canvas, root)
    print("next!")

def add_miss_question(question, yaku):
    with open("../miss_question.txt", 'a' ) as ms:
        ms.write(f"{question}:")
        ms.write(f"{yaku}:")
        ms.write(f"N")
        ms.write("\n")


def result (canvas, root, wait_piece_answer, question, yaku, this_question):
    new_canvas = tk.Canvas(
        root,
        bg = "#000000",
        height = 630,
        width = 1003,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    new_canvas.place(x = 0, y = 0)
    show_piece(question, new_canvas)
    correct = check_answer(wait_piece_answer, yaku)

    if correct:
        label = tk.Label(
            root,
            text = "正解",
            font=("MSゴシック", "20", "bold")
        )
    else:
        add_miss_question(question, yaku)
        label = tk.Label(
            root,
            text = "不正解",
            font=("MSゴシック", "20", "bold")
        )
    label.place(x=450, y=350)

    nextquestion = image.images["nextquestion"]
    nextb = tk.Button(
        image = nextquestion,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:nextb_clicked(new_canvas, root, this_question),
        relief = "flat")
    nextb.place(
        x = 770, y = 550,
        width = 202,
        height = 35)
    
    backpage = image.images["backpage"]
    backb = tk.Button(
        image = backpage,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:backb_clicked(new_canvas, root),
        relief = "flat")
    backb.place(
        x = 5, y = 550,
        width = 202,
        height = 35)