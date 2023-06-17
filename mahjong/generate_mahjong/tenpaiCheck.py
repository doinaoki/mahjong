import copy
def check(piece_array, number_mahjong):
    agari = []
    for i in range(9):
        if piece_array[i] != 4:
            piece_array[i] += 1
            head(copy.deepcopy(piece_array), number_mahjong+1, [[i]],agari)
            piece_array[i] -= 1
    return agari

def head(piece_array, number_mahjong, agari_array,agari):
    for i in range(9):
        if piece_array[i] >= 2:
            piece_array[i] -= 2
            set(piece_array, number_mahjong-2, agari_array + [[i, i]],agari)
            piece_array[i] += 2


def set(piece_array, number_mahjong, agari_array,agari):
    if number_mahjong == 0:
        agari.append(agari_array)
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
            set(piece_array, number_mahjong-3, agari_array+[[i,i+1,i+2]],agari)
            piece_array[i] += 1
            piece_array[i+1] += 1
            piece_array[i+2] += 1
            is_set = True

        #暗刻
        if piece_array[i] >= 3:
            piece_array[i] -= 3
            set(piece_array, number_mahjong-3,agari_array+[[i,i,i]],agari)
            piece_array[i] += 3
            is_set = True

        if not is_set:
            return False
