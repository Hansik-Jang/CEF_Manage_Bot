import string

def getNickFromDisplayname(ctx):
    temp = ctx.author.display_name.split('[')
    nickname = temp[0].strip()
    return nickname

def getNickFromDisplayname2(name):
    temp = name.split('[')
    nickname = temp[0].strip()
    return nickname

def getJupoFromDisplayname(ctx):
    a = ctx.author.display_name.split('[')
    temp = a[1]
    if '/' in ctx.author.display_name:
        b = temp.split('/')
        jupo = b[0].upper()
        return jupo
    else:
        b = temp.split(']')
        jupo = b[0].upper()
        return jupo

# display_name으로부터 주포지션 정보 얻기
def getJupoFromDisplayname2(name):
    a = name.split('[')
#    print("0 - ", a[0])
#   print("1 - ", a[1])
    temp = a[1]
    if '/' in name:
        b = temp.split('/')
        jupo = b[0].upper()
        return jupo
    else:
        b = temp.split(']')
        jupo = b[0].upper()
        return jupo

def getBupoFromDisplayname(ctx):
    if '/' in ctx.author.display_name:
        a = ctx.author.display_name.split('/')
        temp = a[1]
        b = temp.split(']')
        bupo = b[0].upper()
        return bupo
    else:
        return '없음'

def eraseBlackNick(nickname):
    if ' ' in nickname:
        nickname = nickname.replace(' ', '')
        return nickname
    else:
        return nickname

def fitExcludeBupo(ctx):
    nickname = getNickFromDisplayname(ctx)
    jupo = getJupoFromDisplayname(ctx)
    result = nickname + "[" + jupo + "]"
    return result

def fitIncludeBupo(ctx):
    nickname = getNickFromDisplayname(ctx)
    jupo = getJupoFromDisplayname(ctx)
    bupo = getBupoFromDisplayname(ctx)
    result = nickname + "[" + jupo + "/" + bupo + "]"
    return result

def printDump(conn):
    # Dump 출력
    # 데이터베이스 백업
    with conn:
        with open('./resource/dump.sql', 'w') as f:
            for line in conn.iterdump():
                f.write('%s\n' % line)
            print('DumpPrint Complete')

    # f.close(), conn.close()