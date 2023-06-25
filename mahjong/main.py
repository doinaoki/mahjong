import generate_mahjong.mahjong as gmm
import os
import sys
import frontend.home as fh
sys.path.append('../')
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def btn_clicked():
    print("Button Clicked")

if __name__ == "__main__":
    fh.home()
    '''
    mh = gmm.mahjong()
    question, yaku = mh.generate_question()
    print(question, yaku)
    question, yaku = mh.generate_question()
    print(question, yaku)
    '''
