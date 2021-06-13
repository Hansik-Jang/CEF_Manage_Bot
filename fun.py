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