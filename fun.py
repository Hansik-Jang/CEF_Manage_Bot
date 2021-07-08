def teamNameConvert(name):
    if name == "A" or name == 'a' or name == 'TEAM_A':
        return 'TEAM_A'
    elif name == "B" or name == 'b' or name == 'TEAM_B':
        return 'TEAM_B'
    elif name == "C" or name == 'c' or name == 'TEAM_C':
        return 'TEAM_C'
    elif name == "D" or name == 'd' or name == 'TEAM_D':
        return 'TEAM_D'
    elif name == "E" or name == 'e' or name == 'TEAM_E':
        return 'TEAM_E'
    else:
        return 'error'

def convertNickname(name):
    temp = name.split('[')
    nickname = temp[0]
    return nickname

def convertJupo(name):
    a = name.split('[')
    temp = a[1]
    if '/' in name:
        b = temp.split('/')
        jupo = b[0]
        return jupo
    else:
        b = temp.split(']')
        jupo = b[0]
        return jupo

def convertBupo(name):
    a = name.split('/')
    temp = a[1]
    b = temp.split(']')
    bupo = b[0]
    return bupo

def caculateUnit(money):
    money = int(money)
    if money >= 100000000:
        uk = money // 100000000
        man = (money % 100000000) // 10000
        won = (money % 100000000) % 10000
        if man == 0 and won != 0:
            text = str(uk) + "억 " + str(won) + "원"
        elif man != 0 and won == 0:
            text = str(uk) + "억 " + str(man) + "만원"
        elif man == 0 and won == 0:
            text = str(uk) + "억원"
        else:
            text = str(uk) + "억 " + str(man) + "만 " + str(won) + "원"

        return text
    elif money < 100000000 and money >= 10000:
        man = money // 10000
        won = money % 10000
        if won == 0:
            text = str(man) + "만원"
        else:
            text = str(man) + "만 " + str(won) + "원"
        return text
    elif money < 10000:
        man = money // 10000
        won = money % 10000
        text = str(won) + " 원"
        return text

def convertCheck(teamlist, pos):
    text = ''
    pos2 = pos.upper()
    for player in teamlist:
        if player[2] == '체크':
            if player[0] == pos2:
                text = text + player[1] + ", "
    return text

def countCheck(teamlist):
    count = 0
    for player in teamlist:
        if player[2] == '체크':
               count += 1
    return count


def getteamlist(teamlist):
    text = ""
    for player in teamlist:
        text = text + player[1] + " / " + player[0] + "\n"

    return text

def checklowercase(nickname):
    nickname = nickname.lower()
    return nickname