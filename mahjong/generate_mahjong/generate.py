import random
import math
from . import tenpaiCheck

class generate:
    def __init__(self, tenpai, number_mahjong, difficulty):
        self.is_tenpai = tenpai
        self.number_mahjong = number_mahjong
        self.difficulty = difficulty

    def generate_question(self):
        while True:
            question = self.generate_piece()
            #print(question)
            agari = tenpaiCheck.check(question, self.number_mahjong)
            number_of_agari = 0
            for k in range(9):
                for i in agari:
                    if i[0][0] == k:
                        number_of_agari += 1
                        break
            print(f"{number_of_agari}面張")
            if not self.is_tenpai:
                break
            elif self.difficulty == 0:
                if number_of_agari <= 2 and number_of_agari > 0:
                    break
            elif self.difficulty == 1:
                if number_of_agari > 2:
                    break
            elif self.difficulty == 2:
                if number_of_agari > 0:
                    break


            #if number_of_agari > self.difficulty or not self.is_tenpai:
                #break
        return question,agari
                

    def generate_piece(self):
        piece_array = [0 for _ in range(9)]
        i = 0
        while i < self.number_mahjong:
            piece_value = math.ceil(random.random()*9)
            if piece_array[piece_value-1] <= 3:
                piece_array[piece_value-1] += 1
                i += 1
        return piece_array