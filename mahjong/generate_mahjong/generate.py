import random
import math
from . import tenpaiCheck

class generate:
    def __init__(self, tenpai, number_mahjong):
        self.is_tenpai = tenpai
        self.number_mahjong = number_mahjong

    def generate_question(self):
        while True:
            question = self.generate_piece()
            print(question)
            yaku = tenpaiCheck.check(question, self.number_mahjong)
            if len(yaku) > 0 or not self.is_tenpai:
                print(yaku)
                break
        return question,yaku
                

    def generate_piece(self):
        piece_array = [0 for _ in range(9)]
        i = 0
        while i < self.number_mahjong:
            piece_value = math.ceil(random.random()*9)
            if piece_array[piece_value-1] <= 3:
                piece_array[piece_value-1] += 1
                i += 1
        return piece_array