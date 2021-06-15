def teamNameConvert(name):
    if name == "A" or name == 'a':
        return 'TEAM_A'
    elif name == "B" or name == 'b':
        return 'TEAM_B'
    elif name == "C" or name == 'c':
        return 'TEAM_C'
    elif name == "D" or name == 'd':
        return 'TEAM_D'

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