import tkinter as tk
from . import Image
from . import ListMissQuestion
from . import DrawFigure

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

def back_button_clicked(canvas, root):
    canvas.delete("all")
    canvas.place_forget()
    l = ListMissQuestion.ListMissQuestion()
    l.show_list(canvas, root)
    print("back")

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
'''
def show_result_pieces(root, canvas, yaku):
    s = ["pin1", "pin2", "pin3", "pin4", "pin5", "pin6", "pin7", "pin8", "pin9"]
    places = [[210, 264],[568,264],[210, 358],[568,358],[210,452],[568,452],[210,546],[568,546]]
    for i in range(len(yaku)):
        agari = yaku[i]
        win_piece = agari[0]
        yaku_list = agari[2]
        place = places[i]

        pin = Image.images[s[win_piece]]
        canvas.create_image(
            place[0], place[1],
            image=pin)
'''
            
def miss_result (canvas, root, question, yaku):
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

    backpage = Image.images["missbackpage"]
    backb = tk.Button(
        image = backpage,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:back_button_clicked(new_canvas, root),
        relief = "flat",
        background="#F2F0F0")
    backb.place(
        x = 11, y = 558,
        width = 170,
        height = 43)