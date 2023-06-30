import tkinter as tk
from . import image
import generate_mahjong.mahjong as gmm
from . import result

def check_answer(wait_piece_answer, yaku):
    answer_piece = []
    for i in yaku:
        answer_piece.append(i[0]+1)
    answer_piece = sorted(list(set(answer_piece)))
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
    

def result(canvas, root, wait_piece_answer, question, yaku):
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