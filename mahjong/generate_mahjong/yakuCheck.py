

def check(question, agari):
    if sum(question) <= 12:
        yakus = []
        for i in agari:
            yakus.append([i[0][0], 0, []])
        return yakus
    #[[上がり牌, 面子, 待ち, 順子数, 暗刻数]]
    sets_info = []
    for i in agari:
        win_tile = i[0][0]
        sets = i[1:]
        w = wait_tile(win_tile,sets)
        chow = count_chow(sets)
        pung = 4 - chow
        sets_info.append([win_tile, sets, w, chow, pung])
    return yaku(sets_info)
    
def wait_tile(win_tile, sets):
    #カンチャン,シャンポン,単騎,両面
    wait_string = ["両面", "単騎", "カンチャン", "ペンチャン", "シャンポン"]
    wait_array = [False,False,False,False,False]
    print(win_tile)
    for set in sets:
        if len(set) == 2 and win_tile in set:
            wait_array[1] = True
        elif win_tile in set and set[0] == set[1]:
            wait_array[4] = True
        elif win_tile in set and set[1] == win_tile:
            wait_array[2] = True
        elif win_tile in set and (win_tile == 6 and set[0] == 7):
            wait_array[3] = True
        elif win_tile in set and (win_tile == 2 and set[2] == 3):
            wait_array[3] = True
        elif win_tile in set:
            wait_array[0] = True
    
    for i in range(len(wait_array)):
        if wait_array[i] :
            return wait_string[i]
    

def count_chow(sets):
    count = 0
    for set in sets:
        if set[0] != set[1]:
            count += 1
    return count

def arrangement(yakus):
    new_yakus = []
    for i in range(9):
        maxhan = 0
        y = []
        for yaku in yakus:
            agari_piece = yaku[0]
            han = yaku[1]
            if agari_piece != i:
                continue
            if maxhan < han:
                y = yaku
                maxhan = han
        if maxhan != 0:
            new_yakus.append(y)
    return new_yakus

def yaku(sets_info):
    yakus = []
    for set_info in sets_info:
        yaku_array = ["清一色"]
        han = 6
        if set_info[4] == 4:
            if set_info[2] == "単騎":
                yaku_array.append("四暗刻単騎")
            else:
                yaku_array.append("四暗刻")
            han += 100
        if set_info[4] == 3:
            yaku_array.append("三暗刻")
            yaku_array.append("対々和")
            han += 4
        if set_info[4] == 0 and set_info[2] == "両面":
            yaku_array.append("平和")
            han += 1
        for i in range(len(set_info[1])):
            if 0 in set_info[1][i] or 8 in set_info[1][i]:
                break
            if i == 3:
                yaku_array.append("タンヤオ")
                han += 1
        a = [0 for _ in range(9)]
        iipeekoo = False
        ryanpeekoo = False
        for i in set_info[1]:
            if i[0] != i[1]:
                a[i[0]] += 1
        
        for i in a:
            if i >= 2 and iipeekoo:
                ryanpeekoo = True
                iipeekoo = False
            elif i >= 2:
                iipeekoo = True
            
        if iipeekoo:
            yaku_array.append("一盃口")
            han += 1
        if ryanpeekoo:
            yaku_array.append("二盃口")
            han += 3
        if [0,1,2] in set_info[1] and [3,4,5] in set_info[1] and [6,7,8] in set_info[1]:
            yaku_array.append("一気通貫")
            han += 2
        
        yakus.append([set_info[0], han, yaku_array]) 
        yakus = arrangement(yakus)
    return yakus
            
