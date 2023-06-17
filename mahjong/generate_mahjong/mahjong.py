import logging
from . import generate


class mahjong:
    def __init__(self):
        try:
            self.is_tenpai = bool(int(input("tenpai?")))
            self.number_mahjong = int(input("麻雀牌の数は?"))
            if self.number_mahjong not in [7,10,13]:
                logging.error("generate_mahjong.mahjong.mahjong 麻雀牌の数がただしくありません")
        except ValueError as e:
            print("ERROR generate_mahjong.mahjong.mahjong")
            print(e)
    
    def generate_question(self):
        question = generate.generate(self.is_tenpai, self.number_mahjong)
        question.generate_question()

