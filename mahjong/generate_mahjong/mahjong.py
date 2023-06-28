import logging
from . import generate
from . import yakuCheck
import sys

class mahjong:
    def __init__(self, is_tenpai, number_mahjong):
        try:
            self.is_tenpai = is_tenpai
            self.number_mahjong = number_mahjong
            if self.number_mahjong not in [7,10,13]:
                logging.error("generate_mahjong.mahjong.mahjong 麻雀牌の数がただしくありません")
                sys.exit()

        except ValueError as e:
            print("ERROR generate_mahjong.mahjong.mahjong")
            print(e)

    #question = [1の個数, 2の個数, ..., 9の個数]
    #yaku = [[待ち, 飜, 役],[]]
    def generate_question(self):
        gene = generate.generate(self.is_tenpai, self.number_mahjong)
        question, agari = gene.generate_question()
        yaku = yakuCheck.check(question, agari)
        return question, yaku
        

