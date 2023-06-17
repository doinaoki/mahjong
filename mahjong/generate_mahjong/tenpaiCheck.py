import copy

def check(piece_array, number_mahjong):
    tenpai = [False for _ in range(9)]
    #聴牌確認
    for i in range(9):
        if piece_array[i] != 4:
            piece_array[i] += 1
            # 雀頭決定 
            if head(copy.deepcopy(piece_array), number_mahjong+1):
                tenpai[i] = True
            piece_array[i] -= 1
    return tenpai

def head(piece_array, number_mahjong):
    piece_array = piece_array
    for i in range(9):
        if piece_array[i] >= 2:
            piece_array[i] -= 2
            if set(piece_array, number_mahjong-2):
                return True
            piece_array[i] += 2


def set(piece_array, number_mahjong):
    if number_mahjong == 0:
        return True
    else:
        i = 0
        while piece_array[i] == 0:
            i += 1
        
        is_set = False
        #順子
        if i <= 6 and piece_array[i+1] >= 1 and piece_array[i+2] >= 1:
            piece_array[i] -= 1
            piece_array[i+1] -= 1
            piece_array[i+2] -= 1
            if set(piece_array, number_mahjong-3):
                return True
            piece_array[i] += 1
            piece_array[i+1] += 1
            piece_array[i+2] += 1
            is_set = True

        #暗刻
        if piece_array[i] >= 3:
            piece_array[i] -= 3
            if set(piece_array, number_mahjong-3):
                return True

            piece_array[i] += 3
            is_set = True

        if not is_set:
            return False

