import tkinter as tk
from . import Image
import generate_mahjong.mahjong as gmm
from . import Question
from . import QuestionSetting
from . import DrawFigure

widgits = []

def check_answer(wait_piece_answer, yaku):
    answer_piece = []
    for i in yaku:
        answer_piece.append(i[0]+1)
    answer_piece = sorted(list(set(answer_piece)))
    if wait_piece_answer == "":
        wait_piece_answer = []
    else:
        wait_piece_answer = sorted([int(i) for i in wait_piece_answer])
    if answer_piece == wait_piece_answer:
        return True
    else:
        return False

def puzzled_button_clicked(check):
    pass

def show_piece(question, canvas):
    s = ["pin1", "pin2", "pin3", "pin4", "pin5", "pin6", "pin7", "pin8", "pin9"]
    t = 1
    for i in range(len(question)):
        p = s[i]
        for k in range(question[i]):
            pin = Image.images[p]
            canvas.create_image(
                89+50*t, 150.0,
                image=pin)
            t += 1
    return

def backb_clicked(canvas, root, this_setting, correct, check_value, question, yaku):
    canvas.delete("all")
    canvas.place_forget()
    for i in widgits:
        i.destroy()
    add_puzzled_question(check_value, question, yaku)
    this_setting.back_question(root, canvas, this_setting, correct)

def nextb_clicked(canvas, root, this_setting, correct, check_value, question, yaku):
    canvas.delete("all")
    canvas.place_forget()
    for i in widgits:
        i.destroy()
    add_puzzled_question(check_value, question, yaku)
    this_setting.again_question(root, canvas, this_setting, correct)

def add_miss_question(question, yaku):
    with open("../miss_question.txt", 'a' ) as ms:
        ms.write(f"{question}:")
        ms.write(f"{yaku}:")
        ms.write("\n")

def add_puzzled_question(check_value, question, yaku):
    if not check_value.get():
        return
    with open("../puzzled_question.txt", 'a' ) as ms:
        ms.write(f"{question}:")
        ms.write(f"{yaku}:")
        ms.write("\n")

def show_result_pieces(root, canvas, yaku):
    s = ["pin1", "pin2", "pin3", "pin4", "pin5", "pin6", "pin7", "pin8", "pin9"]
    piece_places = [[210, 264],[568,264],[210, 358],[568,358],[210,452],[568,452],[210,546],[568,546]]
    yaku_places = [[50,-30],[180,-30],[50,0],[180,0]]
    for i in range(len(yaku)):
        agari = yaku[i]
        win_piece = agari[0]
        yaku_list = agari[2]
        place = piece_places[i]
        pin = Image.images[s[win_piece]]
        canvas.create_image(
            place[0], place[1],
            image=pin)
        
        for k in range(len(yaku_list)):
            yaku_name = yaku_list[k]
            yaku_place = [place[0] + yaku_places[k][0], place[1] + yaku_places[k][1]]
            label = DrawFigure.draw_label(root, yaku_name, ("MSゴシック", "20", "bold"), yaku_place[0], yaku_place[1])



def result (canvas, root, wait_piece_answer, question, yaku, this_setting):
    global widgits
    widgits = []
    new_canvas = tk.Canvas(
        root,
        bg = "#000000",
        height = 630,
        width = 1003,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    new_canvas.place(x = 0, y = 0)
    new_canvas.create_image(
        506.5, 313.0,
        image=Image.images["resultbackground"])
    show_piece(question, new_canvas)
    show_result_pieces(root, new_canvas, yaku)
    correct = check_answer(wait_piece_answer, yaku)

    if correct:
        new_canvas.create_image(
        720, 40,
        image=Image.images["correct"])
    else:
        add_miss_question(question, yaku)
        new_canvas.create_image(
        720, 40,
        image=Image.images["uncorrect"])

    check_value = tk.BooleanVar(value = False)
    puzzledb = tk.Checkbutton(
        image = Image.images["puzzledbutton"],
        borderwidth = 0,
        highlightthickness = 0,
        variable = check_value,
        command = lambda:puzzled_button_clicked(check_value.get()),
        indicatoron = False)
    puzzledb.place(
        x = 420, y = 550,
        width = 166,
        height = 46)


    nextquestion = Image.images["nextquestion"]
    nextb = tk.Button(
        image = nextquestion,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:nextb_clicked(new_canvas, root, this_setting, correct, check_value, question, yaku),
        relief = "flat")
    nextb.place(
        x = 700, y = 550,
        width = 295,
        height = 50)
    
    backpage = Image.images["backpage"]
    backb = tk.Button(
        image = backpage,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:backb_clicked(new_canvas, root, this_setting, correct, check_value, question, yaku),
        relief = "flat")
    backb.place(
        x = 5, y = 550,
        width = 295,
        height = 50)
    
    widgits.append(puzzledb)
    widgits.append(nextb)
    widgits.append(backb)
    
