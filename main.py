import discord
import asyncio
import string
import random
import os
import time
import myfun
from discord.ext import commands
from discord.utils import get
import datetime
import googletrans
import gspread
import fun
import sqlite3

SWITCH_NICKNAME_CHANGE = True

TRASNFER_PERSENT = 15

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1552A1axMJDfxN7kv1TyohmJ3VqKNa7mBeQstHoIRpUQ')
# sh2 = gc.open_by_key('1OP8XMpM93DPScaHX9hGtukf-qaZyalVgzhF--8i2e7')
worksheet_list = sh.worksheet('명단')
worksheet_join = sh.worksheet('가입')
worksheet_left = sh.worksheet('탈퇴')
worksheet_career = sh.worksheet('경력')
worksheet_info = sh.worksheet('팀정보')
worksheet_check_A = sh.worksheet('출첵A')
worksheet_check_B = sh.worksheet('출첵B')
worksheet_check_C = sh.worksheet('출첵C')
worksheet_check_D = sh.worksheet('출첵D')
worksheet_check_E = sh.worksheet('출첵E')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="%", intents=intents)

team = "무소속"
image_types = ["png", "jpeg", "jpg"]

f = open("key.txt", 'r')
key = f.readline()
nick_change_switch = 1
toto_dividend = 23 / 10
a_team_name = ''
b_team_name = ''
c_team_name = ''
d_team_name = ''

number1 = 0

@bot.event
async def on_ready():
    print("로그인 중")
    print(bot.user.name)
    print(bot.user.id)
    print('........')
    game = discord.Game("'%도움말2' | 관리봇")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
async def 번역(ctx,*, text):
    translator = googletrans.Translator()
    ru_result = translator.translate(text, dest='ru')
    en_result = translator.translate(text, dest='en')
    ja_result = translator.translate(text, dest='ja')
    id_result = translator.translate(text, dest='id')
    await ctx.reply(content=f"번역 : {en_result.text}")
    

@bot.command(aliases=['tr'])
async def trans(ctx, *, text):
    translator = googletrans.Translator()
    result = translator.translate(text, dest='ko')
    await ctx.send(content=f"```{result.text}```")


@bot.command()
async def 스위치(ctx, select):
    MAX_COUNT = 20
    role_names = [role.name for role in ctx.author.roles]
    if '스태프' in role_names:
        if select == '닉변':
            global SWITCH_NICKNAME_CHANGE
            if SWITCH_NICKNAME_CHANGE:
                SWITCH_NICKNAME_CHANGE = False
                await ctx.send('```cs\n'
                               '정상 작동되어 닉네임 변경이 가능합니다.```')
                cd = await ctx.send("20초 후 자동으로 변경됩니다.")
                for i in range(0, MAX_COUNT) :
                    j = MAX_COUNT - i
                    await cd.edit(content=f"{j}초 남았습니다.")
                    time.sleep(1)
                    if j == 1 :
                        print(SWITCH_NICKNAME_CHANGE)
                        SWITCH_NICKNAME_CHANGE = True
                        print(SWITCH_NICKNAME_CHANGE)
                        await cd.edit('```cs\n'
                                       '제한 시간이 종료되었습니다.```')
    else:
        await ctx.send("스태프만 사용 가능한 명령어입니다.")

@bot.command()
async def 로또(ctx):
    num = []
    for i in range(1, 45):
        num.append(i)
    num_li = []
    for i in range(6):
        temp = random.choice(num)
        num_li.append(temp)
        num.remove(temp)

    num_li.sort()
    text = ''
    for nu in num_li:
        text = text + str(nu) + ', '
    await ctx.send(content=f"로또 번호 : {text}")


@bot.command(aliases=['카페'])
async def 카페링크(ctx):
    await ctx.send('카페 링크 : https://cafe.naver.com/cyberearlyfootballc')


@bot.command()
async def 내전채팅공지(ctx, *, text):
    a_team_chat_id = get(ctx.guild.text_channels, id=716649980374286386)
    b_team_chat_id = get(ctx.guild.text_channels, id=716650018664349706)
    c_team_chat_id = get(ctx.guild.text_channels, id=727532506932445354)
    d_team_chat_id = get(ctx.guild.text_channels, id=1052741347515322490)
    e_team_chat_id = get(ctx.guild.text_channels, id=1053639929323868161)
    f_team_chat_id = get(ctx.guild.text_channels, id=1052603649794252901)
    g_team_chat_id = get(ctx.guild.text_channels, id=1084082346745135134)
    h_team_chat_id = get(ctx.guild.text_channels, id=1084082460041682984)

    channel_li = [a_team_chat_id, b_team_chat_id, c_team_chat_id, d_team_chat_id, e_team_chat_id, f_team_chat_id, g_team_chat_id, h_team_chat_id]

    for channel in channel_li:
        await channel.send(content=f"{text}")

@bot.command()
async def 투표(ctx, *, text):

    msg = await ctx.send(content=f"{text}")

    await msg.add_reaction("⭕")
    await msg.add_reaction("❌")



@bot.command()
async def 내전순서공지(ctx):
    a_team_chat_id = get(ctx.guild.text_channels, id=716649980374286386)
    b_team_chat_id = get(ctx.guild.text_channels, id=716650018664349706)
    c_team_chat_id = get(ctx.guild.text_channels, id=727532506932445354)
    d_team_chat_id = get(ctx.guild.text_channels, id=1052741347515322490)
    e_team_chat_id = get(ctx.guild.text_channels, id=1053639929323868161)
    f_team_chat_id = get(ctx.guild.text_channels, id=1052603649794252901)
    g_team_chat_id = get(ctx.guild.text_channels, id=1084082346745135134)
    h_team_chat_id = get(ctx.guild.text_channels, id=1084082460041682984)

    channel_li = [a_team_chat_id, b_team_chat_id, c_team_chat_id, d_team_chat_id, e_team_chat_id, f_team_chat_id, g_team_chat_id, h_team_chat_id]

    #for channel in channel_li:
    #    await channel.send(content=f"{text}")
    try:
        await ctx.send("```현재 진행 중인 팀의 개수를 입력하세요.\n"
                       "1 - 4팀\n"
                       "2 - 6팀\n"
                       "3 - 8팀 (4+4)```")
        msg2 = await bot.wait_for("message", check=lambda m : m.author == ctx.author and m.channel == ctx.channel,
                                     timeout=10.0)
    except asyncio.TimeoutError :
        await ctx.channel.send("시간 초과")
    else:
        if msg2.content.lower() == '1':
            try:
                await ctx.send("```숫자를 입력하세요.\n"
                         "1 - 1번째 경기 : A팀 vs B팀 // C팀 vs D팀\n"
                         "2 - 2번째 경기 : A팀 vs C팀 // B팀 vs D팀\n"
                         "3 - 3번째 경기 : A팀 vs D팀 // B팀 vs C팀```")
                msg = await bot.wait_for("message", check=lambda m : m.author == ctx.author and m.channel == ctx.channel,
                                         timeout=10.0)
            except asyncio.TimeoutError :
                await ctx.channel.send("시간 초과")

            else:
                if msg.content.lower() == '1':
                    await msg.delete()
                    await a_team_chat_id.send("```현재 경기 순서\n1번째 경기 : A팀 vs B팀 // C팀 vs D팀```")
                    await b_team_chat_id.send("```현재 경기 순서\n1번째 경기 : A팀 vs B팀 // C팀 vs D팀```")
                    await c_team_chat_id.send("```현재 경기 순서\n1번째 경기 : A팀 vs B팀 // C팀 vs D팀```")
                    await d_team_chat_id.send("```현재 경기 순서\n1번째 경기 : A팀 vs B팀 // C팀 vs D팀```")
                elif msg.content.lower() == '2':
                    await msg.delete()
                    await a_team_chat_id.send("```현재 경기 순서\n2번째 경기 : A팀 vs C팀 // B팀 vs D팀```")
                    await b_team_chat_id.send("```현재 경기 순서\n2번째 경기 : A팀 vs C팀 // B팀 vs D팀```")
                    await c_team_chat_id.send("```현재 경기 순서\n2번째 경기 : A팀 vs C팀 // B팀 vs D팀```")
                    await d_team_chat_id.send("```현재 경기 순서\n2번째 경기 : A팀 vs C팀 // B팀 vs D팀```")
                elif msg.content.lower() == '3':
                    await msg.delete()
                    await a_team_chat_id.send("```현재 경기 순서\n3번째 경기 : A팀 vs D팀 // B팀 vs C팀```")
                    await b_team_chat_id.send("```현재 경기 순서\n3번째 경기 : A팀 vs D팀 // B팀 vs C팀```")
                    await c_team_chat_id.send("```현재 경기 순서\n3번째 경기 : A팀 vs D팀 // B팀 vs C팀```")
                    await d_team_chat_id.send("```현재 경기 순서\n3번째 경기 : A팀 vs D팀 // B팀 vs C팀```")

        elif msg2.content.lower() == '2':
            try:
                await ctx.send("```숫자를 입력하세요.\n"
                               "1 - 1번째 경기 : F vs A // B vs C // D vs E\n"
                               "2 - 2번째 경기 : F vs B // A vs D // C vs E\n"
                               "3 - 3번째 경기 : F vs C // A vs E // B vs D\n"
                               "4 - 4번째 경기 : F vs D // A vs C // B vs E\n"
                               "5 - 5번째 경기 : F vs E // A vs B // C vs D\n```")
                msg = await bot.wait_for("message",
                                         check=lambda m : m.author == ctx.author and m.channel == ctx.channel,
                                         timeout=10.0)
            except asyncio.TimeoutError :
                await ctx.channel.send("시간 초과")
            else:
                if msg.content.lower() == '1':
                    await msg.delete()
                    await a_team_chat_id.send("```1번째 경기 : F vs A // B vs C // D vs E```")
                    await b_team_chat_id.send("```1번째 경기 : F vs A // B vs C // D vs E```")
                    await c_team_chat_id.send("```1번째 경기 : F vs A // B vs C // D vs E```")
                    await d_team_chat_id.send("```1번째 경기 : F vs A // B vs C // D vs E```")
                    await e_team_chat_id.send("```1번째 경기 : F vs A // B vs C // D vs E```")
                    await f_team_chat_id.send("```1번째 경기 : F vs A // B vs C // D vs E```")
                elif msg.content.lower() == '2':
                    await msg.delete()
                    await a_team_chat_id.send("```2번째 경기 : F vs B // A vs D // C vs E```")
                    await b_team_chat_id.send("```2번째 경기 : F vs B // A vs D // C vs E```")
                    await c_team_chat_id.send("```2번째 경기 : F vs B // A vs D // C vs E```")
                    await d_team_chat_id.send("```2번째 경기 : F vs B // A vs D // C vs E```")
                    await e_team_chat_id.send("```2번째 경기 : F vs B // A vs D // C vs E```")
                    await f_team_chat_id.send("```2번째 경기 : F vs B // A vs D // C vs E```")
                elif msg.content.lower() == '3':
                    await msg.delete()
                    await a_team_chat_id.send("```3번째 경기 : F vs C // A vs E // B vs D```")
                    await b_team_chat_id.send("```3번째 경기 : F vs C // A vs E // B vs D```")
                    await c_team_chat_id.send("```3번째 경기 : F vs C // A vs E // B vs D```")
                    await d_team_chat_id.send("```3번째 경기 : F vs C // A vs E // B vs D```")
                    await e_team_chat_id.send("```3번째 경기 : F vs C // A vs E // B vs D```")
                    await f_team_chat_id.send("```3번째 경기 : F vs C // A vs E // B vs D```")
                elif msg.content.lower() == '4':
                    await msg.delete()
                    await a_team_chat_id.send("```4번째 경기 : F vs D // A vs C // B vs E```")
                    await b_team_chat_id.send("```4번째 경기 : F vs D // A vs C // B vs E```")
                    await c_team_chat_id.send("```4번째 경기 : F vs D // A vs C // B vs E```")
                    await d_team_chat_id.send("```4번째 경기 : F vs D // A vs C // B vs E```")
                    await e_team_chat_id.send("```4번째 경기 : F vs D // A vs C // B vs E```")
                    await f_team_chat_id.send("```4번째 경기 : F vs D // A vs C // B vs E```")
                elif msg.content.lower() == '5':
                    await msg.delete()
                    await a_team_chat_id.send("```5번째 경기 : F vs E // A vs B // C vs D```")
                    await b_team_chat_id.send("```5번째 경기 : F vs E // A vs B // C vs D```")
                    await c_team_chat_id.send("```5번째 경기 : F vs E // A vs B // C vs D```")
                    await d_team_chat_id.send("```5번째 경기 : F vs E // A vs B // C vs D```")
                    await e_team_chat_id.send("```5번째 경기 : F vs E // A vs B // C vs D```")
                    await f_team_chat_id.send("```5번째 경기 : F vs E // A vs B // C vs D```")

        elif msg2.content.lower() == '3':
            try :
                await ctx.send("```숫자를 입력하세요.\n"
                               "1 - 1번째 경기 : A vs B // C vs D // E vs F // G vs H\n"
                               "2 - 2번째 경기 : A vs C // B vs D // E vs G // F vs H\n"
                               "3 - 3번째 경기 : A vs D // B vs C // E vs H // F vs G\n```")
                msg = await bot.wait_for("message",
                                         check=lambda m : m.author == ctx.author and m.channel == ctx.channel,
                                         timeout=10.0)
            except asyncio.TimeoutError :
                await ctx.channel.send("시간 초과")
            else :
                if msg.content.lower() == '1':
                    await a_team_chat_id.send("```현재 경기 순서(그룹 A)\n1번째 경기 : A팀 vs B팀 // C팀 vs D팀```")
                    await b_team_chat_id.send("```현재 경기 순서(그룹 A)\n1번째 경기 : A팀 vs B팀 // C팀 vs D팀```")
                    await c_team_chat_id.send("```현재 경기 순서(그룹 A)\n1번째 경기 : A팀 vs B팀 // C팀 vs D팀```")
                    await d_team_chat_id.send("```현재 경기 순서(그룹 A)\n1번째 경기 : A팀 vs B팀 // C팀 vs D팀```")

                    await e_team_chat_id.send("```현재 경기 순서(그룹 B)\n1번째 경기 : E팀 vs F팀 // G팀 vs H팀```")
                    await f_team_chat_id.send("```현재 경기 순서(그룹 B)\n1번째 경기 : E팀 vs F팀 // G팀 vs H팀```")
                    await g_team_chat_id.send("```현재 경기 순서(그룹 B)\n1번째 경기 : E팀 vs F팀 // G팀 vs H팀```")
                    await h_team_chat_id.send("```현재 경기 순서(그룹 B)\n1번째 경기 : E팀 vs F팀 // G팀 vs H팀```")

                elif msg.content.lower() == '2':
                    await msg.delete()
                    await a_team_chat_id.send("```현재 경기 순서(그룹 A)\n2번째 경기 : A팀 vs C팀 // B팀 vs D팀```")
                    await b_team_chat_id.send("```현재 경기 순서(그룹 A)\n2번째 경기 : A팀 vs C팀 // B팀 vs D팀```")
                    await c_team_chat_id.send("```현재 경기 순서(그룹 A)\n2번째 경기 : A팀 vs C팀 // B팀 vs D팀```")
                    await d_team_chat_id.send("```현재 경기 순서(그룹 A)\n2번째 경기 : A팀 vs C팀 // B팀 vs D팀```")

                    await e_team_chat_id.send("```현재 경기 순서(그룹 B)\n2번째 경기 : E팀 vs G팀 // F팀 vs H팀```")
                    await f_team_chat_id.send("```현재 경기 순서(그룹 B)\n2번째 경기 : E팀 vs G팀 // F팀 vs H팀```")
                    await g_team_chat_id.send("```현재 경기 순서(그룹 B)\n2번째 경기 : E팀 vs G팀 // F팀 vs H팀```")
                    await h_team_chat_id.send("```현재 경기 순서(그룹 B)\n2번째 경기 : E팀 vs G팀 // F팀 vs H팀```")
                elif msg.content.lower() == '3':
                    await msg.delete()
                    await a_team_chat_id.send("```현재 경기 순서(그룹 A)\n3번째 경기 : A팀 vs D팀 // B팀 vs C팀```")
                    await b_team_chat_id.send("```현재 경기 순서(그룹 A)\n3번째 경기 : A팀 vs D팀 // B팀 vs C팀```")
                    await c_team_chat_id.send("```현재 경기 순서(그룹 A)\n3번째 경기 : A팀 vs D팀 // B팀 vs C팀```")
                    await d_team_chat_id.send("```현재 경기 순서(그룹 A)\n3번째 경기 : A팀 vs D팀 // B팀 vs C팀```")

                    await e_team_chat_id.send("```현재 경기 순서(그룹 B)\n3번째 경기 : E팀 vs H팀 // F팀 vs G팀```")
                    await f_team_chat_id.send("```현재 경기 순서(그룹 B)\n3번째 경기 : E팀 vs H팀 // F팀 vs G팀```")
                    await g_team_chat_id.send("```현재 경기 순서(그룹 B)\n3번째 경기 : E팀 vs H팀 // F팀 vs G팀```")
                    await h_team_chat_id.send("```현재 경기 순서(그룹 B)\n3번째 경기 : E팀 vs H팀 // F팀 vs G팀```")






@bot.command()
async def 팀명등록(ctx, team, *, text):
    global a_team_name
    global b_team_name
    global c_team_name
    global d_team_name
    team = team.upper()

    if team == 'A':
        a_team_name = text
        channel_id = get(ctx.guild.channels, name='내전-a-파랑💙')
        await channel_id.edit(topic=text)
    elif team == 'B':
        b_team_name = text
    elif team == 'C':
        c_team_name = text
    elif team == 'D':
        d_team_name = text

    await ctx.send(content=f"{team} 팀명이 '{text}'로 등록되었습니다.")

@bot.command()
async def 팀명(ctx):
    global a_team_name
    global b_team_name
    global c_team_name
    global d_team_name

    await ctx.send(f"```A팀 팀명 : {a_team_name}\n"
                   f"B팀 팀명 : {b_team_name}\n"
                   f"C팀 팀명 : {c_team_name}\n"
                   f"D팀 팀명 : {d_team_name}```")


@bot.command()
async def te1(ctx, number):
    channel = get(ctx.guild.channels, name='공개회의')
    if ctx.author.id == 283239466712170506:
        global number1
        number1 = number
        await channel.send(content=f"{myfun.getNickFromDisplayname(ctx)} - {number}")
    else:
        await channel.send(content=f"{myfun.getNickFromDisplayname(ctx)} 돌아가라 애송이 당신에겐 권한이 없소")

@bot.command()
async def te2(ctx):
    global number1
    await ctx.send(content=f"{myfun.getNickFromDisplayname(ctx)} - {number1}")

@bot.command()
async def 후원방법(ctx):
    await ctx.send("```사이버 조기 축구회(C.E.F) 서버 후원\n"
                   "카카오뱅크 3333-16-3306289 장한식```"
                   "```해당 후원금은 일정 금액은 봇 가동을 위한 컴퓨터 전기요금에 일부 사용될 것이며, \n"
                   "서버 행사 등 서버 활동을 위해 사용될 것입니다.```")

@bot.command()
async def re(ctx, *, text):
    channel_id = get(ctx.guild.channels, name='자유채팅💬')
    await channel_id.send(content=f"{text}")
'''
@bot.command()
async def 토토배팅(ctx, result, price):
    await ctx.message.delete()
    BAT_MAX = 100000
    if str(ctx.message.channel) == '유로-토토💰':
        game_max = worksheet_game.acell('A1').value
        now = datetime.datetime.now()
        now_time = now.strftime('%Y-%m-%d %H:%M:%S')
        result_li = ['잉글랜드', '무', '이탈리아']
        result_li = ['잉글랜드', '무', '이탈리아']
        if result in result_li and int(price) <= BAT_MAX:      # 승, 무, 패 맞게 입력하고, 베팅 금액이 100만원 이하일 때
            # 중복여부 체크
            ol_max = str(int(game_max) + 1)
            ol_range = worksheet_game.range("D2:D" + ol_max)
            li = []
            for cell in ol_range:
                li.append(cell.value)
            if fun.convertNickname(ctx.author.display_name) not in li:  # 중복 검사
                # 사용한 비용만큼 개인자산 차감
                cell_max = worksheet_career.acell('A1').value        # 범위 내 셀 값 로딩
                range_list = worksheet_career.range('E2:E' + cell_max)        # 내 자산 차감
                for i, cell in enumerate(range_list):
                    if str(cell.value) == str(fun.convertNickname(ctx.author.display_name)):
                        check = i + 2
                        presentMoney = int(worksheet_career.acell('R' + str(check)).value)
                        if int(presentMoney) >= int(price):   # 갖고 있는 자산이 베팅 금액이 높을때만
                            presentMoney = presentMoney - int(price)
                            worksheet_career.update_acell('R' + str(check), str(presentMoney))
                            await ctx.send(content=f"{ctx.author.mention} -> {result} 팀 {fun.caculateUnit(price)} 배팅")
                            # 토토 역할 넣기
                            user = ctx.author
                            if result == '잉글랜드' :
                                role = get(ctx.guild.roles, name='토토-잉글랜드')
                                await user.add_roles(role)
                            elif result == '이탈리아' :
                                role = get(ctx.guild.roles, name='토토-이탈리아')
                                await user.add_roles(role)
                            # 게임 시트 토토 영역에 추가
                            worksheet_game.insert_row(
                                ["", now_time, str(ctx.author.id), fun.convertNickname(ctx.author.display_name), result,
                                 str(price)],
                                int(game_max) + 2)
                        else:
                            await ctx.send(content=f"잔액이 부족합니다.")

            else:
                cell_max = worksheet_game.acell('A1').value        # 범위 내 셀 값 로딩
                range_list = worksheet_game.range('D2:D' + str(int(cell_max)+1))        # 내 자산 차감
                for i, cell in enumerate(range_list):
                    if str(cell.value) == str(fun.convertNickname(ctx.author.display_name)):
                        check = i + 2
                        break
                team = worksheet_game.acell('E' + str(check)).value
                bat = worksheet_game.acell('F' + str(check)).value
                await ctx.send(content=f'```이미 참여하였습니다.\n'
                                       f'선택한 팀 : {team}, 배팅 금액 : {fun.caculateUnit(bat)}```')
        elif result not in result_li:
            await ctx.send("```오타 확인해주세요.\n"
                           "'잉글랜드' 혹은 '이탈리아'만 입력 가능합니다.```")
        elif int(price) > BAT_MAX:
            await ctx.send(content=f"```{BAT_MAX} 이하만 입력 가능합니다.```")
    else:
        await ctx.send('```유로-토토💰 채널에서만 사용 가능합니다.```')
'''


@bot.command()
async def test(ctx):
    jupo = ''
    bupo = ''
    pos_li = ['st', 'lw', 'rw', 'cam', 'cm', 'cdm', 'lb', 'cb', 'rb', 'gk']
    # ------------------------- 주포지션 ----------------------------------
    jupo_msg = await ctx.channel.send("```주포지션을 입력하세요. 아래에 표기된 포지션만 입력 가능합니다.\n"
                           "ST, LW, RW, CAM, CM, CDM, LB, CB, RB, GK```")
    try:
        msg = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                 timeout=10.0)

    except asyncio.TimeoutError:
        await ctx.channel.send("시간 초과")
    else:
        if msg.content.lower() == 'st':
            await msg.delete()
            await ctx.send("ST 선택")
            jupo = 'ST'
        elif msg.content.lower() == 'lw':
            await msg.delete()
            await ctx.send("LW 선택")
            jupo = 'LW'
        elif msg.content.lower() == 'rw':
            await msg.delete()
            await ctx.send("RW 선택")
            jupo = 'RW'
        elif msg.content.lower() == 'cam':
            await msg.delete()
            await ctx.send("CAM 선택")
            jupo = 'CAM'
        elif msg.content.lower() == 'CM':
            await msg.delete()
            await ctx.send("CM 선택")
            jupo = 'CM'
        elif msg.content.lower() == 'cdm':
            await msg.delete()
            await ctx.send("CDM 선택")
            jupo = 'CDM'
        elif msg.content.lower() == 'lb':
            await msg.delete()
            await ctx.send("LB 선택")
            jupo = 'LB'
        elif msg.content.lower() == 'cb':
            await msg.delete()
            await ctx.send("CB 선택")
            jupo = 'CB'
        elif msg.content.lower() == 'rb':
            await msg.delete()
            await ctx.send("RB 선택")
            jupo = 'RB'
        elif msg.content.lower() == 'gk':
            await msg.delete()
            await ctx.send("GK 선택")
            jupo = 'GK'
        else:
            await ctx.send("잘못 입력")
    await jupo_msg.delete()
    # ------------------------- 부포지션 ----------------------------------
    bupo_msg = await ctx.channel.send("```부포지션을 입력하세요. 아래에 표기된 포지션만 입력 가능합니다.\n"
                           "ST, LW, RW, CAM, CM, CDM, LB, CB, RB, GK```")
    try:
        msg = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                 timeout=10.0)
    except asyncio.TimeoutError:
        await ctx.channel.send("시간 초과")
    else:
        if msg.content.lower() == 'st':
            await msg.delete()
            await ctx.send("ST 선택")
            bupo = 'ST'
        elif msg.content.lower() == 'lw':
            await msg.delete()
            await ctx.send("LW 선택")
            bupo = 'LW'
        elif msg.content.lower() == 'rw':
            await msg.delete()
            await ctx.send("RW 선택")
            bupo = 'RW'
        elif msg.content.lower() == 'cam':
            await msg.delete()
            await ctx.send("CAM 선택")
            bupo = 'CAM'
        elif msg.content.lower() == 'CM':
            await msg.delete()
            await ctx.send("CM 선택")
            bupo = 'CM'
        elif msg.content.lower() == 'cdm':
            await msg.delete()
            await ctx.send("CDM 선택")
            bupo = 'CDM'
        elif msg.content.lower() == 'lb':
            await msg.delete()
            await ctx.send("LB 선택")
            bupo = 'LB'
        elif msg.content.lower() == 'cb':
            await msg.delete()
            await ctx.send("CB 선택")
            bupo = 'CB'
        elif msg.content.lower() == 'rb':
            await msg.delete()
            await ctx.send("RB 선택")
            bupo = 'RB'
        elif msg.content.lower() == 'gk':
            await msg.delete()
            await ctx.send("GK 선택")
            bupo = 'GK'
        else:
            await ctx.send("잘못 입력")
    await bupo_msg.delete()
    await ctx.send(content=f"```<입력한 정보>\n"
                           f"주포지션 : {jupo}\n"
                           f"부포지션 : {bupo}```")
    # ------------------------- 닉네임 변환 ----------------------------------
    if bupo == '':
        nickname = myfun.getNickFromDisplayname(ctx) + "[" + jupo + "]"
    else:
        nickname = myfun.getNickFromDisplayname(ctx) + "[" + jupo + "/" + bupo + "]"
    await ctx.send(nickname)
    user = ctx.author
    await user.edit(nick=nickname)
'''
@bot.command()
async def 토토결과(ctx, win, rate):
    switch = False
    winners = []
    car_select_li = worksheet_game.range('E3:E100')
    for i, cell in enumerate(car_select_li):
        print(cell.value, win)
        if cell.value == win:
            key = str(i + 3)
            print(key)
            data = worksheet_game.range('D' + key + ':F' + key)
            winners.append((data[0].value, data[2].value))
            switch = True
    print(winners)
    print(len(winners))

    if switch:
        car_max = worksheet_career.acell("a1").value
        nick_li = worksheet_career.range('E2:E' + car_max)  # 닉네임 목록
        text = '```토토 당첨 결과(배당율 : ' + rate + ')\n\n'
        for winner in winners:
            for i, cell in enumerate(nick_li):
                if cell.value == winner[0] or cell.value == winner[0] + ' ':
                    time.sleep(1.5)
                    print(cell.value, winner[0])
                    col2 = i + 2
                    price = int(int(winner[1]) * float(rate))
                    pw = int(worksheet_career.acell('R' + str(col2)).value)
                    bf_pw = pw
                    pw = round(pw + price, -1)
                    af_pw = pw
                    #worksheet_career.update_acell('R' + str(col2), str(pw))
                    tw = int(worksheet_career.acell('S' + str(col2)).value)
                    bf_tw = tw
                    tw = round(tw + price, -1)
                    af_tw = tw
                    #worksheet_career.update_acell('S' + str(col2), str(tw))
                    #await ctx.send(content=f"```<{fun.convertNickname(winner[0])}>\t"
                    #                       f"현재 잔액 : {fun.caculateUnit(bf_pw)} -> {fun.caculateUnit(af_pw)}, "
                    #                       f"누적 금액 : {fun.caculateUnit(bf_tw)} -> {fun.caculateUnit(af_tw)}```")
                    text = text + '<' + fun.convertNickname(winner[0]) + '> 배팅금액 : ' + str(winner[1]) + ' 원\n' + \
                           '현재 잔액 : ' + str(bf_pw) + ' 원 -> ' + str(af_pw) + ' 원, ' + \
                           '누적 금액 : ' + str(bf_tw) + ' 원 -> ' + str(af_tw) + ' 원\n\n'

        text = text + '```'
        await ctx.send(text)
        # 게임 토토 시트 초기화
        #worksheet_game.delete_rows(3, 50)
    else:
        await ctx.send('```승리팀을 다시 입력하세요.```')

'''
'''
@bot.command()
async def 결(ctx):
    name_list = worksheet_game.range('D3:D41')
    choice_list = worksheet_game.range('E3:E41')
    price_list = worksheet_game.range('F3:F41')
    a = []
    b = []

    for i, cell in enumerate(choice_list):
        if str(cell.value) == '이탈리아':
            aname = name_list[i].value
            aprice = price_list[i].value
            result = int(int(aprice) * 23 / 10)
            a.append([aname, aprice, result])
        else:
            bname = name_list[i].value
            bprice = price_list[i].value
            result = int(int(bprice) * 204 / 100)
            b.append([bname, bprice, result])

    print(a)
    print(b)
    text1 = ''
    text2 = ''
    for i in range(len(a)):
        text1 = text1 + a[i][0] + "(" + a[i][1] + " -> " + str(a[i][2]) + ")\n"
    for i in range(len(b)):
        text2 = text2 + b[i][0] + "(" + b[i][1] + " -> 0)\n"
    print(text1)
    print(text2)
    embed = discord.Embed(title="유로2020 결승전 토토 베팅 결과", description="", color=0x62c1cc)
    embed.add_field(name="이탈리아 (승) (x2.30)", value=text1, inline=False)
    embed.add_field(name="잉글랜드 (x2.04)", value=text2, inline=False)
    await ctx.send(embed=embed)
    ownRoles = [role.name for role in ctx.author.roles]
    if '스태프' in ownRoles:
        print('a')
        await ctx.send(content=f"")
    else:
        await ctx.send("```스태프만 사용 가능한 명령어입니다.```")
'''



@bot.command()
async def 송금(ctx, member: discord.Member, send):
    print(send)
    send = send.replace(',', '')
    send = int(send)
    print(type(send))
    print('send : ', send)
    if send > 0:    # 0원 이상만 가능
        cell_max = worksheet_career.acell('A1').value
        # 범위 내 셀 값 로딩
        range_list = worksheet_career.range('E2:E' + cell_max)
        # 내 자산 차감
        for i, cell in enumerate(range_list):
            if str(cell.value) == str(fun.convertNickname(ctx.author.display_name)):
                check = i + 2
                mymoney = int(worksheet_career.acell('R' + str(check)).value)
                if int(mymoney) >= int(send):        # 갖고 있는 자산이 송금 금액보다 높을때만
                    myaftermoney = int(mymoney) - send
                    print('myaftermoney:', myaftermoney)
                    worksheet_career.update_acell('R' + str(check), str(myaftermoney))

                    for j, cell2 in enumerate(range_list):
                        if str(cell2.value) == str(fun.convertNickname(member.display_name)):
                            check2 = j + 2
                            mem_money = int(worksheet_career.acell('R' + str(check2)).value)
                            print('mem_money:', mem_money)
                            mem_aftermoney = int(mem_money) + send
                            print('mem_aftermoney:', mem_aftermoney)
                            worksheet_career.update_acell('R' + str(check2), str(mem_aftermoney))
                            break
                    await ctx.send(content=f"```<송금 완료>\n"
                                           f"송금 금액 : {fun.caculateUnit(send)}\n"
                                           f"보낸이 : {fun.convertNickname(ctx.author.display_name)}\n"
                                           f"{fun.caculateUnit(mymoney)} - {fun.caculateUnit(send)} = {fun.caculateUnit(myaftermoney)}\n"
                                           f"받는이 : {fun.convertNickname(member.display_name)}\n"
                                           f"{fun.caculateUnit(mem_money)} + {fun.caculateUnit(send)} = {fun.caculateUnit(mem_aftermoney)}```")
                else:
                    await ctx.send(content=f"```<송금 오류>\n"
                                           f"{fun.convertNickname(ctx.author.display_name)} 잔액이 부족합니다.\n"
                                           f"현재 자산 : {mymoney} 만원```")
    else:
        await ctx.send("0원 이상만 송금 가능합니다.")
'''

'''
@bot.command()
async def 환율(ctx, member: discord.Member, text):
    name = member.display_name.split('[')
    role_names = [role.name for role in ctx.author.roles]
    if "스태프" in role_names:
        # 범위(체크)
        cell_max = worksheet_list.acell('A1').value
        # 범위 내 셀 값 로딩
        range_list = worksheet_list.range('E2:E' + cell_max)
        temp = member.display_name.split('[')
        nickname = temp[0]
        # 스프레드 체크 및 업데이트
        if text == '선수':
            for i, cell in enumerate(range_list) :
                if str(cell.value) == str(nickname) :
                    check = i + 2
                    before_price = worksheet_career.acell('Q' + str(check)).value
                    now_price = int(before_price) * 120 / 100
                    print(now_price)


@bot.command()
async def 시트링크(ctx):
    await ctx.send("https://docs.google.com/spreadsheets/d/1552A1axMJDfxN7kv1TyohmJ3VqKNa7mBeQstHoIRpUQ/edit?usp=sharing")

'''@bot.command()
async def 도움말2(ctx):
    # 임베드 설정
    embed = discord.Embed(title="CEF 관리봇 명령어", description="", color=0x62c1cc)
    embed.add_field(name="가입 및 탈퇴", value="%가입, %가입안내, %탈퇴", inline=False)
    embed.add_field(name="변경", value="%닉변, %주포변경, %부포변경, %부포삭제, %역할부여, %역할회수(미구현)", inline=False)
    embed.add_field(name="커리어", value="%커리어, %토츠, %발롱도르, %내정보", inline=False)
    embed.add_field(name="출석", value="%출석, %출석취소, %출석결과, %출석초기화", inline=False)
    embed.add_field(name="가이드", value="각 명령어에 대한 설명 및 사용 방법이 궁금하시면 <%가이드 '명령어'>를 입력해주세요.", inline=False)
    embed.add_field(name="스태프 전용 명령어", value="%가입안내, %역할부여, %역할회수(미구현), %커리어, %토츠, %발롱도르, %출석초기화, %출석공지", inline=False)
    embed.add_field(name="확인 링크",
                    value="https://docs.google.com/spreadsheets/d/1552A1axMJDfxN7kv1TyohmJ3VqKNa7mBeQstHoIRpUQ/edit?usp=sharing",
                    inline=False)
    embed.set_footer(text="Copyright ⓒ 2020-2021 타임제이(TimeJ) in C.E.F All Right Reserved.")

    await ctx.message.delete()
    await ctx.send(embed=embed)


@bot.command()
async def 가이드(ctx, text):
    if text == '가입':
        embed = discord.Embed(title="%가입", description="", color=0x62c1cc)
        embed.add_field(name="설명", value="최초 가입 시 시트에 등록하기 위한 명령어입니다.\n"
                                         "가입 명령어를 입력하기 전, 가입 안내 채널의 간단한 퀴즈 먼저 해주세요.", inline=False)
        embed.add_field(name="사용방법", value="%가입", inline=True)
        embed.add_field(name="사용권한", value="[everyone]", inline=True)
    elif text == '가입안내':
        embed = discord.Embed(title="%가입안내", description="", color=0x62c1cc)
        embed.add_field(name="설명", value="가입안내문을 출력하며, 이모지를 입력받습니다.", inline=False)
        embed.add_field(name="사용방법", value="%가입안내", inline=True)
        embed.add_field(name="사용권한", value="[스태프]", inline=True)
    elif text == '탈퇴':
        embed = discord.Embed(title="%탈퇴", description="", color=0x62c1cc)
        embed.add_field(name="설명", value="탈퇴 시 입력하는 명령어입니다.\n"
                                         "탈퇴 명령어를 입력 시, 스프레드 시트에 탈퇴일자가 기록됩니다.", inline=False)
        embed.add_field(name="사용방법", value="%탈퇴", inline=True)
        embed.add_field(name="사용권한", value="[everyone]", inline=True)
    elif text == '닉변':
        embed = discord.Embed(title="%닉변", description="", color=0x62c1cc)
        embed.add_field(name="설명", value="시트 상의 주포지션을 수정합니다.\n"
                                         "해당 명령어는 현재의 디스코드 닉네임을 기반으로 수정됩니다.\n"
                                         "디스코드 닉네임을 수정한 후 사용해주세요.", inline=False)
        embed.add_field(name="사용방법", value="%닉변", inline=True)
        embed.add_field(name="사용권한", value="[everyone]", inline=True)
    elif text == '주포변경':
        embed = discord.Embed(title="%주포변경", description="", color=0x62c1cc)
        embed.add_field(name="설명", value="입력한 포지션으로 스프레드 시트를 업데이트합니다.\n"
                                        "주 포지션은 ST, LW, RW, CAM, CM, CDM, LB, CB, RB, GK, ALL, AF 중에 입력 가능하며,\n"
                                        "리그 참가 시에는 리그에 참가한 포지션으로 수정해주세요.\n"
                                        "명령어 사용 후에는 직접 디스코드 닉네임을 수정해주세요.", inline=False)
        embed.add_field(name="사용방법", value="%주포변경 <포지션>", inline=True)
        embed.add_field(name="사용권한", value="[everyone]", inline=True)
    elif text == '부포변경':
        embed = discord.Embed(title="%부포변경", description="", color=0x62c1cc)
        embed.add_field(name="설명", value="입력한 포지션으로 스프레드 시트를 업데이트합니다.\n"
                                            "주 포지션은 ST, LW, RW, CAM, CM, CDM, LB, CB, RB, GK, ALL, AF 중에 입력 가능하며,\n"
                                            "부 포지션은 리그 참가와 상관 없이 자유롭게 수정해주시면 됩니다."
                                            "명령어 사용 후에는 직접 디스코드 닉네임을 수정해주세요.", inline=False)
        embed.add_field(name="사용방법", value="%부포변경 <포지션>", inline=True)
        embed.add_field(name="사용권한", value="[everyone]", inline=True)
    elif text == '부포삭제':
        embed = discord.Embed(title="%부포삭제", description="", color=0x62c1cc)
        embed.add_field(name="설명", value="스프레드 시트에서 부 포지션을 삭제합니다.\n"
                                         "명령어 사용 후에는 직접 디스코드 닉네임을 수정해주세요.", inline=False)
        embed.add_field(name="사용방법", value="%부포삭제", inline=True)
        embed.add_field(name="사용권한", value="[everyone]", inline=True)
    elif text == '역할부여':
        embed = discord.Embed(title="%역할부여", description="", color=0x62c1cc)
        embed.add_field(name="설명", value="입력한 팀 이름과 멘션, 포지션에 맞춰 팀 역할이 부여되며,\n"
                                         "스프레드 시트에 업데이트 됩니다.\n"
                                         "팀 이름 : TEAM_A, TEAM_B, TEAM_C, TEAM_D\n"
                                         "ST, LW, RW, CAM, CM, CDM, LB, CB, RB, GK", inline=False)
        embed.add_field(name="사용방법", value="%역할부여 <팀이름> @멘션 <포지션>", inline=True)
        embed.add_field(name="사용권한", value="[스태프]", inline=True)
    elif text == '역할회수':
        embed = discord.Embed(title="%역할회수", description="미구현 상태", color=0x62c1cc)
        embed.add_field(name="설명", value="입력한 팀 이름의 역할을 가진 인원들로부터 해당 역할을 회수합니다.", inline=False)
        embed.add_field(name="사용방법", value="%역할회수", inline=True)
        embed.add_field(name="사용권한", value="[스태프]", inline=True)
    elif text == '커리어':
        embed = discord.Embed(title="%커리어", description="", color=0x62c1cc)
        embed.add_field(name="설명", value="입력한 인원의 우승 횟수를 업데이트합니다.", inline=False)
        embed.add_field(name="사용방법", value="선수일 경우 : %커리어 <선수> @멘션\n"
                                           "코치일 경우 : %커리어 <코치> @멘션", inline=True)
        embed.add_field(name="사용권한", value="[스태프]", inline=True)
    elif text == '토츠':
        embed = discord.Embed(title="%토츠", description="", color=0x62c1cc)
        embed.add_field(name="설명", value="입력한 인원의 포지션별 토츠 횟수를 업데이트합니다.\n"
                                         "FW, MF, DF, GK 중에 입력 가능합니다.", inline=False)

        embed.add_field(name="사용방법", value="%토츠 <포지션> @멘션", inline=True)
        embed.add_field(name="사용권한", value="[스태프]", inline=True)
    elif text == '발롱도르':
        embed = discord.Embed(title="%출석", description="", color=0x62c1cc)
        embed.add_field(name="설명", value="입력한 인원의 발롱도르 횟수를 업데이트 합니다.\n", inline=False)
        embed.add_field(name="사용방법", value="%발롱도르 @멘션", inline=True)
        embed.add_field(name="사용권한", value="[스태프]", inline=True)
    elif text == '내정보':
        embed = discord.Embed(title="%내정보", description="", color=0x62c1cc)
        embed.add_field(name="설명", value="포지션, 소속팀, 토츠, 발롱도르 수상 이력 등 본인의 커리어 정보를 출력합니다.\n"
                                         "해당 명령어는 실행시간이 약간 소요됩니다.", inline=False)
        embed.add_field(name="사용방법", value="%내정보", inline=True)
        embed.add_field(name="사용권한", value="[everyone]", inline=True)
    elif text == '출석':
        embed = discord.Embed(title="%출석", description="", color=0x62c1cc)
        embed.add_field(name="설명", value="본인 팀 출석 명단에 입력한 숫자에 맞게 출석체크를 하여, 이를 업데이트합니다.\n"
                                         "숫자는 1, 2, 3 중 정확하게 입력해야 하며,\n"
                                         "각 팀 출석조사 채널에서만 사용이 가능합니다.", inline=False)
        embed.add_field(name="사용방법", value="%출석 <숫자>", inline=True)
        embed.add_field(name="사용권한", value="[everyone]", inline=True)
    elif text == '출석취소':
        embed = discord.Embed(title="%출석취소", description="", color=0x62c1cc)
        embed.add_field(name="설명", value="본인 팀 출석 명단에 입력한 숫자에 맞게 출석체크를 취소하며, 이를 업데이트합니다.\n"
                                         "숫자는 1, 2, 3 중 정확하게 입력해야 합니다.", inline=False)
        embed.add_field(name="사용방법", value="%출석취소 <숫자>", inline=True)
        embed.add_field(name="사용권한", value="[everyone]", inline=True)
    elif text == '출석결과':
        embed = discord.Embed(title="%출석결과", description="", color=0x62c1cc)
        embed.add_field(name="설명", value="스프레드 시트의 출석 명단으로부터 당일 출석결과를 출력합니다.\n"
                                         "팀 이름은 TEAM_A, TEAM_B, TEAM_C, TEAM_D 중 하나를 정확하게 입력해야 하며,\n"
                                         "숫자는 1, 2, 3 중 정확하게 입력해야 합니다.", inline=False)
        embed.add_field(name="사용방법", value="%출석결과 <팀이름> <숫자>", inline=True)
        embed.add_field(name="사용권한", value="[everyone]", inline=True)
    elif text == '출석초기화':
        embed = discord.Embed(title="%출석초기화", description="", color=0x62c1cc)
        embed.add_field(name="설명", value="당일의 출석체크 명단을 초기화하며,\n"
                                         "각 팀 출석체크 채널에 초기화되었음을 알립니다.", inline=False)
        embed.add_field(name="사용방법", value="%출석초기화", inline=True)
        embed.add_field(name="사용권한", value="[스태프]", inline=True)
    elif text == '출석공지':
        embed = discord.Embed(title="%출석공지", description="", color=0x62c1cc)
        embed.add_field(name="설명", value="각 팀 출석체크 채널에 해당 팀 멘션을 하여 출석체크 공지를 합니다.", inline=False)
        embed.add_field(name="사용방법", value="%출석공지", inline=True)
        embed.add_field(name="사용권한", value="[스태프]", inline=True)

    await ctx.send(embed=embed)

'''
@bot.command()
async def 가입안내(ctx):
    role_names = [role.name for role in ctx.author.roles]
    if '스태프' in role_names:
        await ctx.send("```FIFA 프로클럽 커뮤니티 C.E.F(Cyber Early Football Club)에 오신 것을 환영합니다!\n\n"
                       "저희 C.E.F는 모두가 즐겁게 할 수 있고, 쉽게 접근이 가능한 프로클럽 커뮤니티를 추구합니다.\n"
                       "'상호 간의 존중과 배려'는 저희 C.E.F 가 가장 중요시 여기는 방향성이며,\n"
                       "상호 간의 반말, 과한 친목 행위, 욕설, 음란성 발언 등은 엄중히 금하고 있습니다.\n"
                       "자세한 사항은 카페 혹은 디스코드 내 운영총칙을 참고하여 주시기 바랍니다.```")
        await ctx.send("```저희 C.E.F의 닉네임은 오리진 ID, 인게임 별명, 디스코드, 네이버 카페, 오픈 카톡을 총 5개를 통일해주셔야 합니다.\n"
                       "또한 닉네임의 경우 영어로 제한하고 있으며, 이는 유저들의 혼동을 막기 위한 조치이입니다.\n"
                       "닉네임 양식 : CEF_Nickname\n"
                       "<닉네임 예시>\n"
                       "오리진 ID : CEF_TimeJ\n"
                       "인게임 별명 : CEF TimeJ\n"
                       "디스코드 닉네임 : TimeJ\n"
                       "네이버 카페 닉네임 : TimeJ\n"
                       "오픈 카톡방 닉네임 : TimeJ\n```")
        text1 = await ctx.send("```닉네임 양식 규정을 확인 및 변경이 완료되셨나요?\n"
                               "위의 사항을 다 확인 및 완료되었다면 아래 하트 이모지를 눌러주세요.```")
        await text1.add_reaction("❤")
        text2 = await ctx.send("```저희 C.E.F가 가장 중요하게 여기는 방향성은 무엇일까요?\n"
                               "1번. 클럽원 간의 과도한 경쟁\n"
                               "2번. 상호 간의 존중과 배려\n"
                               "3번. 반말 사용 등 클럽원간의 과한 친목```")
        await text2.add_reaction("1️⃣")
        await text2.add_reaction("2️⃣")
        await text2.add_reaction("3️⃣")
        await ctx.send("```정답을 다 입력하셨으면 cef-가입신청 에서 '%가입' 명령어와 \n"
                       "함께 카페에 작성한 선수 등록글의 링크를 첨부하여 입력해주세요.```")
    else:
        await ctx.send("```해당 명령어는 스태프만 사용 가능합니다.```")


@bot.command(aliases=['join'])
async def 가입(ctx):
    now = datetime.datetime.now()
    now_time = now.strftime('%Y-%m-%d %H:%M:%S')
    overlap_check = 0
    answer = 0
    # 범위(체크)
    cell_max = worksheet_list.acell('A1').value
    cell_data = int(cell_max) + 1
    # 범위 내 셀 값 로딩
    range_list = worksheet_list.range('D2:D' + str(cell_data))
    overlap_list = worksheet_list.range('E2:E' + str(cell_max))
    # 가입 여부 체크
    for i, cell in enumerate(range_list):
        if str(cell.value) == str(ctx.author.id):
            join_point = i + 2
            join_key = True
            break
        else:
            join_key = False

    nickname = fun.convertNickname(ctx.author.display_name)
    # 닉네임 중복 체크
    for i, cell in enumerate(overlap_list):
        if fun.convertNickname(str(cell.value)) == fun.checklowercase(nickname) \
                or fun.convertNickname(str(cell.value)) == fun.checklowercase((nickname + " ")):
            ovr_point = i + 2
            overlap_check = True
            break
        else:
            overlap_check = False
    # 역할 및 채널세팅
    user = ctx.author
    cefRole = get(ctx.guild.roles, name='CEF')
    newRole = get(ctx.guild.roles, name='신규')
    channel = get(ctx.guild.channels, name='가입-탈퇴-명단')
    role_names = [role.name for role in ctx.author.roles]
    team_channel = get(ctx.guild.channels, id=1048944605493743677)
    player_channel = get(ctx.guild.channels, id=969159455956684801)
    # 닉네임 양식 체크, 분리 및 시트 등록
    #  - 신규 가입 & 닉네임 중복 아닐 경우
    if 'CEF' not in role_names:
        print('a')
        if overlap_check == False and join_key == False:
            print('신규, 닉네임 중복 없음')
            # 스프레드 체크 및 업데이트
            if "," in ctx.author.display_name:
                await ctx.reply("```정확한 닉네임 양식을 지켜주세요\n"
                               "주 포지션과 부 포지션의 구분은 '/'을 사용해주세요.\n"
                               "해당 봇에서는 ','를 인식하지 않으며, 이는 봇 고장의 원인이 됩니다.\n"
                               "닉네임 양식 : 닉네임[주포지션/부포지션] or 닉네임[주포지션]```")
            elif "." in ctx.author.display_name:
                await ctx.reply("```정확한 닉네임 양식을 지켜주세요\n"
                               "주 포지션과 부 포지션의 구분은 '/'을 사용해주세요.\n"
                               "해당 봇에서는 '.'를 인식하지 않으며, 이는 봇 고장의 원인이 됩니다.\n"
                               "닉네임 양식 : 닉네임[주포지션/부포지션] or 닉네임[주포지션]```")
            elif "[" in ctx.author.display_name:
                if '/' in ctx.author.display_name:
                    jupo = fun.convertJupo(ctx.author.display_name)
                    bupo = fun.convertBupo(ctx.author.display_name)
                    display_name = ctx.author.display_name + "🐤"
                    id_num = "" + str(ctx.author.id)

                    worksheet_list.insert_row(
                        ["", now_time, display_name, id_num, nickname, jupo, bupo, '무소속',
                         '0000-00-00 00:00:00'], int(cell_max) + 1)
                    worksheet_career.insert_row(
                        ["", now_time, display_name, id_num, nickname, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0], int(cell_max) + 1)

                    await ctx.send(content=f"```{ctx.author.display_name}님 정상 등록되었습니다.```")
                    await user.add_roles(cefRole)
                    await user.add_roles(newRole)
                    await user.edit(nick=display_name)

                    await ctx.reply(content=f"```가입을 환영합니다!\n"
                                            "필독하셔서 게임 진행이나 서버 이용에 차질 없도록 부탁드리겠습니다.```\n"
                                            "https://cafe.naver.com/cyberearlyfootballc/18267\n"
                                            "저희 C.E.F는 토요일을 제외한 매 저녁 9시부터 11시 30분까지 각 팀에 소속되어 게임하게 됩니다.\n"
                                            f"팀을 구하실 때는 아무런 채널에 '%FA역할부여' 명령어를 사용한 후\n"
                                            f"'팀-홍보' 채널 혹은 '선수-홍보' 채널을 이용하시기 바랍니다.")

                    '''await ctx.reply(content=f"```가입을 환영합니다!\n"
                                            "필독하셔서 게임 진행이나 서버 이용에 차질 없도록 부탁드리겠습니다.```\n"
                                            "https://cafe.naver.com/cyberearlyfootballc/18267\n"
                                            "저희 C.E.F는 토요일을 제외한 매 저녁 9시부터 11시 30분까지 각 팀에 소속되어 게임하게 됩니다.\n"
                                            f"팀을 구하실 때는 아무런 채널에 '%FA역할부여' 명령어를 사용한 후\n"
                                            f"{team_channel.mention} 채널 혹은 {player_channel.mention} 채널을 이용하시기 바랍니다.")'''
                    await channel.send(content=f"<신규가입> {ctx.author.mention} (가입일자 : {now_time})")

                else:
                    jupo = fun.convertJupo(ctx.author.display_name)
                    id_num = "" + str(ctx.author.id)
                    display_name = ctx.author.display_name + "🐤"
                    worksheet_list.insert_row(
                        ["", now_time, display_name, id_num, nickname, jupo, '', '무소속',
                         '0000-00-00 00:00:00'], int(cell_max) + 1)
                    worksheet_career.insert_row(
                        ["", now_time, display_name, id_num, nickname, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0], int(cell_max) + 1)
                    await ctx.send(content=f"```{ctx.author.display_name}님 정상 등록되었습니다.```")
                    await user.add_roles(cefRole)
                    await user.add_roles(newRole)
                    await user.edit(nick=display_name)
                    await ctx.reply(content=f"```가입을 환영합니다!\n"
                                            "필독하셔서 게임 진행이나 서버 이용에 차질 없도록 부탁드리겠습니다.\n```"
                                            "https://cafe.naver.com/cyberearlyfootballc/18267\n"
                                            "저희 C.E.F는 토요일을 제외한 매 저녁 9시부터 11시 30분까지 각 팀에 소속되어 게임하게 됩니다.\n"
                                            f"팀을 구하실 때는 아무런 채널에 '%FA역할부여' 명령어를 사용한 후\n"
                                            f"'팀-홍보' 채널 혹은 '선수-홍보' 채널을 이용하시기 바랍니다.")
                    '''await ctx.reply(content=f"```가입을 환영합니다!\n"
                                     "필독하셔서 게임 진행이나 서버 이용에 차질 없도록 부탁드리겠습니다.```"
                                     "https://cafe.naver.com/cyberearlyfootballc/18267\n"
                                     "저희 C.E.F는 토요일을 제외한 매 저녁 9시부터 11시 30분까지 각 팀에 소속되어 게임하게 됩니다.\n"
                                     f"팀을 구하실 때는 아무런 채널에 '%FA역할부여' 명령어를 사용한 후\n"
                                     f"{team_channel.mention} 채널 혹은 {player_channel.mention} 채널을 이용하시기 바랍니다.")'''
                    await channel.send(content=f"<신규가입> {ctx.author.mention} (가입일자 : {now_time})")

            else:
                await ctx.send("```정확한 닉네임 양식을 지켜주세요\n닉네임 양식 : 닉네임[주포지션/부포지션] or 닉네임[주포지션]```")
        # 재가입 & 닉네임 중복 없을 경우
        elif join_key and overlap_check == False:
            print('재가입, 닉네임 중복 없음')
            worksheet_list.update_acell('C' + str(join_point), ctx.author.display_name)
            worksheet_career.update_acell('C' + str(join_point), ctx.author.display_name)
            worksheet_list.update_acell('E' + str(join_point), nickname)
            worksheet_career.update_acell('E' + str(join_point), nickname)
            if '/' in ctx.author.display_name:
                jupo = fun.convertJupo(ctx.author.display_name)
                bupo = fun.convertBupo(ctx.author.display_name)
                worksheet_list.update_acell('F' + str(join_point), jupo)
                worksheet_list.update_acell('G' + str(join_point), bupo)
            else:
                jupo = fun.convertJupo(ctx.author.display_name)
                worksheet_list.update_acell('F' + str(join_point), jupo)
                worksheet_list.update_acell('G' + str(join_point), '')

            user = ctx.author
            role = get(ctx.guild.roles, name='CEF')
            await user.add_roles(role)
            channel = get(ctx.guild.channels, name='가입-탈퇴-명단')
            await ctx.reply("```복귀를 환영합니다!```"
                                            "필독하셔서 게임 진행이나 서버 이용에 차질 없도록 부탁드리겠습니다.\n```"
                                            "https://cafe.naver.com/cyberearlyfootballc/18267\n"
                                            "저희 C.E.F는 토요일을 제외한 매 저녁 9시부터 11시 30분까지 각 팀에 소속되어 게임하게 됩니다.\n"
                                            f"팀을 구하실 때는 아무런 채널에 '%FA역할부여' 명령어를 사용한 후\n"
                                            f"'팀-홍보' 채널 혹은 '선수-홍보' 채널을 이용하시기 바랍니다.")
            '''await ctx.reply("```복귀를 환영합니다!```"
                                            "필독하셔서 게임 진행이나 서버 이용에 차질 없도록 부탁드리겠습니다.```"
                                            "https://cafe.naver.com/cyberearlyfootballc/18267\n"
                                            "저희 C.E.F는 토요일을 제외한 매 저녁 9시부터 11시 30분까지 각 팀에 소속되어 게임하게 됩니다.\n"
                                            f"팀을 구하실 때는 아무런 채널에 '%FA역할부여' 명령어를 사용한 후\n"
                                            f"{team_channel.mention} 채널 혹은 {player_channel.mention} 채널을 이용하시기 바랍니다.")'''
            await channel.send(content=f"<재가입> {ctx.author.mention} (가입일자 : {now_time})")

        # 신규 & 닉네임 중복일 경우
        elif join_key == False and overlap_check:
            print('신규, 닉네임 중복 있음')
            await ctx.reply("```해당 닉네임은 이미 다른 유저가 사용 중입니다.\n"
                               "다른 닉네임으로 등록해주세요.```"
                               "%검색 닉네임 명령어를 사용하여 사용하고 있는 닉네임을 검색할 수 있습니다.```")
        # 재가입 & 닉네임 중복일 경우
        elif overlap_check and join_key:
            print('재가입, 닉네임 중복 있음')
            print(ovr_point)
            overlap_id = worksheet_list.acell('D' + str(join_point)).value
            # 중복이 본인일 경우
            print(str(overlap_id), str(ctx.author.id))
            if str(overlap_id) == str(ctx.author.id):
                print("중복이 본인임")
                await user.add_roles(cefRole)
                await ctx.reply("```복귀를 환영합니다!```")
                await channel.send(content=f"<재가입> {ctx.author.mention} (가입일자 : {now_time})")
            # 중복이 타 유저일 경우
            else:
                print("중복이 타인임")
                await ctx.reply(content=f"{ctx.author.mention}\n"
                                       f"```해당 닉네임은 다른 유저가 이미 사용 중입니다.\n"
                                       f"다른 닉네임으로 변경해주세요.\n"
                                       f"%검색 닉네임 명령어를 사용하여 사용하고 있는 닉네임을 검색할 수 있습니다.```")
    else:
        await ctx.reply(content=f"```이미 가입되었습니다.```")

# 탈퇴
@bot.command()
async def 탈퇴(ctx):
    now = datetime.datetime.now()
    now_time = now.strftime('%Y-%m-%d %H:%M:%S')

    # 범위(체크)
    cell_max = worksheet_list.acell('A1').value
    # 범위 내 셀 값 로딩
    range_list = worksheet_list.range('D2:D' + cell_max)

    # 스프레드 체크 및 업데이트
    for i, cell in enumerate(range_list):
        if str(cell.value) == str(ctx.author.id):
            check = i + 2
            worksheet_list.update_acell('I' + str(check), now_time)
            key = 1
            break
        else:
            key = 0
    if key == 0:
        await ctx.send(content=f"```스프레드 시트에서 {ctx.author.display_name}님의 이름을 검색할 수 없습니다.\n"
                               f"%가입 명령어를 사용해 스프레드 시트에 등록하거나\n"
                               f"%닉변 명령어를 사용해 닉네임을 업데이트해주세요.```")

# 닉네임 검색
@bot.command(aliases=['searchnick'])
async def 검색(ctx, *, nickname):
    overlap_check = 0
    # 범위(체크)
    cell_max = worksheet_list.acell('A1').value
    # 범위 내 셀 값 로딩
    range_list = worksheet_list.range('D2:D' + cell_max)
    overlap_list = worksheet_list.range('E2:E' + str(cell_max))
    # 스프레드 체크 및 업데이트
    for i, cell in enumerate(overlap_list):
        if str(cell.value) == nickname or str(cell.value) == (nickname + " "):
            overlap_check = 1
            break
        else:
            overlap_check = 0
    if overlap_check == 1:
        await ctx.send(content=f"```검색한 닉네임 : {nickname}\n"
                               f"해당 닉네임은 이미 사용 중이므로, 사용할 수 없습니다.```")
    else:
        await ctx.send(content=f"```검색한 닉네임 : {nickname}\n"
                               f"해당 닉네임은 사용 가능합니다.```")

# 닉네임, 주포, 부포 리셋
@bot.command(aliases=['reset'])
async def 리셋(ctx):
    global SWITCH_NICKNAME_CHANGE
    if SWITCH_NICKNAME_CHANGE == False:
        role_names = [role.name for role in ctx.author.roles]
        key1 = 0
        temp = ctx.author.display_name.split('[')
        nickname = temp[0]
        # 범위(체크)
        cell_max = worksheet_list.acell('A1').value
        # 범위 내 셀 값 로딩
        range_list = worksheet_list.range('D2:D' + cell_max)
        overlap_list = worksheet_list.range('E2:E' + str(cell_max))
        # 스프레드 체크 및 업데이트
        '''
        for i, cell in enumerate(overlap_list):
            if str(cell.value) == nickname or str(cell.value) == (nickname + " "):
                overlap_check = 1
                break
            else:
                overlap_check = 0'''
        if "," in ctx.author.display_name:
            await ctx.send("```정확한 닉네임 양식을 지켜주세요\n"
                           "주 포지션과 부 포지션의 구분은 '/'을 사용해주세요.\n"
                           "해당 봇에서는 ','를 인식하지 않으며, 이는 봇 고장의 원인이 됩니다.\n"
                           "닉네임 양식 : 닉네임[주포지션/부포지션] or 닉네임[주포지션]```")
        elif "." in ctx.author.display_name:
            await ctx.send("```정확한 닉네임 양식을 지켜주세요\n"
                           "주 포지션과 부 포지션의 구분은 '/'을 사용해주세요.\n"
                           "해당 봇에서는 '.'를 인식하지 않으며, 이는 봇 고장의 원인이 됩니다.\n"
                           "닉네임 양식 : 닉네임[주포지션/부포지션] or 닉네임[주포지션]```")
        elif "[" in ctx.author.display_name:
            if '/' in temp[1]:
                a = temp[1].split('/')
                jupo = a[0]
                b = a[1].split(']')
                bupo = b[0]
                for i, cell in enumerate(range_list):
                    if str(cell.value) == str(ctx.author.id):
                        check = i + 2
                        worksheet_list.update_acell('C' + str(check), ctx.author.display_name)
                        worksheet_career.update_acell('C' + str(check), ctx.author.display_name)
                        worksheet_list.update_acell('E' + str(check), nickname)
                        worksheet_career.update_acell('E' + str(check), nickname)
                        worksheet_list.update_acell('F' + str(check), jupo)
                        worksheet_list.update_acell('G' + str(check), bupo)
                        key1 = 1
                        break
                    else:
                        key1 = 0
                await ctx.send(content=f"```{ctx.author.display_name}님의 닉네임, 주포지션, 부포지션이 재업데이트 되었습니다.\n"
                                       f"서버 내 별명 : {ctx.author.display_name}, 닉네임 : {nickname}\n"
                                       f"주포지션 : {jupo}, 부포지션 : {bupo}\n"
                                       f"자세한 사항은 %시트링크 명령어를 입력하여, 시트에서 확인해주세요.```")
            else:
                a = temp[1].split(']')
                jupo = a[0]
                for i, cell in enumerate(range_list):
                    if str(cell.value) == str(ctx.author.id):
                        check = i + 2
                        worksheet_list.update_acell('C' + str(check), ctx.author.display_name)
                        worksheet_career.update_acell('C' + str(check), ctx.author.display_name)
                        worksheet_list.update_acell('E' + str(check), nickname)
                        worksheet_career.update_acell('E' + str(check), nickname)
                        worksheet_list.update_acell('F' + str(check), jupo)
                        worksheet_list.update_acell('G' + str(check), '')
                        key1 = 1
                        break
                    else:
                        key1 = 0
                await ctx.send(content=f"```{ctx.author.display_name}님의 닉네임, 주포지션, 부포지션이 재업데이트 되었습니다.\n"
                                       f"서버 내 별명 : {ctx.author.display_name}, 닉네임 : {nickname}\n"
                                       f"주포지션 : {jupo}, 부포지션 : 없음\n"
                                       f"자세한 사항은 %시트링크 명령어를 입력하여, 시트에서 확인해주세요.```")
        '''else:
            await ctx.send(content=f"{ctx.author.mention}\n"
                                   f"```해당 닉네임은 이미 사용 중입니다.\n"
                                   f"다른 닉네임으로 변경해주세요.```")'''
        if key1 == 0:
            await ctx.send(content=f"```스프레드 시트 명단에서 {ctx.author.display_name}님의 고유 ID 번호를 검색할 수 없습니다.\n```")
    else :
        await ctx.send('```현재 닉네임 변경이 불가합니다.\n'
                       '스태프를 멘션하여 요청해주세요.```')


# 주 포지션 업데이트
@bot.command()
async def 주포변경(ctx, *, text):
    pos_list = ['ST', 'LW', 'RW', 'CAM', 'CM', 'CDM', 'LB', 'CB', 'RB', 'GK']
    key = 0
    # 범위(체크)
    cell_max = worksheet_list.acell('A1').value
    # 범위 내 셀 값 로딩
    range_list = worksheet_list.range('D2:D' + cell_max)
    if text in pos_list:
        # 스프레드 체크 및 업데이트
        for i, cell in enumerate(range_list):
            if str(cell.value) == str(ctx.author.id):
                check = i + 2
                ex_bupo = worksheet_list.acell('F' + str(check)).value
                worksheet_list.update_acell('F' + str(check), text)
                worksheet_list.update_acell('C' + str(check), ctx.author.display_name)
                await ctx.send(content=f"```주포지션 변경을 정상적으로 업데이트하였습니다.\n"
                                       f"이전 주포지션 : {ex_bupo} --> 현재 주포지션 : {text}\n"
                                       f"디스코드 내 닉네임은 직접 변경해주세요.```")
                key = 1
                break
            else:
                key = 0

        if key == 0:
            await ctx.send(content=f"```스프레드 시트에서 {ctx.author.display_name}님의 이름을 검색할 수 없습니다.\n"
                                   f"%가입 명령어를 사용해 스프레드 시트에 등록하거나\n"
                                   f"%닉변 명령어를 사용해 닉네임을 업데이트해주세요.```")
    else:
        await ctx.send("포지션을 잘못 입력하였습니다.")


# 부 포지션 업데이트
@bot.command()
async def 부포변경(ctx, *, text):
    key = 0
    # 범위(체크)
    cell_max = worksheet_list.acell('A1').value
    # 범위 내 셀 값 로딩
    range_list = worksheet_list.range('D2:D' + cell_max)
    pos_list = ['ST', 'LW', 'RW', 'CAM', 'CM', 'CDM', 'LB', 'CB', 'RB', 'GK']
    if text in pos_list:
        # 스프레드 체크 및 업데이트
        for i, cell in enumerate(range_list):
            if str(cell.value) == str(ctx.author.id):
                print(i)
                check = i + 2
                ex_bupo = worksheet_list.acell('G' + str(check)).value
                if ex_bupo == "":
                    ex_bupo = '없음'
                worksheet_list.update_acell('G' + str(check), text)
                worksheet_list.update_acell('C' + str(check), ctx.author.display_name)
                key = 1
                await ctx.send(content=f"```부포지션 변경을 정상적으로 업데이트하였습니다.\n"
                                       f"이전 부포지션 : {ex_bupo} --> 현재 부포지션 : {text}\n"
                                       f"디스코드 내 닉네임은 직접 변경해주세요.```")
                break
            else:
                key = 0

        if key == 0:
            await ctx.send(content=f"```스프레드 시트에서 {ctx.author.display_name}님의 이름을 검색할 수 없습니다.\n"
                                   f"%가입 명령어를 사용해 스프레드 시트에 등록하거나\n"
                                   f"%닉변 명령어를 사용해 닉네임을 업데이트해주세요.```")

    else:
        await ctx.send("포지션을 잘못 입력하였습니다.")


@bot.command()
async def 색깔(ctx):
    color_list = ["빨강", "노랑", "파랑", "보라", "검정", "흰색"]
    color = random.choice(color_list)
    await ctx.send(content=f"{color}")


# 부 포지션 삭제
@bot.command()
async def 부포삭제(ctx):
    key = 0
    # 범위(체크)
    cell_max = worksheet_list.acell('A1').value
    # 범위 내 셀 값 로딩
    range_list = worksheet_list.range('D2:D' + cell_max)

    # 스프레드 체크 및 업데이트
    for i, cell in enumerate(range_list):
        if str(cell.value) == str(ctx.author.id):
            print(i)
            check = i + 2
            worksheet_list.update_acell('G' + str(check), '')
            worksheet_list.update_acell('C' + str(check), ctx.author.display_name)
            key = 1
            await ctx.send(content=f"```부포지션을 정상적으로 삭제하였습니다.\n"
                                   f"디스코드 내 닉네임은 직접 수정해주세요.```")
            break
        else:
            key = 0

    if key == 0:
        await ctx.send(content=f"```스프레드 시트에서 {ctx.author.display_name}님의 이름을 검색할 수 없습니다.\n"
                               f"%가입 명령어를 사용해 스프레드 시트에 등록하거나\n"
                               f"%닉변 명령어를 사용해 닉네임을 업데이트해주세요.```")

'''
# 닉네임 업데이트
@bot.command()
async def 닉변(ctx):
    global SWITCH_NICKNAME_CHANGE

    if SWITCH_NICKNAME_CHANGE:
        role_names = [role.name for role in ctx.author.roles]

        #if not "신규" in role_names: # '신규' 역할이 있을 시
        #    await ctx.send("```현재 닉네임 변경 기간이 아닙니다.\n"
        #                   "2월의 닉변 변경일은 2월 12일, 26일 입니다.```")
        
        #if "신규" in role_names: # '신규' 역할이 없을 시

        key = 0

        # 범위(체크)
        cell_max = worksheet_list.acell('A1').value
        a_max = str(int(worksheet_check_A.acell('A1').value) + 1)
        b_max = str(int(worksheet_check_B.acell('A1').value) + 1)
        c_max = str(int(worksheet_check_C.acell('A1').value) + 1)
        d_max = str(int(worksheet_check_D.acell('A1').value) + 1)
        # 범위 내 셀 값 로딩
        range_list = worksheet_list.range('D2:D' + cell_max)
        nickname_list = worksheet_list.range('E2:E' + cell_max)
        team_a_list = worksheet_check_A.range('C3:C' + a_max)
        team_b_list = worksheet_check_B.range('C3:C' + b_max)
        team_c_list = worksheet_check_C.range('C3:C' + c_max)
        team_d_list = worksheet_check_D.range('C3:C' + d_max)
        temp = ctx.author.display_name.split('[')
        nickname = temp[0]
        check = 0
        overlap_list = worksheet_list.range('E2:E' + str(cell_max))

        for i, cell in enumerate(range_list):
            if str(cell.value) == str(ctx.author.id):
                check = i + 2
                ex_temp = worksheet_list.acell('C' + str(check)).value
                ex_temp2 = ex_temp.split('[')
                ex_name = ex_temp2[0]
                break

        # 스프레드 체크 및 업데이트
        if ex_name != nickname:
            for i, cell in enumerate(range_list):
                if str(cell.value) == str(ctx.author.id):
                    check = i + 2
                    worksheet_list.update_acell('C' + str(check), ctx.author.display_name)
                    worksheet_list.update_acell('E' + str(check), str(nickname))
                    worksheet_career.update_acell('C' + str(check), ctx.author.display_name)
                    worksheet_career.update_acell('E' + str(check), str(nickname))
                    if "TEAM_A" in role_names:
                        for j, cell2 in enumerate(team_a_list):
                            if str(cell2.value) == str(ctx.author.id):
                                check = j + 3
                                worksheet_check_A.update_acell('B' + str(check), ctx.author.display_name)
                                break
                    elif "TEAM_B" in role_names:
                        for j, cell2 in enumerate(team_b_list):
                            if str(cell2.value) == str(ctx.author.id):
                                check = j + 3
                                worksheet_check_B.update_acell('B' + str(check), ctx.author.display_name)
                                break
                    elif "TEAM_C" in role_names:
                        for j, cell2 in enumerate(team_c_list):
                            if str(cell2.value) == str(ctx.author.id):
                                check = j + 3
                                worksheet_check_C.update_acell('B' + str(check), ctx.author.display_name)
                                break
                    elif "TEAM_D" in role_names:
                        for j, cell2 in enumerate(team_d_list):
                            if str(cell2.value) == str(ctx.author.id):
                                check = j + 3
                                worksheet_check_D.update_acell('B' + str(check), ctx.author.display_name)
                                break
                    key = 1

                    await ctx.send(
                        content=f"```닉네임 변경을 정상적으로 업데이트하였습니다.\n"
                                f"이전 닉네임 : {ex_name} --> 현재 닉네임 : {nickname}\n"
                                f"디스코드 내 닉네임은 직접 수정해주세요.\n"
                                f"닉네임변경 명령어는 디스코드 내 닉네임을 먼저 수정한 후 사용해야 정상적으로 처리됩니다.```")
                    break
                else:
                    key = 0
            if key == 0:
                await ctx.send(content=f"```스프레드 시트에서 {ctx.author.display_name}님의 이름을 검색할 수 없습니다.\n"
                                       f"%가입 명령어를 사용해 스프레드 시트에 등록하거나\n"
                                       f"%닉변 명령어를 사용해 닉네임을 업데이트해주세요.```")
        else:
            await ctx.send(content=f"{ctx.author.mention}\n"
                                   f"```이전의 닉네임과 현재 변경하려는 닉네임이 일치합니다.\n"
                                   f"디스코드 내 닉네임을 먼저 수정한 후 다시 사용해주세요.```")
        #else:
            #await ctx.send(content=f"{ctx.author.mention}\n"
                                   #f"```해당 닉네임은 이미 사용 중입니다.\n"
                                   #f"다른 닉네임으로 변경해주세요.```")
    else:
        await ctx.send('닉네임 변경 기간이 아닙니다.')
    await ctx.message.delete()
    
'''

# 역할 부여하기
@bot.command()
async def 역할부여(ctx, team_name, member: discord.Member, position, price):
    ju_po = ""
    print(team_name)
    ownRoles = [role.name for role in ctx.author.roles]
    convertprice = int(price) * 100000000
    addWallet = convertprice * 0.00001
    await ctx.message.delete()
    if '스태프' in ownRoles:
        key = 0
        role = get(member.guild.roles, name=fun.teamNameConvert(team_name))
        id_num = "" + str(member.id)
        # 오타체크
        team_name_list = ["TEAM_A", "TEAM_B", "TEAM_C", "TEAM_D", "TEAM_E"]
        position_list = ["ST", "LW", "RW", "CAM", "CM", "CDM", "LB", "CB", "RB", "GK"]
        print(role, role.name)
        if role.name in team_name_list:
            print(role.name)
            teamname_error = 1
        else:
            teamname_error = 0

        print(teamname_error)

        if position in position_list:
            position_error = 1
        else:
            position_error = 0
        print(position_error)
        # 범위(체크)
        cell_max = worksheet_list.acell('A1').value
        a_max = worksheet_check_A.acell('A1').value
        b_max = worksheet_check_B.acell('A1').value
        c_max = worksheet_check_C.acell('A1').value
        d_max = worksheet_check_D.acell('A1').value
        e_max = worksheet_check_E.acell('A1').value
        # 범위 내 셀 값 로딩
        range_list = worksheet_list.range('E2:E' + cell_max)
        temp = member.display_name.split('[')
        nickname = temp[0]
        # 스프레드 체크 및 업데이트
        for i, cell in enumerate(range_list):
            if str(cell.value) == str(nickname) or str(cell.value) + " " == str(nickname):
                check = i + 2
                list_pos = i
                key = 1
                break
        if teamname_error == 1 & key == 1 & position_error == 1:
            beforePresentWallet = worksheet_career.acell('R' + str(list_pos + 2)).value
            beforeTotalWallet = worksheet_career.acell('S' + str(list_pos + 2)).value
            print(beforePresentWallet, addWallet)
            presentWallet = int(beforePresentWallet) + int(addWallet)
            TotalWallet = int(beforeTotalWallet) + int(addWallet)
            worksheet_career.update_acell('Q' + str(list_pos + 2), str(price))
            #worksheet_career.update_acell('R' + str(list_pos + 2), str(TotalWallet))
            worksheet_list.update_acell('H' + str(list_pos + 2), fun.teamNameConvert(team_name))
            await member.add_roles(role)
            await ctx.send(content=f"<소속 변경>\n"
                                   f"{member.mention} -> {fun.teamNameConvert(team_name)} 배정 (선발 포지션 : {position})\n"
                                   f"이적료는 {price} 억원이며, 개인자산으로 {fun.caculateUnit(addWallet)} 지급되었습니다.")

            if fun.teamNameConvert(team_name) == "TEAM_A":
                worksheet_check_A.insert_row(["", member.display_name, id_num, position, 0, 0, 0, 0, 0], int(a_max) + 2)
            elif fun.teamNameConvert(team_name) == "TEAM_B":
                worksheet_check_B.insert_row(["", member.display_name, id_num, position, 0, 0, 0, 0, 0], int(b_max) + 2)
            elif fun.teamNameConvert(team_name) == "TEAM_C":
                worksheet_check_C.insert_row(["", member.display_name, id_num, position, 0, 0, 0, 0, 0], int(c_max) + 2)
            elif fun.teamNameConvert(team_name) == "TEAM_D":
                worksheet_check_D.insert_row(["", member.display_name, id_num, position, 0, 0, 0, 0, 0], int(d_max) + 2)
            elif fun.teamNameConvert(team_name) == "TEAM_E":
                worksheet_check_E.insert_row(["", member.display_name, id_num, position, 0, 0, 0, 0, 0], int(e_max) + 2)
        elif teamname_error == 0:
            await ctx.send("팀 이름 오타 체크해주세요.")
        elif position_error == 0:
            await ctx.send("포지션 오타 체크해주세요.")
        elif key == 0:
            await ctx.send(content=f"<소속 변경 실패>\n"
                                   f"스프레드 시트에서 {member.display_name}님의 이름을 검색할 수 없습니다.\n"
                                   f"%가입 명령어를 사용해 스프레드 시트에 등록하거나\n"
                                   f"%닉변 명령어를 사용해 닉네임을 업데이트해주세요.")

    else:
        await ctx.send("```해당 명령어는 스태프만 사용 가능합니다.```")

# 역할 부여하기
@bot.command()
async def 이적(ctx, team_name, member: discord.Member, position):
    ju_po = ""
    print(team_name)
    ownRoles = [role.name for role in ctx.author.roles]
    #convertprice = int(price) * 100000000
    #addWallet = convertprice * 0.00001
    await ctx.message.delete()
    if '스태프' in ownRoles:
        key = 0
        role = get(member.guild.roles, name=fun.teamNameConvert(team_name))
        id_num = "" + str(member.id)
        li = ['TEAM A', 'TEAM B', 'TEAM C', 'TEAM D', 'TEAM E']
        for role in li :
            await member.remove_roles(role)
        # 오타체크
        team_name_list = ["TEAM_A", "TEAM_B", "TEAM_C", "TEAM_D", "TEAM_E"]
        position_list = ["ST", "LW", "RW", "CAM", "CM", "CDM", "LB", "CB", "RB", "GK"]
        print(role, role.name)
        if role.name in team_name_list:
            print(role.name)
            teamname_error = 1
        else:
            teamname_error = 0

        print(teamname_error)

        if position in position_list:
            position_error = 1
        else:
            position_error = 0
        print(position_error)
        # 범위(체크)
        cell_max = worksheet_list.acell('A1').value
        a_max = worksheet_check_A.acell('A1').value
        b_max = worksheet_check_B.acell('A1').value
        c_max = worksheet_check_C.acell('A1').value
        d_max = worksheet_check_D.acell('A1').value
        e_max = worksheet_check_E.acell('A1').value
        # 범위 내 셀 값 로딩
        range_list = worksheet_list.range('E2:E' + cell_max)
        temp = member.display_name.split('[')
        nickname = temp[0]
        # 스프레드 체크 및 업데이트
        for i, cell in enumerate(range_list):
            if str(cell.value) == str(nickname) or str(cell.value) + " " == str(nickname):
                check = i + 2
                list_pos = i
                key = 1
                break
        if teamname_error == 1 & key == 1 & position_error == 1:
            beforePresentWallet = worksheet_career.acell('R' + str(list_pos + 2)).value
            beforeTotalWallet = worksheet_career.acell('S' + str(list_pos + 2)).value
            #print(beforePresentWallet, addWallet)
            #presentWallet = int(beforePresentWallet) + int(addWallet)
            #TotalWallet = int(beforeTotalWallet) + int(addWallet)
            #worksheet_career.update_acell('Q' + str(list_pos + 2), str(price))
            #worksheet_career.update_acell('R' + str(list_pos + 2), str(TotalWallet))
            worksheet_list.update_acell('H' + str(list_pos + 2), fun.teamNameConvert(team_name))
            await member.add_roles(role)
            await ctx.send(content=f"<소속 변경>\n"
                                   f"{member.mention} -> {fun.teamNameConvert(team_name)} 팀으로 이적 (선발 포지션 : {position})\n")

            if fun.teamNameConvert(team_name) == "TEAM_A":
                worksheet_check_A.insert_row(["", member.display_name, id_num, position, 0, 0, 0, 0, 0], int(a_max) + 2)
            elif fun.teamNameConvert(team_name) == "TEAM_B":
                worksheet_check_B.insert_row(["", member.display_name, id_num, position, 0, 0, 0, 0, 0], int(b_max) + 2)
            elif fun.teamNameConvert(team_name) == "TEAM_C":
                worksheet_check_C.insert_row(["", member.display_name, id_num, position, 0, 0, 0, 0, 0], int(c_max) + 2)
            elif fun.teamNameConvert(team_name) == "TEAM_D":
                worksheet_check_D.insert_row(["", member.display_name, id_num, position, 0, 0, 0, 0, 0], int(d_max) + 2)
            elif fun.teamNameConvert(team_name) == "TEAM_E":
                worksheet_check_E.insert_row(["", member.display_name, id_num, position, 0, 0, 0, 0, 0], int(e_max) + 2)
        elif teamname_error == 0:
            await ctx.send("팀 이름 오타 체크해주세요.")
        elif position_error == 0:
            await ctx.send("포지션 오타 체크해주세요.")
        elif key == 0:
            await ctx.send(content=f"<소속 변경 실패>\n"
                                   f"스프레드 시트에서 {member.display_name}님의 이름을 검색할 수 없습니다.\n"
                                   f"%가입 명령어를 사용해 스프레드 시트에 등록하거나\n"
                                   f"%닉변 명령어를 사용해 닉네임을 업데이트해주세요.")

    else:
        await ctx.send("```해당 명령어는 스태프만 사용 가능합니다.```")


# 역할 회수하기
@bot.command()
async def 역할회수(ctx, team_name):
    role_names = [role.name for role in ctx.author.roles]
    if '스태프' in role_names:
        role = get(ctx.guild.roles, name=team_name)
        team_mem = []
        print(role)
        # 오타체크
        role_list = ["TEAM_A", "TEAM_B", "TEAM_C", "TEAM_D"]
        if role.name in role_list:
            type_error = 1
        else:
            type_error = 0
        # 범위(체크)
        cell_max = worksheet_list.acell('A1').value
        # 범위 내 셀 값 로딩
        range_list = worksheet_list.range('H2:H' + cell_max)

        if type_error == 1:
            # 시트 내에서 소속 업데이트
            for i, cell in enumerate(range_list):
                # print(str(i) + " / " + cell.value)
                if str(cell.value) == team_name:
                    temp = i + 2
                    data = worksheet_list.acell('H' + str(temp)).value
                    worksheet_list.update_acell('H' + str(temp), '무소속')
                    # print(temp, data)
                    if data == role:
                        team_mem.append(worksheet_list.acell('C' + str(temp)).value)
            # await ctx.message.delete()
            await ctx.send(content=f"{team_name} 역할을 전원 회수하였습니다.")
        else:
            await ctx.send("오타 및 팀명 체크")

        # 디스코드 내 역할 업데이트
        empty = True
        for member in ctx.guild.members:
            if role in member.roles:
                await ctx.guild.member.remove_roles(role)
                empty = False
        if empty == False:
            await ctx.send("Anyone has this role")
    else:
        await ctx.send("```해당 명령어는 스태프만 사용 가능합니다.```")


# 선수 커리어 관리
@bot.command()
async def 커리어(ctx, text, member: discord.Member):
    key = 0
    name = member.display_name.split('[')
    role_names = [role.name for role in ctx.author.roles]
    if "스태프" in role_names:
        # 범위(체크)
        cell_max = worksheet_list.acell('A1').value
        # 범위 내 셀 값 로딩
        range_list = worksheet_list.range('E2:E' + cell_max)
        temp = member.display_name.split('[')
        nickname = temp[0]

        # 스프레드 체크 및 업데이트
        if text == '선수':
            for i, cell in enumerate(range_list):
                if str(cell.value) == str(nickname):
                    check = i + 2
                    # 우승 횟수
                    before = worksheet_career.acell('F' + str(check)).value
                    now = int(before) + 1
                    worksheet_career.update_acell('F' + str(check), str(now))
                    key = 1
                    await ctx.send(content=f"```cs\n"
                                           f"{name[0]}님의 선수 커리어가 정상적으로 업데이트되었습니다.\n"
                                           f"이전 선수 우승횟수 : {before} --> 현재 선수 우승횟수 : {now}```")

                    break
                else:
                    key = 0


        elif text == '코치':
            for i, cell in enumerate(range_list):
                if str(cell.value) == str(nickname):
                    check = i + 2
                    before = worksheet_career.acell('G' + str(check)).value
                    now = int(before) + 1
                    worksheet_career.update_acell('G' + str(check), str(now))
                    key = 1
                    await ctx.send(content=f"```cs\n"
                                           f"{name[0]}님의 주장 커리어가 정상적으로 업데이트되었습니다.\n"
                                           f"이전 주장 우승횟수 : {before} --> 현재 주장 우승횟수 : {now}```")
                    break
                else:
                    key = 0
        if key == 0:
            await ctx.send(content=f"```스프레드 시트에서 {member.display_name}님의 이름을 검색할 수 없습니다.\n"
                                   f"%가입 명령어를 사용해 스프레드 시트에 등록하거나\n"
                                   f"%닉변 명령어를 사용해 닉네임을 업데이트해주세요.```")

    else:
        await ctx.send("```해당 명령어는 스태프만 사용 가능합니다.```")


# 내 정보 보기
@bot.command(aliases=['myinfo'])
async def 내정보(ctx):
    key = 0
    # 범위(체크)
    cell_max = worksheet_list.acell('A1').value
    # 범위 내 셀 값 로딩
    range_list = worksheet_list.range('D2:D' + cell_max)
    # 스프레드 체크 및 업데이트
    '''if str(ctx.message.channel) != "내정보-열람실📜":
    #if str(ctx.message.channel) != "프클-공지사항📝":
        await ctx.send("내정보-열람실📜 채널에서 사용해주세요.")
    else:'''
    for i, cell in enumerate(range_list):
        if str(cell.value) == str(ctx.author.id):
            check = i + 2
            key = 1
            team = worksheet_list.acell('H' + str(check)).value
            player_win = worksheet_career.acell('F' + str(check)).value
            coach_win = worksheet_career.acell('G' + str(check)).value
            to_fw = worksheet_career.acell('H' + str(check)).value
            to_mf = worksheet_career.acell('I' + str(check)).value
            to_df = worksheet_career.acell('J' + str(check)).value
            to_gk = worksheet_career.acell('K' + str(check)).value
            total_to = worksheet_career.acell('L' + str(check)).value
            before_to = worksheet_career.acell('M' + str(check)).value
            val = worksheet_career.acell('N' + str(check)).value
            before_val = worksheet_career.acell('O' + str(check)).value
            naejeon = worksheet_career.acell('P' + str(check)).value
            #price = worksheet_career.acell('Q' + str(check)).value
            #presentWallet = worksheet_career.acell('R' + str(check)).value
            #totalWallet = worksheet_career.acell('S' + str(check)).value

    if key == 1:
        if "/" in ctx.author.display_name:
            temp = ctx.author.display_name.split('[')
            a = temp[1].split('/')
            jupo = a[0]
            b = a[1].split(']')
            bupo = b[0]

            embed = discord.Embed(title=f"내 정보", description=f"{ctx.author.display_name} 님의 정보창", color=0xFF007F)
            #embed.add_field(name="이적료", value=price + " 억원", inline=True)
            #embed.add_field(name="현재 자산", value=fun.caculateUnit(presentWallet), inline=True)
            #embed.add_field(name="누적 자산", value=fun.caculateUnit(totalWallet), inline=True)
            embed.add_field(name="소속팀", value=f"{team}", inline=True)
            embed.add_field(name="주포지션", value=jupo, inline=True)
            embed.add_field(name="부포지션", value=bupo, inline=True)
            embed.add_field(name="우승 기록", value=f"선수 : {player_win} 회\n"
                                                  f"감독 : {coach_win} 회\n"
                                                  f"내전 리그 : {naejeon} 회", inline=True)
            embed.add_field(name="수상 내역", value=f"토츠 : 총 {total_to} 회\n"
                                                  f"- FW : {to_fw} 회\n"
                                                  f"- MF : {to_mf} 회\n"
                                                  f"- DF : {to_df} 회\n"
                                                  f"- GK : {to_gk} 회\n"
                                                  f"발롱도르 : {val} 회\n", inline=True)
            embed.add_field(name="이전 수상 내역", value=f"토츠 : {before_to} 회\n"
                                                       f"발롱도르 : {before_val} 회", inline=True)
            embed.set_footer(text="Copyright ⓒ 2020-2021 타임제이(TimeJ) in C.E.F All Right Reserved.")

            await ctx.send(embed=embed)
        else:
            temp = ctx.author.display_name.split('[')
            a = temp[1].split(']')
            jupo = a[0]
            bupo = "없음"

            embed = discord.Embed(title=f"내 정보", description=f"{ctx.author.display_name} 님의 정보창", color=0xFF007F)
            #embed.add_field(name="이적료", value=price + " 억원", inline=True)
            #embed.add_field(name="현재 자산", value=fun.caculateUnit(presentWallet), inline=True)
            #embed.add_field(name="누적 자산", value=fun.caculateUnit(totalWallet), inline=True)
            embed.add_field(name="소속팀", value=f"{team}", inline=True)
            embed.add_field(name="주포지션", value=jupo, inline=True)
            embed.add_field(name="부포지션", value=bupo, inline=True)
            embed.add_field(name="우승 기록", value=f"선수 : {player_win} 회\n"
                                                  f"감독 : {coach_win} 회\n"
                                                  f"내전 리그 : {naejeon} 회", inline=True)
            embed.add_field(name="수상 내역", value=f"토츠 : 총 {total_to} 회\n"
                                                  f"- FW : {to_fw} 회\n"
                                                  f"- MF : {to_mf} 회\n"
                                                  f"- DF : {to_df} 회\n"
                                                  f"- GK : {to_gk} 회\n"
                                                  f"발롱도르 : {val} 회\n", inline=True)
            embed.add_field(name="이전 수상 내역", value=f"토츠 : {before_to} 회\n"
                                                       f"발롱도르 : {before_val} 회", inline=True)
            embed.set_footer(text="Copyright ⓒ 2020-2021 타임제이(TimeJ) in C.E.F All Right Reserved.")


            await ctx.send(embed=embed)
    else:
        await ctx.send(content=f"```스프레드 시트에서 {ctx.author.display_name}님의 이름을 검색할 수 없습니다.\n"
                               f"%가입 명령어를 사용해 스프레드 시트에 등록하거나\n"
                               f"%닉변 명령어를 사용해 닉네임을 업데이트해주세요.```")


@bot.command()
async def 발롱도르(ctx, member: discord.Member):
    key = 0
    role_names = [role.name for role in ctx.author.roles]
    # 범위(체크)
    cell_max = worksheet_list.acell('A1').value
    # 범위 내 셀 값 로딩
    range_list = worksheet_list.range('E2:E' + cell_max)
    temp = member.display_name.split('[')
    nickname = temp[0]
    if "스태프" in role_names:
        # 중복 체크
        for cell in range_list:
            if cell.value == nickname:
                key = 1
                print(key)
                print(str(cell.value) + " / " + str(member.display_name))
                break
            else:
                key = 0
                print(key)
                print(str(cell.value) + " / " + str(member.display_name))

        # 스프레드 체크 및 업데이트
        if key == 1:
            for i, cell in enumerate(range_list):
                if str(cell.value) == str(nickname):
                    print(1)
                    check = i + 2
                    before = worksheet_career.acell('N' + str(check)).value
                    now_num = int(before) + 1
                    worksheet_career.update_acell('N' + str(check), str(now_num))
                    await ctx.send(content=f"```cs\n"
                                           f"{member.display_name} 님의 발롱도르 업데이트가 정상적으로 되었습니다.\n"
                                           f"이전 기록 : {before}회 --> 현재 기록 : {now_num}회```")
                else:
                    print(2)
        else:
            await ctx.send(content=f"```스프레드 시트에서 {member.display_name}님의 이름을 검색할 수 없습니다.\n"
                                   f"%가입 명령어를 사용해 스프레드 시트에 등록하거나\n"
                                   f"%닉변 명령어를 사용해 닉네임을 업데이트해주세요.```")
    else:
        await ctx.send("```해당 명령어는 스태프만 사용가능합니다.```")


@bot.command()
async def 토츠(ctx, position, member: discord.Member):
    role_names = [role.name for role in ctx.author.roles]
    # 범위(체크)
    cell_max = worksheet_list.acell('A1').value
    # 범위 내 셀 값 로딩
    range_list = worksheet_list.range('E2:E' + cell_max)
    temp = member.display_name.split('[')
    nickname = temp[0]
    # 중복 체크
    for cell in range_list:
        if cell.value == nickname:
            key = 1
            break
        else:
            key = 0
    check = 1
    if "스태프" in role_names:
        # 스프레드 체크 및 업데이트
        if key == 1:
            if position == 'FW':
                for i, cell in enumerate(range_list):
                    if str(cell.value) == str(nickname):
                        check = i + 2
                        before = worksheet_career.acell('H' + str(check)).value
                        before_to = worksheet_career.acell('L' + str(check)).value
                        now_to = int(before_to) + 1
                        now_num = int(before) + 1
                        worksheet_career.update_acell('H' + str(check), now_num)
                        worksheet_career.update_acell('L' + str(check), now_to)
                        await ctx.send(content=f"```cs\n"
                                               f"{member.display_name} 님의 토츠 FW 항목이 정상적으로 업데이트 되었습니다.\n"
                                               f"이전 FW 토츠 기록 : {before}회 --> 현재 토츠 FW 기록 : {now_num}회\n"
                                               f"이전 총 토츠 기록 : {before_to}회 --> 현재 총 토츠 기록 : {now_to}회```")
            elif position == 'MF':
                for i, cell in enumerate(range_list):
                    if str(cell.value) == str(nickname):
                        check = i + 2
                        before = worksheet_career.acell('I' + str(check)).value
                        before_to = worksheet_career.acell('L' + str(check)).value
                        now_to = int(before_to) + 1
                        now_num = int(before) + 1
                        worksheet_career.update_acell('I' + str(check), now_num)
                        worksheet_career.update_acell('L' + str(check), now_to)
                        await ctx.send(content=f"```cs\n"
                                               f"{member.display_name} 님의 토츠 MF 항목이 정상적으로 업데이트 되었습니다.\n"
                                               f"이전 MF 토츠 기록 : {before}회 --> 현재 토츠 MF 기록 : {now_num}회\n"
                                               f"이전 총 토츠 기록 : {before_to}회 --> 현재 총 토츠 기록 : {now_to}회```")
            elif position == 'DF':
                for i, cell in enumerate(range_list):
                    if str(cell.value) == str(nickname):
                        check = i + 2
                        before = worksheet_career.acell('J' + str(check)).value
                        before_to = worksheet_career.acell('L' + str(check)).value
                        now_to = int(before_to) + 1
                        now_num = int(before) + 1
                        worksheet_career.update_acell('J' + str(check), now_num)
                        worksheet_career.update_acell('L' + str(check), now_to)
                        await ctx.send(content=f"```cs\n"
                                               f"{member.display_name} 님의 토츠 DF 항목이 정상적으로 업데이트 되었습니다.\n"
                                               f"이전 DF 토츠 기록 : {before}회 --> 현재 토츠 DF 기록 : {now_num}회\n"
                                               f"이전 총 토츠 기록 : {before_to}회 --> 현재 총 토츠 기록 : {now_to}회```")
            elif position == 'GK':
                for i, cell in enumerate(range_list):
                    if str(cell.value) == str(nickname):
                        check = i + 2
                        before = worksheet_career.acell('K' + str(check)).value
                        before_to = worksheet_career.acell('L' + str(check)).value
                        now_to = int(before_to) + 1
                        now_num = int(before) + 1
                        worksheet_career.update_acell('K' + str(check), now_num)
                        worksheet_career.update_acell('L' + str(check), now_to)
                        await ctx.send(content=f"```cs\n"
                                               f"{member.display_name} 님의 토츠 GK 항목이 정상적으로 업데이트 되었습니다.\n"
                                               f"이전 GK 토츠 기록 : {before}회 --> 현재 토츠 GK 기록 : {now_num}회\n"
                                               f"이전 총 토츠 기록 : {before_to}회 --> 현재 총 토츠 기록 : {now_to}회```")
            else:
                await ctx.send("포지션이 잘못 입력되었습니다.")
        else:
            await ctx.send(content=f"```스프레드 시트에서 {member.display_name}님의 이름을 검색할 수 없습니다.\n"
                                   f"%가입 명령어를 사용해 스프레드 시트에 등록하거나\n"
                                   f"%닉변 명령어를 사용해 닉네임을 업데이트해주세요.```")
    else:
        await ctx.send("```해당 명령어는 스태프만 사용가능합니다.```")


@bot.command(aliases=['check', '출'])
async def 출석(ctx, game):
    time_now = datetime.datetime.now()
    time_1st = datetime.datetime(time_now.year, time_now.month, time_now.day, 20, 30, 00)
    time_2nd = datetime.datetime(time_now.year, time_now.month, time_now.day, 21, 00, 00)
    time_3rd = datetime.datetime(time_now.year, time_now.month, time_now.day, 21, 30, 00)
    time_4th = datetime.datetime(time_now.year, time_now.month, time_now.day, 22, 00, 00)
    time_after = datetime.datetime(time_now.year, time_now.month, time_now.day, 23, 00, 00)
    now_month = time_now.strftime('%m')
    now_day = time_now.strftime('%d')
    role_names = [role.name for role in ctx.author.roles]
    # 범위(체크)
    # 범위 내 셀 값 로딩

    if str(ctx.message.channel) == 'team-a-출석조사':
        if "TEAM_A" in role_names:  # A팀 역할 있는지 체크
            a_max = str(int(worksheet_check_A.acell('A1').value) + 2)
            team_a_list = worksheet_check_A.range('C3:C' + a_max)
            for i, cell in enumerate(team_a_list):  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id):
                    temp = i + 3
                    if game == '1':
                        if time_1st < time_now and time_now < time_after:
                            await ctx.send(content=f"1경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_1st} 까지")
                        else:
                            if worksheet_check_A.acell('E' + str(temp)).value == '체크':
                                await ctx.send(content=f"{game}경기 : 이미 출석체크 되었습니다.")
                            else:
                                worksheet_check_A.update_acell('E' + str(temp), '체크')
                                count = worksheet_check_A.acell('I' + str(temp)).value
                                count = int(count) + 1
                                worksheet_check_A.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 A팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"정상적으로 출석참가 되었습니다.```")
                    elif game == '2':
                        if time_2nd < time_now and time_now < time_after:
                            await ctx.send(content=f"2경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_2nd} 까지")
                        else:
                            if worksheet_check_A.acell('F' + str(temp)).value == '체크':
                                await ctx.send(content=f"{game}경기 : 이미 출석체크 되었습니다.")
                            else:
                                worksheet_check_A.update_acell('F' + str(temp), '체크')
                                count = worksheet_check_A.acell('I' + str(temp)).value
                                count = int(count) + 1
                                worksheet_check_A.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 A팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"정상적으로 출석참가 되었습니다.```")

                    elif game == '3':
                        if time_3rd < time_now and time_now < time_after:
                            await ctx.send(content=f"3경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_3rd} 까지")
                        else:
                            if worksheet_check_A.acell('G' + str(temp)).value == '체크':
                                await ctx.send(content=f"{game}경기 : 이미 출석체크 되었습니다.")
                            else:
                                worksheet_check_A.update_acell('G' + str(temp), '체크')
                                count = worksheet_check_A.acell('I' + str(temp)).value
                                count = int(count) + 1
                                worksheet_check_A.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 A팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"정상적으로 출석참가 되었습니다.```")
                    elif game == '4':
                        if time_4th < time_now and time_now < time_after:
                            await ctx.send(content=f"4경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_4th} 까지")
                        else:
                            if worksheet_check_A.acell('H' + str(temp)).value == '체크':
                                await ctx.send(content=f"{game}경기 : 이미 출석체크 되었습니다.")
                            else:
                                worksheet_check_A.update_acell('H' + str(temp), '체크')
                                count = worksheet_check_A.acell('I' + str(temp)).value
                                count = int(count) + 1
                                worksheet_check_A.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 A팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"정상적으로 출석참가 되었습니다.```")
                    else:
                        await ctx.send("```입력이 잘못되었습니다.```")
        else:
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_A 소속이 아닙니다.```")
    elif str(ctx.message.channel) == 'team-b-출석조사':
        if "TEAM_B" in role_names:  # B팀 역할 있는지 체크
            b_max = str(int(worksheet_check_B.acell('A1').value) + 2)
            team_b_list = worksheet_check_B.range('C3:C' + b_max)
            for i, cell in enumerate(team_b_list):  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id):
                    temp = i + 3
                    jupo = worksheet_check_B.acell('D' + str(temp)).value
                    if game == '1' :
                        if time_1st < time_now and time_now < time_after :
                            await ctx.send(content=f"1경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_1st} 까지")
                        else :
                            if worksheet_check_B.acell('E' + str(temp)).value == '체크':
                                await ctx.send(content=f"{game}경기 : 이미 출석체크 되었습니다.")
                            else:
                                worksheet_check_B.update_acell('E' + str(temp), '체크')
                                count = worksheet_check_B.acell('I' + str(temp)).value
                                count = int(count) + 1
                                worksheet_check_B.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 B팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"정상적으로 출석참가 되었습니다.```")
                    elif game == '2' :
                        if time_2nd < time_now and time_now < time_after :
                            await ctx.send(content=f"2경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_2nd} 까지")
                        else :
                            if worksheet_check_B.acell('F' + str(temp)).value == '체크':
                                await ctx.send(content=f"{game}경기 : 이미 출석체크 되었습니다.")
                            else:
                                worksheet_check_B.update_acell('F' + str(temp), '체크')
                                count = worksheet_check_B.acell('I' + str(temp)).value
                                count = int(count) + 1
                                worksheet_check_B.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 B팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"정상적으로 출석참가 되었습니다.```")
                    elif game == '3' :
                        if time_3rd < time_now and time_now < time_after :
                            await ctx.send(content=f"3경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_3rd} 까지")
                        else :
                            if worksheet_check_B.acell('G' + str(temp)).value == '체크':
                                await ctx.send(content=f"{game}경기 : 이미 출석체크 되었습니다.")
                            else:
                                worksheet_check_B.update_acell('G' + str(temp), '체크')
                                count = worksheet_check_B.acell('I' + str(temp)).value
                                count = int(count) + 1
                                worksheet_check_B.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 B팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"정상적으로 출석참가 되었습니다.```")
                    elif game == '4' :
                        if time_4th < time_now and time_now < time_after :
                            await ctx.send(content=f"4경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_4th} 까지")
                        else :
                            if worksheet_check_B.acell('H' + str(temp)).value == '체크' :
                                await ctx.send(content=f"{game}경기 : 이미 출석체크 되었습니다.")
                            else :
                                worksheet_check_B.update_acell('H' + str(temp), '체크')
                                count = worksheet_check_B.acell('I' + str(temp)).value
                                count = int(count) + 1
                                worksheet_check_B.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 B팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"정상적으로 출석참가 되었습니다.```")
                    else :
                        await ctx.send("```입력이 잘못되었습니다.```")
        else:
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_B 소속이 아닙니다.```")

    elif str(ctx.message.channel) == 'team-c-출석조사':
        if "TEAM_C" in role_names:  # C팀 역할 있는지 체크
            c_max = str(int(worksheet_check_C.acell('A1').value) + 2)
            team_c_list = worksheet_check_C.range('C3:C' + c_max)
            for i, cell in enumerate(team_c_list):  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id):
                    temp = i + 3
                    jupo = worksheet_check_C.acell('D' + str(temp)).value
                    if game == '1':
                        if time_1st < time_now and time_now < time_after:
                            await ctx.send(content=f"1경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_1st} 까지")
                        else:
                            if worksheet_check_C.acell('E' + str(temp)).value == '체크':
                                await ctx.send(content=f"{game}경기 : 이미 출석체크 되었습니다.")
                            else:
                                worksheet_check_C.update_acell('E' + str(temp), '체크')
                                count = worksheet_check_C.acell('I' + str(temp)).value
                                count = int(count) + 1
                                worksheet_check_C.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 C팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"정상적으로 출석참가 되었습니다.```")
                    elif game == '2':
                        if time_2nd < time_now and time_now < time_after:
                            await ctx.send(content=f"2경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_2nd} 까지")
                        else:
                            if worksheet_check_C.acell('F' + str(temp)).value == '체크':
                                await ctx.send("2경기 : 이미 출석체크 되었습니다.")
                            else:
                                worksheet_check_C.update_acell('F' + str(temp), '체크')
                                count = worksheet_check_C.acell('I' + str(temp)).value
                                count = int(count) + 1
                                worksheet_check_C.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 C팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"정상적으로 출석참가 되었습니다.```")
                    elif game == '3':
                        if time_3rd < time_now and time_now < time_after:
                            await ctx.send(content=f"3경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_3rd} 까지")
                        else:
                            if worksheet_check_C.acell('G' + str(temp)).value == '체크':
                                await ctx.send(content=f"{game}경기 : 이미 출석체크 되었습니다.")
                            else:
                                worksheet_check_C.update_acell('G' + str(temp), '체크')
                                count = worksheet_check_C.acell('I' + str(temp)).value
                                count = int(count) + 1
                                worksheet_check_C.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 C팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"정상적으로 출석참가 되었습니다.```")
                    elif game == '4':
                        if time_4th < time_now and time_now < time_after:
                            await ctx.send(content=f"4경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_4th} 까지")
                        else:
                            if worksheet_check_C.acell('H' + str(temp)).value == '체크':
                                await ctx.send(content=f"{game}경기 : 이미 출석체크 되었습니다.")
                            else:
                                worksheet_check_C.update_acell('H' + str(temp), '체크')
                                count = worksheet_check_C.acell('I' + str(temp)).value
                                count = int(count) + 1
                                worksheet_check_C.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 C팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"정상적으로 출석참가 되었습니다.```")
                    else:
                        await ctx.send("```입력이 잘못되었습니다.```")
        else:
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_C 소속이 아닙니다.```")

    elif str(ctx.message.channel) == 'team-d-출석조사':
        if "TEAM_D" in role_names:  # A팀 역할 있는지 체크
            d_max = str(int(worksheet_check_D.acell('A1').value) + 2)
            team_d_list = worksheet_check_D.range('C3:C' + d_max)
            for i, cell in enumerate(team_d_list):  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id):
                    temp = i + 3
                    jupo = worksheet_check_D.acell('D' + str(temp)).value
                    if game == '1' :
                        if time_1st < time_now and time_now < time_after :
                            await ctx.send(content=f"1경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_1st} 까지")
                        else :
                            if worksheet_check_D.acell('E' + str(temp)).value == '체크':
                                await ctx.send(content=f"{game}경기 : 이미 출석체크 되었습니다.")
                            else:
                                worksheet_check_D.update_acell('E' + str(temp), '체크')
                                count = worksheet_check_D.acell('I' + str(temp)).value
                                count = int(count) + 1
                                worksheet_check_D.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 D팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"정상적으로 출석참가 되었습니다.```")
                    elif game == '2' :
                        if time_2nd < time_now and time_now < time_after :
                            await ctx.send(content=f"2경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_2nd} 까지")
                        else :
                            if worksheet_check_D.acell('F' + str(temp)).value == '체크':
                                await ctx.send(content=f"{game}경기 : 이미 출석체크 되었습니다.")
                            else:
                                worksheet_check_D.update_acell('F' + str(temp), '체크')
                                count = worksheet_check_D.acell('I' + str(temp)).value
                                count = int(count) + 1
                                worksheet_check_D.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 D팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"정상적으로 출석참가 되었습니다.```")
                    elif game == '3' :
                        if time_3rd < time_now and time_now < time_after :
                            await ctx.send(content=f"3경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_3rd} 까지")
                        else:
                            if worksheet_check_D.acell('G' + str(temp)).value == '체크' :
                                await ctx.send(content=f"{game}경기 : 이미 출석체크 되었습니다.")
                            else :
                                worksheet_check_D.update_acell('G' + str(temp), '체크')
                                count = worksheet_check_D.acell('I' + str(temp)).value
                                count = int(count) + 1
                                worksheet_check_D.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 D팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"정상적으로 출석참가 되었습니다.```")
                    elif game == '4' :
                        if time_4th < time_now and time_now < time_after :
                            await ctx.send(content=f"4경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_4th} 까지")
                        else:
                            if worksheet_check_D.acell('H' + str(temp)).value == '체크' :
                                await ctx.send(content=f"{game}경기 : 이미 출석체크 되었습니다.")
                            else :
                                worksheet_check_D.update_acell('H' + str(temp), '체크')
                                count = worksheet_check_D.acell('I' + str(temp)).value
                                count = int(count) + 1
                                worksheet_check_D.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 D팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"정상적으로 출석참가 되었습니다.```")
                    else:
                        await ctx.send("```입력이 잘못되었습니다.```")
        else:
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_D 소속이 아닙니다.```")

    elif str(ctx.message.channel) == 'team-e-출석조사':
        if "TEAM_E" in role_names:  # A팀 역할 있는지 체크
            e_max = str(int(worksheet_check_E.acell('A1').value) + 2)
            team_e_list = worksheet_check_E.range('C3:C' + e_max)
            for i, cell in enumerate(team_e_list):  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id):
                    temp = i + 3
                    jupo = worksheet_check_E.acell('D' + str(temp)).value
                    if game == '1' :
                        if time_1st < time_now and time_now < time_after :
                            await ctx.send(content=f"1경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_1st} 까지")
                        else :
                            worksheet_check_E.update_acell('E' + str(temp), '체크')
                            await ctx.send(content=f"```{now_month}월 {now_day}일 E팀 {game}경기\n"
                                                   f"닉네임 : {ctx.author.display_name}\n"
                                                   f"정상적으로 출석참가 되었습니다.```")
                    elif game == '2' :
                        if time_2nd < time_now and time_now < time_after :
                            await ctx.send(content=f"2경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_2nd} 까지")
                        else :
                            worksheet_check_E.update_acell('F' + str(temp), '체크')
                            await ctx.send(content=f"```{now_month}월 {now_day}일 E팀 {game}경기\n"
                                                   f"닉네임 : {ctx.author.display_name}\n"
                                                   f"정상적으로 출석참가 되었습니다.```")
                    elif game == '3' :
                        if time_3rd < time_now and time_now < time_after :
                            await ctx.send(content=f"3경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_3rd} 까지")
                        else :
                            worksheet_check_E.update_acell('G' + str(temp), '체크')
                            await ctx.send(content=f"```{now_month}월 {now_day}일 E팀 {game}경기\n"
                                                   f"닉네임 : {ctx.author.display_name}\n"
                                                   f"정상적으로 출석참가 되었습니다.```")
                    elif game == '4' :
                        if time_4th < time_now and time_now < time_after :
                            await ctx.send(content=f"4경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_4th} 까지")
                        else :
                            worksheet_check_E.update_acell('H' + str(temp), '체크')
                            await ctx.send(content=f"```{now_month}월 {now_day}일 E팀 {game}경기\n"
                                                   f"닉네임 : {ctx.author.display_name}\n"
                                                   f"정상적으로 출석참가 되었습니다.```")
                    else:
                        await ctx.send("```입력이 잘못되었습니다.```")
                        
        else:
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_E 소속이 아닙니다.```")

    else:
        await ctx.send("각 팀 출석조사 채널에 입력해주세요.")



@bot.command(aliases=['cancelcheck', '출취'])
async def 출석취소(ctx, game):
    time_now = datetime.datetime.now()
    time_1st = datetime.datetime(time_now.year, time_now.month, time_now.day, 20, 30, 00)
    time_2nd = datetime.datetime(time_now.year, time_now.month, time_now.day, 21, 00, 00)
    time_3rd = datetime.datetime(time_now.year, time_now.month, time_now.day, 21, 30, 00)
    time_4th = datetime.datetime(time_now.year, time_now.month, time_now.day, 22, 00, 00)
    time_after = datetime.datetime(time_now.year, time_now.month, time_now.day, 23, 00, 00)
    now_month = time_now.strftime('%m')
    now_day = time_now.strftime('%d')
    role_names = [role.name for role in ctx.author.roles]

    # 범위(체크)
    cell_max = worksheet_list.acell('A1').value
    a_max = str(int(worksheet_check_A.acell('A1').value) + 2)
    b_max = str(int(worksheet_check_B.acell('A1').value) + 2)
    c_max = str(int(worksheet_check_C.acell('A1').value) + 2)
    d_max = str(int(worksheet_check_D.acell('A1').value) + 2)
    e_max = str(int(worksheet_check_E.acell('A1').value) + 2)
    # 범위 내 셀 값 로딩
    team_a_list = worksheet_check_A.range('C3:C' + a_max)
    team_b_list = worksheet_check_B.range('C3:C' + b_max)
    team_c_list = worksheet_check_C.range('C3:C' + c_max)
    team_d_list = worksheet_check_D.range('C3:C' + d_max)
    team_e_list = worksheet_check_E.range('C3:C' + e_max)
    name = ctx.author.display_name.split('[')

    ctx.message.delete()

    if str(ctx.message.channel) == 'team-a-출석조사':
        if "TEAM_A" in role_names:  # A팀 역할 있는지 체크
            for i, cell in enumerate(team_a_list):  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id):
                    temp = i + 3
                    if game == '1' :
                        if time_1st < time_now and time_now < time_after :
                            await ctx.send(content=f"1경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_1st} 까지")
                        else :
                            if worksheet_check_A.acell('E' + str(temp)).value == '0':
                                await ctx.send(content=f"{game}경기 : 출석체크를 하지 않았습니다.")
                            else :
                                worksheet_check_A.update_acell('E' + str(temp), '0')
                                count = worksheet_check_A.acell('I' + str(temp)).value
                                count = int(count) - 1
                                worksheet_check_A.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 A팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"출석취소 되었습니다.```")
                    elif game == '2' :
                        if time_2nd < time_now and time_now < time_after :
                            await ctx.send(content=f"2경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_2nd} 까지")
                        else :
                            if worksheet_check_A.acell('F' + str(temp)).value == '0' :
                                await ctx.send(content=f"{game}경기 : 출석체크를 하지 않았습니다.")
                            else :
                                worksheet_check_A.update_acell('F' + str(temp), '0')
                                count = worksheet_check_A.acell('I' + str(temp)).value
                                count = int(count) - 1
                                worksheet_check_A.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 A팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"출석취소 되었습니다.```")
                    elif game == '3' :
                        if time_3rd < time_now and time_now < time_after :
                            await ctx.send(content=f"3경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_3rd} 까지")
                        else :
                            if worksheet_check_A.acell('G' + str(temp)).value == '0' :
                                await ctx.send(content=f"{game}경기 : 출석체크를 하지 않았습니다.")
                            else :
                                worksheet_check_A.update_acell('G' + str(temp), '0')
                                count = worksheet_check_A.acell('I' + str(temp)).value
                                count = int(count) - 1
                                worksheet_check_A.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 A팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"출석취소 되었습니다.```")
                    elif game == '4' :
                        if time_4th < time_now and time_now < time_after :
                            await ctx.send(content=f"4경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_4th} 까지")
                        else :
                            if worksheet_check_A.acell('H' + str(temp)).value == '0' :
                                await ctx.send(content=f"{game}경기 : 출석체크를 하지 않았습니다.")
                            else :
                                worksheet_check_A.update_acell('H' + str(temp), '0')
                                count = worksheet_check_A.acell('I' + str(temp)).value
                                count = int(count) - 1
                                worksheet_check_A.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 A팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"출석취소 되었습니다.```")
                        await ctx.send("```입력이 잘못되었습니다.```")
        else:
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_A 소속이 아닙니다.```")

    elif str(ctx.message.channel) == 'team-b-출석조사':
        if "TEAM_B" in role_names:  # A팀 역할 있는지 체크
            for i, cell in enumerate(team_b_list):  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id):
                    temp = i + 3
                    if game == '1' :
                        if time_1st < time_now and time_now < time_after :
                            await ctx.send(content=f"1경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_1st} 까지")
                        else :
                            if worksheet_check_B.acell('E' + str(temp)).value == '0' :
                                await ctx.send(content=f"{game}경기 : 출석체크를 하지 않았습니다.")
                            else :
                                worksheet_check_B.update_acell('E' + str(temp), '0')
                                count = worksheet_check_B.acell('I' + str(temp)).value
                                count = int(count) - 1
                                worksheet_check_B.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 B팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"출석취소 되었습니다.```")
                    elif game == '2' :
                        if time_2nd < time_now and time_now < time_after :
                            await ctx.send(content=f"2경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_2nd} 까지")
                        else :
                            if worksheet_check_B.acell('F' + str(temp)).value == '0' :
                                await ctx.send(content=f"{game}경기 : 출석체크를 하지 않았습니다.")
                            else :
                                worksheet_check_B.update_acell('F' + str(temp), '0')
                                count = worksheet_check_B.acell('I' + str(temp)).value
                                count = int(count) - 1
                                worksheet_check_B.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 B팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"출석취소 되었습니다.```")
                    elif game == '3' :
                        if time_3rd < time_now and time_now < time_after :
                            await ctx.send(content=f"3경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_3rd} 까지")
                        else :
                            if worksheet_check_B.acell('G' + str(temp)).value == '0' :
                                await ctx.send(content=f"{game}경기 : 출석체크를 하지 않았습니다.")
                            else :
                                worksheet_check_B.update_acell('G' + str(temp), '0')
                                count = worksheet_check_B.acell('I' + str(temp)).value
                                count = int(count) - 1
                                worksheet_check_B.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 B팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"출석취소 되었습니다.```")
                    elif game == '4' :
                        if time_4th < time_now and time_now < time_after :
                            await ctx.send(content=f"4경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_4th} 까지")
                        else :
                            if worksheet_check_B.acell('H' + str(temp)).value == '0' :
                                await ctx.send(content=f"{game}경기 : 출석체크를 하지 않았습니다.")
                            else :
                                worksheet_check_B.update_acell('H' + str(temp), '0')
                                count = worksheet_check_B.acell('I' + str(temp)).value
                                count = int(count) - 1
                                worksheet_check_B.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 B팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"출석취소 되었습니다.```")
                    else:
                        await ctx.send("```입력이 잘못되었습니다.```")
        else:
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_B 소속이 아닙니다.```")

    elif str(ctx.message.channel) == 'team-c-출석조사':
        if "TEAM_C" in role_names:  # A팀 역할 있는지 체크
            for i, cell in enumerate(team_c_list):  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id):
                    temp = i + 3
                    if game == '1' :
                        if time_1st < time_now and time_now < time_after :
                            await ctx.send(content=f"1경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_1st} 까지")
                        else :
                            if worksheet_check_C.acell('E' + str(temp)).value == '0' :
                                await ctx.send(content=f"{game}경기 : 출석체크를 하지 않았습니다.")
                            else :
                                worksheet_check_C.update_acell('E' + str(temp), '0')
                                count = worksheet_check_C.acell('I' + str(temp)).value
                                count = int(count) - 1
                                worksheet_check_C.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 C팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"출석취소 되었습니다.```")
                        if time_2nd < time_now and time_now < time_after :
                            await ctx.send(content=f"2경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_2nd} 까지")
                        else :
                            if worksheet_check_C.acell('F' + str(temp)).value == '0' :
                                await ctx.send(content=f"{game}경기 : 출석체크를 하지 않았습니다.")
                            else :
                                worksheet_check_C.update_acell('F' + str(temp), '0')
                                count = worksheet_check_C.acell('I' + str(temp)).value
                                count = int(count) - 1
                                worksheet_check_C.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 C팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"출석취소 되었습니다.```")
                    elif game == '3' :
                        if time_3rd < time_now and time_now < time_after :
                            await ctx.send(content=f"3경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_3rd} 까지")
                        else :
                            if worksheet_check_C.acell('G' + str(temp)).value == '0' :
                                await ctx.send(content=f"{game}경기 : 출석체크를 하지 않았습니다.")
                            else :
                                worksheet_check_C.update_acell('G' + str(temp), '0')
                                count = worksheet_check_C.acell('I' + str(temp)).value
                                count = int(count) - 1
                                worksheet_check_C.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 C팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"출석취소 되었습니다.```")
                        if time_4th < time_now and time_now < time_after :
                            await ctx.send(content=f"4경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_4th} 까지")
                        elif game == '4':
                            if time_4th < time_now and time_now < time_after :
                                await ctx.send(content=f"4경기 출석 가능한 시간이 아닙니다.\n"
                                                       f"출석 가능 시간 - {time_4th} 까지")
                            else :
                                if worksheet_check_C.acell('H' + str(temp)).value == '0' :
                                    await ctx.send(content=f"{game}경기 : 출석체크를 하지 않았습니다.")
                                else :
                                    worksheet_check_C.update_acell('H' + str(temp), '0')
                                    count = worksheet_check_C.acell('I' + str(temp)).value
                                    count = int(count) - 1
                                    worksheet_check_C.update_acell('I' + str(temp), str(count))
                                    await ctx.send(content=f"```{now_month}월 {now_day}일 B팀 {game}경기\n"
                                                           f"닉네임 : {ctx.author.display_name}\n"
                                                           f"출석취소 되었습니다.```")
                    else:
                        await ctx.send("```입력이 잘못되었습니다.```")
        else:
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_C 소속이 아닙니다.```")

    elif str(ctx.message.channel) == 'team-d-출석조사':
        if "TEAM_D" in role_names:  # A팀 역할 있는지 체크
            for i, cell in enumerate(team_d_list):  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id):
                    temp = i + 3
                    if game == '1' :
                        if time_1st < time_now and time_now < time_after :
                            await ctx.send(content=f"1경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_1st} 까지")
                        else :
                            if worksheet_check_D.acell('E' + str(temp)).value == '0' :
                                await ctx.send(content=f"{game}경기 : 출석체크를 하지 않았습니다.")
                            else :
                                worksheet_check_D.update_acell('E' + str(temp), '0')
                                count = worksheet_check_D.acell('I' + str(temp)).value
                                count = int(count) - 1
                                worksheet_check_D.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 D팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"출석취소 되었습니다.```")
                    elif game == '2' :
                        if time_2nd < time_now and time_now < time_after :
                            await ctx.send(content=f"2경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_2nd} 까지")
                        else :
                            if worksheet_check_D.acell('F' + str(temp)).value == '0' :
                                await ctx.send(content=f"{game}경기 : 출석체크를 하지 않았습니다.")
                            else :
                                worksheet_check_D.update_acell('F' + str(temp), '0')
                                count = worksheet_check_D.acell('I' + str(temp)).value
                                count = int(count) - 1
                                worksheet_check_D.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 D팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"출석취소 되었습니다.```")
                    elif game == '3' :
                        if time_3rd < time_now and time_now < time_after :
                            await ctx.send(content=f"3경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_3rd} 까지")
                        else :
                            if worksheet_check_D.acell('G' + str(temp)).value == '0' :
                                await ctx.send(content=f"{game}경기 : 출석체크를 하지 않았습니다.")
                            else :
                                worksheet_check_D.update_acell('G' + str(temp), '0')
                                count = worksheet_check_D.acell('I' + str(temp)).value
                                count = int(count) - 1
                                worksheet_check_D.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 D팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"출석취소 되었습니다.```")
                    elif game == '4' :
                        if time_4th < time_now and time_now < time_after :
                            await ctx.send(content=f"4경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_4th} 까지")
                        else :
                            if worksheet_check_D.acell('H' + str(temp)).value == '0' :
                                await ctx.send(content=f"{game}경기 : 출석체크를 하지 않았습니다.")
                            else :
                                worksheet_check_D.update_acell('H' + str(temp), '0')
                                count = worksheet_check_D.acell('I' + str(temp)).value
                                count = int(count) - 1
                                worksheet_check_D.update_acell('I' + str(temp), str(count))
                                await ctx.send(content=f"```{now_month}월 {now_day}일 D팀 {game}경기\n"
                                                       f"닉네임 : {ctx.author.display_name}\n"
                                                       f"출석취소 되었습니다.```")
                    else:
                        await ctx.send("```입력이 잘못되었습니다.```")
        else:
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_D 소속이 아닙니다.```")

    elif str(ctx.message.channel) == 'team-e-출석조사':
        if "TEAM_E" in role_names :  # A팀 역할 있는지 체크
            for i, cell in enumerate(team_e_list) :  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id) :
                    temp = i + 3
                    if game == '1':
                        if time_1st < time_now and time_now < time_after :
                            await ctx.send(content=f"1경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_1st} 까지")
                        else :
                            worksheet_check_E.update_acell('E' + str(temp), '체크')
                            await ctx.send(content=f"```{now_month}월 {now_day}일 E팀 {game}경기\n"
                                                   f"닉네임 : {ctx.author.display_name}\n"
                                                   f"출석취소 되었습니다.```")
                    elif game == '2':
                        if time_2nd < time_now and time_now < time_after :
                            await ctx.send(content=f"2경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_2nd} 까지")
                        else :
                            worksheet_check_E.update_acell('F' + str(temp), '체크')
                            await ctx.send(content=f"```{now_month}월 {now_day}일 E팀 {game}경기\n"
                                                   f"닉네임 : {ctx.author.display_name}\n"
                                                   f"출석취소 되었습니다.```")
                    elif game == '3':
                        if time_3rd < time_now and time_now < time_after :
                            await ctx.send(content=f"3경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_3rd} 까지")
                        else :
                            worksheet_check_E.update_acell('G' + str(temp), '체크')
                            await ctx.send(content=f"```{now_month}월 {now_day}일 E팀 {game}경기\n"
                                                   f"닉네임 : {ctx.author.display_name}\n"
                                                   f"출석취소 되었습니다.```")
                    elif game == '4':
                        if time_4th < time_now and time_now < time_after :
                            await ctx.send(content=f"4경기 출석 가능한 시간이 아닙니다.\n"
                                                   f"출석 가능 시간 - {time_4th} 까지")
                        else:
                            worksheet_check_E.update_acell('H' + str(temp), '체크')
                            await ctx.send(content=f"```{now_month}월 {now_day}일 E팀 {game}경기\n"
                                                   f"닉네임 : {ctx.author.display_name}\n"
                                                   f"출석취소 되었습니다.```")
                    else :
                        await ctx.send("```입력이 잘못되었습니다.```")
        else :
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_E 소속이 아닙니다.```")
    else :
        await ctx.send("각 팀 출석조사 채널에 입력해주세요.")



@bot.command(aliases=['출결'])
async def 출석결과(ctx, teamname):
    await ctx.message.delete()
    teamli1 = []
    teamli2 = []
    teamli3 = []
    teamli4 = []
    teamliwhole = []
    switch = True
    print(fun.teamNameConvert(teamname))
    if fun.teamNameConvert(teamname) == 'TEAM_A':
        # 범위(체크)
        a_max = str(int(worksheet_check_A.acell('A1').value) + 2)
        # 범위 내 셀 값 로딩
        color = 0xdf8b00
        team_nick = worksheet_check_A.range('B3:B' + a_max)
        team_pos = worksheet_check_A.range('D3:D' + a_max)
        team_match1 = worksheet_check_A.range('E3:E' + a_max)
        team_match2 = worksheet_check_A.range('F3:F' + a_max)
        team_match3 = worksheet_check_A.range('G3:G' + a_max)
        team_match4 = worksheet_check_A.range('H3:H' + a_max)
    elif fun.teamNameConvert(teamname) == 'TEAM_B':
        color = 0x8634c4
        b_max = str(int(worksheet_check_B.acell('A1').value) + 2)
        team_nick = worksheet_check_B.range('B3:B' + b_max)
        team_pos = worksheet_check_B.range('D3:D' + b_max)
        team_match1 = worksheet_check_B.range('E3:E' + b_max)
        team_match2 = worksheet_check_B.range('F3:F' + b_max)
        team_match3 = worksheet_check_B.range('G3:G' + b_max)
        team_match4 = worksheet_check_B.range('H3:H' + b_max)
    elif fun.teamNameConvert(teamname) == 'TEAM_C':
        color = 0xfff400
        c_max = str(int(worksheet_check_C.acell('A1').value) + 2)
        team_nick = worksheet_check_C.range('B3:B' + c_max)
        team_pos = worksheet_check_C.range('D3:D' + c_max)
        team_match1 = worksheet_check_C.range('E3:E' + c_max)
        team_match2 = worksheet_check_C.range('F3:F' + c_max)
        team_match3 = worksheet_check_C.range('G3:G' + c_max)
        team_match4 = worksheet_check_C.range('H3:H' + c_max)
    elif fun.teamNameConvert(teamname) == 'TEAM_D':
        color = 0xff67ff
        d_max = str(int(worksheet_check_D.acell('A1').value) + 2)
        team_nick = worksheet_check_D.range('B3:B' + d_max)
        team_pos = worksheet_check_D.range('D3:D' + d_max)
        team_match1 = worksheet_check_D.range('E3:E' + d_max)
        team_match2 = worksheet_check_D.range('F3:F' + d_max)
        team_match3 = worksheet_check_D.range('G3:G' + d_max)
        team_match4 = worksheet_check_D.range('H3:H' + d_max)
    elif fun.teamNameConvert(teamname) == 'TEAM_E':
        color = 0x76fd61
        e_max = str(int(worksheet_check_E.acell('A1').value) + 2)
        team_nick = worksheet_check_E.range('B3:B' + e_max)
        team_pos = worksheet_check_E.range('D3:D' + e_max)
        team_match1 = worksheet_check_E.range('E3:E' + e_max)
        team_match2 = worksheet_check_E.range('F3:F' + e_max)
        team_match3 = worksheet_check_E.range('G3:G' + e_max)
        team_match4 = worksheet_check_E.range('H3:H' + e_max)
    elif fun.teamNameConvert(teamname) == 'error':
        switch = False

    if switch:
        for i in range(len(team_nick)):
            teamli1.append([team_pos[i].value, fun.convertNickname(team_nick[i].value), team_match1[i].value])
            teamli2.append([team_pos[i].value, fun.convertNickname(team_nick[i].value), team_match2[i].value])
            teamli3.append([team_pos[i].value, fun.convertNickname(team_nick[i].value), team_match3[i].value])
            teamli4.append([team_pos[i].value, fun.convertNickname(team_nick[i].value), team_match4[i].value])
            teamliwhole.append([team_pos[i].value, fun.convertNickname(team_nick[i].value)])
        embed = discord.Embed(title=f"{fun.teamNameConvert(teamname)} 정보", description="이적 자금 : <미추가>", color=color)
        embed.add_field(name=f"1경기 출석결과({fun.countCheck(teamli1)} 명)",
                        value=f"ST:{fun.convertCheck(teamli1, 'st')}\n"
                              f"LW:{fun.convertCheck(teamli1, 'lw')}\n"
                              f"RW:{fun.convertCheck(teamli1, 'rw')}\n"
                              f"CAM:{fun.convertCheck(teamli1, 'cam')}\n"
                              f"CM:{fun.convertCheck(teamli1, 'cm')}\n"
                              f"CDM:{fun.convertCheck(teamli1, 'cdm')}\n"
                              f"LB:{fun.convertCheck(teamli1, 'lb')}\n"
                              f"CB:{fun.convertCheck(teamli1, 'cb')}\n"
                              f"RB:{fun.convertCheck(teamli1, 'rb')}\n"
                              f"GK:{fun.convertCheck(teamli1, 'gk')}\n", inline=True)
        embed.add_field(name=f"2경기 출석결과({fun.countCheck(teamli2)} 명)",
                        value=f"ST:{fun.convertCheck(teamli1, 'st')}\n"
                              f"LW:{fun.convertCheck(teamli2, 'lw')}\n"
                              f"RW:{fun.convertCheck(teamli2, 'rw')}\n"
                              f"CAM:{fun.convertCheck(teamli2, 'cam')}\n"
                              f"CM:{fun.convertCheck(teamli2, 'cm')}\n"
                              f"CDM:{fun.convertCheck(teamli2, 'cdm')}\n"
                              f"LB:{fun.convertCheck(teamli2, 'lb')}\n"
                              f"CB:{fun.convertCheck(teamli2, 'cb')}\n"
                              f"RB:{fun.convertCheck(teamli2, 'rb')}\n"
                              f"GK:{fun.convertCheck(teamli2, 'gk')}\n", inline=True)
        embed.add_field(name=f"3경기 출석결과({fun.countCheck(teamli3)} 명)",
                        value=f"ST:{fun.convertCheck(teamli3, 'st')}\n"
                              f"LW:{fun.convertCheck(teamli3, 'lw')}\n"
                              f"RW:{fun.convertCheck(teamli3, 'rw')}\n"
                              f"CAM:{fun.convertCheck(teamli3, 'cam')}\n"
                              f"CM:{fun.convertCheck(teamli3, 'cm')}\n"
                              f"CDM:{fun.convertCheck(teamli3, 'cdm')}\n"
                              f"LB:{fun.convertCheck(teamli3, 'lb')}\n"
                              f"CB:{fun.convertCheck(teamli3, 'cb')}\n"
                              f"RB:{fun.convertCheck(teamli3, 'rb')}\n"
                              f"GK:{fun.convertCheck(teamli3, 'gk')}\n", inline=True)
        embed.add_field(name=f"4경기 출석결과({fun.countCheck(teamli4)} 명)",
                        value=f"ST:{fun.convertCheck(teamli4, 'st')}\n"
                              f"LW:{fun.convertCheck(teamli4, 'lw')}\n"
                              f"RW:{fun.convertCheck(teamli4, 'rw')}\n"
                              f"CAM:{fun.convertCheck(teamli4, 'cam')}\n"
                              f"CM:{fun.convertCheck(teamli4, 'cm')}\n"
                              f"CDM:{fun.convertCheck(teamli4, 'cdm')}\n"
                              f"LB:{fun.convertCheck(teamli4, 'lb')}\n"
                              f"CB:{fun.convertCheck(teamli4, 'cb')}\n"
                              f"RB:{fun.convertCheck(teamli4, 'rb')}\n"
                              f"GK:{fun.convertCheck(teamli4, 'gk')}\n", inline=True)
        embed.set_footer(text="Copyright ⓒ 2020-2021 타임제이(TimeJ) in C.E.F All Right Reserved.")
        await ctx.send(embed=embed)
    else:
        await ctx.send("```팀명을 다시 입력해주세요.\n"
                       "팀명은 A, B, C, D, E 까지 입력 가능하며\n"
                       "대소문자, TEAM_A 식으로 3가지 방법으로 팀명을 입력 가능합니다.```")


@bot.command(aliases=['출초'])
async def 출석초기화(ctx):
    role_names = [role.name for role in ctx.author.roles]
    A_check_channel = get(ctx.guild.channels, name='team-a-출석조사')
    B_check_channel = get(ctx.guild.channels, name='team-b-출석조사')
    C_check_channel = get(ctx.guild.channels, name='team-c-출석조사')
    D_check_channel = get(ctx.guild.channels, name='team-d-출석조사')
    E_check_channel = get(ctx.guild.channels, name='🔈team-e-출석조사')
    if '스태프' in role_names:
        # 범위(체크)
        a_max = str(int(worksheet_check_A.acell('A1').value) + 2)
        b_max = str(int(worksheet_check_B.acell('A1').value) + 2)
        c_max = str(int(worksheet_check_C.acell('A1').value) + 2)
        d_max = str(int(worksheet_check_D.acell('A1').value) + 2)
        e_max = str(int(worksheet_check_E.acell('A1').value) + 2)
        # 범위 내 셀 값 로딩
        team_a_reset_list = worksheet_check_A.range('E3:H' + a_max)
        team_b_reset_list = worksheet_check_B.range('E3:H' + b_max)
        team_c_reset_list = worksheet_check_C.range('E3:H' + c_max)
        team_d_reset_list = worksheet_check_D.range('E3:H' + d_max)
        team_e_reset_list = worksheet_check_E.range('E3:H' + d_max)

        for cell in team_a_reset_list:
            cell.value = '0'
        for cell in team_b_reset_list:
            cell.value = '0'
        for cell in team_c_reset_list:
            cell.value = '0'
        for cell in team_d_reset_list:
            cell.value = '0'
        for cell in team_e_reset_list:
            cell.value = '0'
        worksheet_check_A.update_cells(team_a_reset_list)
        worksheet_check_B.update_cells(team_b_reset_list)
        worksheet_check_C.update_cells(team_c_reset_list)
        worksheet_check_D.update_cells(team_d_reset_list)
        worksheet_check_E.update_cells(team_e_reset_list)
        await A_check_channel.send("```출석체크 시트가 모두 초기화 되었습니다.```")
        await B_check_channel.send("```출석체크 시트가 모두 초기화 되었습니다.```")
        await C_check_channel.send("```출석체크 시트가 모두 초기화 되었습니다.```")
        await D_check_channel.send("```출석체크 시트가 모두 초기화 되었습니다.```")
        await E_check_channel.send("```출석체크 시트가 모두 초기화 되었습니다.```")
    else:
        await ctx.send("```해당 명령어는 스태프만 사용 가능합니다.```")

@bot.command(aliases=['출공'])
async def 출석공지(ctx):
    role_names = [role.name for role in ctx.author.roles]
    A_role = get(ctx.guild.roles, name='TEAM_A')
    B_role = get(ctx.guild.roles, name='TEAM_B')
    C_role = get(ctx.guild.roles, name='TEAM_C')
    D_role = get(ctx.guild.roles, name='TEAM_D')
    E_role = get(ctx.guild.roles, name='TEAM_E')
    A_check_channel = get(ctx.guild.channels, name='team-a-출석조사')
    B_check_channel = get(ctx.guild.channels, name='team-b-출석조사')
    C_check_channel = get(ctx.guild.channels, name='team-c-출석조사')
    D_check_channel = get(ctx.guild.channels, name='team-d-출석조사')
    E_check_channel = get(ctx.guild.channels, name='team-e-출석조사')
    if '스태프' in role_names:
        await A_check_channel.send(content=f"{A_role.mention}\n"
                                           f"```cs\n"        
                                           f"출석체크 및 확인 바랍니다.\n"
                                           f"1경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:00\n"
                                           f"2경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:40\n"
                                           f"3경기 출석 가능 시간 : 전날 23:00 ~ 당일 22:20\n```")
        await B_check_channel.send(content=f"{B_role.mention}\n"
                                           f"```cs\n"        
                                           f"출석체크 및 확인 바랍니다.\n"
                                           f"1경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:00\n"
                                           f"2경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:30\n"
                                           f"3경기 출석 가능 시간 : 전날 23:00 ~ 당일 22:00\n```")
        await C_check_channel.send(content=f"{C_role.mention}\n"
                                           f"```cs\n"        
                                           f"출석체크 및 확인 바랍니다.\n"
                                           f"1경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:00\n"
                                           f"2경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:30\n"
                                           f"3경기 출석 가능 시간 : 전날 23:00 ~ 당일 22:00\n```")
        await D_check_channel.send(content=f"{D_role.mention}\n"
                                           f"```cs\n"        
                                           f"출석체크 및 확인 바랍니다.\n"
                                           f"1경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:00\n"
                                           f"2경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:30\n"
                                           f"3경기 출석 가능 시간 : 전날 23:00 ~ 당일 22:00\n```")
        await E_check_channel.send(content=f"{E_role.mention}\n"
                                           f"```cs\n"        
                                           f"출석체크 및 확인 바랍니다.\n"
                                           f"1경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:00\n"
                                           f"2경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:30\n"
                                           f"3경기 출석 가능 시간 : 전날 23:00 ~ 당일 22:00\n```")
    else:
        await ctx.send("```해당 명령어는 스태프만 사용 가능합니다.```")


@bot.command(aliases=['종공'])
async def 종료공지(ctx):
    emojis = ""
    a_team_chat_id = get(ctx.guild.channels, name='ʀᴀɴ-팀채팅')
    b_team_chat_id = get(ctx.guild.channels, name='ᴊᴜᴠ-팀채팅')
    c_team_chat_id = get(ctx.guild.channels, name='sᴄʜ_팀채팅')
    d_team_chat_id = get(ctx.guild.channels, name='ᴀᴛᴍ-팀채팅')
    e_team_chat_id = get(ctx.guild.channels, name='ɪᴜꜰᴄ-팀채팅')
    f_team_chat_id = get(ctx.guild.channels, name='ꜰᴄʙ-팀채팅')
    g_team_chat_id = get(ctx.guild.channels, name='𝗠𝟬𝟱-팀채팅')
    emoji = "<:__:708304488217313371>"
    for i in range(0, 10):
        emojis = emojis + emoji
    msg = "```리그팀 플레이 종료 시간입니다.```"
    url = "https://tenor.com/view/traffic-fbi-open-up-raid-gif-13450966"
    await a_team_chat_id.send(content=f"{emojis}\n")
    await a_team_chat_id.send(content=f"{msg}\n"
                                      f"{url}")

    await b_team_chat_id.send(content=f"{emojis}\n")
    await b_team_chat_id.send(content=f"{msg}\n"
                                      f"{url}")

    await c_team_chat_id.send(content=f"{emojis}\n")
    await c_team_chat_id.send(content=f"{msg}\n"
                                      f"{url}")

    await d_team_chat_id.send(content=f"{emojis}\n")
    await d_team_chat_id.send(content=f"{msg}\n"
                                      f"{url}")

    await e_team_chat_id.send(content=f"{emojis}\n")
    await e_team_chat_id.send(content=f"{msg}\n"
                                      f"{url}")

    await f_team_chat_id.send(content=f"{emojis}\n")
    await f_team_chat_id.send(content=f"{msg}\n"
                                      f"{url}")

    await g_team_chat_id.send(content=f"{emojis}\n")
    await g_team_chat_id.send(content=f"{msg}\n"
                                      f"{url}")

@bot.command()
async def 반복멘션(ctx, member:discord.Member):
    role_names = [role.name for role in ctx.author.roles]
    if "스태프" in role_names or "머장" in role_names:
        for i in range(10):
            await ctx.send(content=f"{member.mention}")
    else:
        await ctx.send(content=f"스태프만 사용가능합니다.")


@bot.command()
async def 구매완료(ctx):
    await ctx.reply("해당 명령어는 비활성화되었습니다.")
    '''role_names = [role.name for role in ctx.author.roles]

    if '피파23 구매자' not in role_names:
        user = ctx.author
        if '구매 예정' not in role_names :
            Role23 = get(ctx.guild.roles, name='피파23 구매자')
            await user.add_roles(Role23)
            await ctx.reply("피파23 구매자 역할 부여 완료")
        else:
            try:
                await ctx.reply("'구매 에정' 역할을 보유하고 있습니다.\n"
                                "구매를 하였으면 1, 아닐 시 2를 입력주세요.")
                msg = await bot.wait_for("message", check=lambda m : m.author == ctx.author and m.channel == ctx.channel,
                                         timeout=5.0)
            except asyncio.TimeoutError:
                await ctx.channel.send("시간 초과")
            else :
                if msg.content.lower() == '1':
                    delete_role = get(ctx.guild.roles, name='구매 예정')
                    await user.remove_roles(delete_role)
                    Role23 = get(ctx.guild.roles, name='피파23 구매자')
                    await user.add_roles(Role23)
                    await ctx.reply("기존 '구매 예정' 역할을 삭제하였습니다.\n"
                                    "'피파23 구매자' 역할 부여가 완료되었습니다.")

                elif msg.content.lower() == '2':
                    await ctx.reply("구매 이후에 다시 시도해주세요.")
    else:
        await ctx.reply("이미 '피파23 구매자' 역할을 갖고 있습니다.")'''


@bot.command()
async def 구매예정(ctx):
    await ctx.reply("해당 명령어는 비활성화되었습니다.")
    '''role_names = [role.name for role in ctx.author.roles]

    if '구매 예정' not in role_names:
        user = ctx.author
        if '피파23 구매자' in role_names:
            await ctx.reply("이미 '피파23 구매자' 역할을 갖고 있습니다.")
        else:
            Role23 = get(ctx.guild.roles, name='구매 예정')
            await user.add_roles(Role23)
            await ctx.reply("구매 예정자 역할 부여 완료")
    else:
        await ctx.reply("이미 '구매 예정' 역할을 갖고 있습니다.")'''


@bot.command()
async def 리그초기화(ctx):
    # --------------------------------------
    # 리그 역할 초기화
    roleli = []
    #role_names = ["MCI", "SOS", "FCB", "ROM", "MCI Coach", "SOS Coach", "FCB Coach", "ROM Coach", "감독"]
    role_names = ["MIL", "TOT", "BRZ"]
    for rolename in role_names:
        roleli.append(get(ctx.guild.roles, name=rolename))
    for role in roleli:
        for member in role.members:
            await member.remove_roles(role)
            await ctx.send(content=f"{member.mention} - {role} 제거")      # 메시지 닉네임 출력
            #await ctx.send(content=f"{member.mention} - {role} 제거")            메시지 멘션 출력
    # --------------------------------------
    # 출석 체크 시트 초기화
    worksheet_check_A.delete_rows(3, 30)
    worksheet_check_B.delete_rows(3, 30)
    worksheet_check_C.delete_rows(3, 30)
    worksheet_check_D.delete_rows(3, 30)
    worksheet_check_E.delete_rows(3, 30)
    # --------------------------------------
    # 명단 시트 - 소속 변경
    max = worksheet_list.acell('A1').value
    crange = 'H2:H' + max
    cell_list = worksheet_list.range(crange)
    for cell in cell_list:
        cell.value = '무소속'
    worksheet_list.update_cells(cell_list)
    '''# --------------------------------------
    # 채널 초기화
    # A팀 카테고리
    categoryA = get(ctx.guild.categories, name='⚽  TEAM A')
    #  - 팀채팅
    teamA_team_chat = get(ctx.guild.channels, name='team-a-팀채팅')
    teamA_team_chat_temp = teamA_team_chat.overwrites
    temp = await ctx.guild.create_text_channel(name='team-a-팀채팅', category=categoryA)
    await temp.edit(overwrites=teamA_team_chat_temp)
    await teamA_team_chat.delete()
    #  - 전술노트
    teamA_team_tatic = get(ctx.guild.channels, name='team-a-전술노트')
    teamA_team_tatic_temp = teamA_team_tatic.overwrites
    temp = await ctx.guild.create_text_channel(name='team-a-전술노트', category=categoryA)
    await temp.edit(overwrites=teamA_team_tatic_temp)
    await teamA_team_tatic.delete()
    #  - 선발명단
    teamA_team_lineup = get(ctx.guild.channels, name='team-a-선발명단')
    teamA_team_lineup_temp = teamA_team_chat.overwrites
    temp = await ctx.guild.create_text_channel(name='team-a-선발명단', category=categoryA)
    await temp.edit(overwrites=teamA_team_lineup_temp)
    await teamA_team_lineup.delete()
    #  - 출석조사
    teamA_team_check = get(ctx.guild.channels, name='team-a-출석조사')
    teamA_team_check_temp = teamA_team_chat.overwrites
    temp = await ctx.guild.create_text_channel(name='team-a-출석조사', category=categoryA)
    await temp.edit(overwrites=teamA_team_check_temp)
    await teamA_team_check.delete()
    #  - 불참-인원관리
    teamA_team_out = get(ctx.guild.channels, name='불참-인원-관리')
    teamA_team_out_temp = teamA_team_chat.overwrites
    temp = await ctx.guild.create_text_channel(name='불참-인원-관리', category=categoryA)
    await temp.edit(overwrites=teamA_team_out_temp)
    await teamA_team_out.delete()
    #  - 주장-토크
    teamA_team_coach = get(ctx.guild.channels, name='team-a-감독-토크')
    teamA_team_coach_temp = teamA_team_chat.overwrites
    temp = await ctx.guild.create_text_channel(name='team-a-감독-토크', category=categoryA)
    await temp.edit(overwrites=teamA_team_coach_temp)
    await teamA_team_coach.delete()

    # B팀 카테고리
    categoryB = get(ctx.guild.categories, name='⚽  TEAM B')
    #  - 팀채팅
    teamB_team_chat = get(ctx.guild.channels, name='team-b-팀채팅')
    teamB_team_chat_temp = teamB_team_chat.overwrites
    temp = await ctx.guild.create_text_channel(name='team-b-팀채팅', category=categoryB)
    await temp.edit(overwrites=teamB_team_chat_temp)
    await teamB_team_chat.delete()
    #  - 전술노트
    teamB_team_tatic = get(ctx.guild.channels, name='team-b-전술노트')
    teamB_team_tatic_temp = teamB_team_tatic.overwrites
    temp = await ctx.guild.create_text_channel(name='team-b-전술노트', category=categoryB)
    await temp.edit(overwrites=teamB_team_tatic_temp)
    await teamB_team_tatic.delete()
    #  - 선발명단
    teamB_team_lineup = get(ctx.guild.channels, name='team-b-선발명단')
    teamB_team_lineup_temp = teamB_team_lineup.overwrites
    temp = await ctx.guild.create_text_channel(name='team-b-선발명단', category=categoryB)
    await temp.edit(overwrites=teamB_team_lineup_temp)
    await teamB_team_lineup.delete()
    #  - 출석조사
    teamB_team_check = get(ctx.guild.channels, name='team-b-출석조사')
    teamB_team_check_temp = teamB_team_check.overwrites
    temp = await ctx.guild.create_text_channel(name='team-b-출석조사', category=categoryB)
    await temp.edit(overwrites=teamB_team_check_temp)
    await teamB_team_check.delete()
    #  - 불참-인원관리
    teamB_team_out = get(ctx.guild.channels, name='불참-인원-관리')
    teamB_team_out_temp = teamB_team_out.overwrites
    temp = await ctx.guild.create_text_channel(name='불참-인원-관리', category=categoryB)
    await temp.edit(overwrites=teamB_team_out_temp)
    await teamB_team_out.delete() 
    #  - 주장-토크
    teamB_team_coach = get(ctx.guild.channels, name='team-b-감독-토크')
    teamB_team_coach_temp = teamB_team_coach.overwrites
    temp = await ctx.guild.create_text_channel(name='team-b-감독-토크', category=categoryB)
    await temp.edit(overwrites=teamB_team_coach_temp)
    await teamB_team_coach.delete()

    # C팀 카테고리
    categoryC = get(ctx.guild.categories, name='⚽  TEAM C')
    #  - 팀채팅
    teamC_team_chat = get(ctx.guild.channels, name='team-c-팀채팅')
    teamC_team_chat_temp = teamC_team_chat.overwrites
    temp = await ctx.guild.create_text_channel(name='team-c-팀채팅', category=categoryC)
    await temp.edit(overwrites=teamC_team_chat_temp)
    await teamC_team_chat.delete()
    #  - 전술노트
    teamC_team_tatic = get(ctx.guild.channels, name='team-c-전술노트')
    teamC_team_tatic_temp = teamC_team_tatic.overwrites
    temp = await ctx.guild.create_text_channel(name='team-c-전술노트', category=categoryC)
    await temp.edit(overwrites=teamC_team_tatic_temp)
    await teamC_team_tatic.delete()
    #  - 선발명단
    teamC_team_lineup = get(ctx.guild.channels, name='team-c-선발명단')
    teamC_team_lineup_temp = teamC_team_lineup.overwrites
    temp = await ctx.guild.create_text_channel(name='team-c-선발명단', category=categoryC)
    await temp.edit(overwrites=teamC_team_lineup_temp)
    await teamC_team_lineup.delete()
    #  - 출석조사
    teamC_team_check = get(ctx.guild.channels, name='team-c-출석조사')
    teamC_team_check_temp = teamC_team_check.overwrites
    temp = await ctx.guild.create_text_channel(name='team-c-출석조사', category=categoryC)
    await temp.edit(overwrites=teamC_team_check_temp)
    await teamC_team_check.delete()
    #  - 불참-인원관리
    teamC_team_out = get(ctx.guild.channels, name='불참-인원-관리')
    teamC_team_out_temp = teamC_team_out.overwrites
    temp = await ctx.guild.create_text_channel(name='불참-인원-관리', category=categoryB)
    await temp.edit(overwrites=teamC_team_out_temp)
    await teamC_team_out.delete()
    #  - 주장-토크
    teamC_team_coach = get(ctx.guild.channels, name='team-c-감독-토크')
    teamC_team_coach_temp = teamC_team_coach.overwrites
    temp = await ctx.guild.create_text_channel(name='team-c-감독-토크', category=categoryC)
    await temp.edit(overwrites=teamC_team_coach_temp)
    await teamC_team_coach.delete()

    # D팀 카테고리
    categoryD = get(ctx.guild.categories, name='⚽ TEAM D')
    #  - 팀채팅
    teamD_team_chat = get(ctx.guild.channels, name='team-d-팀채팅')
    teamD_team_chat_temp = teamD_team_chat.overwrites
    temp = await ctx.guild.create_text_channel(name='team-d-팀채팅', category=categoryD)
    await temp.edit(overwrites=teamD_team_chat_temp)
    await teamD_team_chat.delete()
    #  - 전술노트
    teamD_team_tatic = get(ctx.guild.channels, name='team-d-전술노트')
    teamD_team_tatic_temp = teamD_team_tatic.overwrites
    temp = await ctx.guild.create_text_channel(name='team-d-전술노트', category=categoryD)
    await temp.edit(overwrites=teamD_team_tatic_temp)
    await teamD_team_tatic.delete()
    #  - 선발명단
    teamD_team_lineup = get(ctx.guild.channels, name='team-d-선발명단')
    teamD_team_lineup_temp = teamD_team_lineup.overwrites
    temp = await ctx.guild.create_text_channel(name='team-d-선발명단', category=categoryD)
    await temp.edit(overwrites=teamD_team_lineup_temp)
    await teamD_team_lineup.delete()
    #  - 출석조사
    teamD_team_check = get(ctx.guild.channels, name='team-d-출석조사')
    teamD_team_check_temp = teamD_team_check.overwrites
    temp = await ctx.guild.create_text_channel(name='team-d-출석조사', category=categoryD)
    await temp.edit(overwrites=teamD_team_check_temp)
    await teamD_team_check.delete()
    #  - 불참-인원관리
    teamC_team_out = get(ctx.guild.channels, name='불참-인원-관리')
    teamC_team_out_temp = teamC_team_out.overwrites
    temp = await ctx.guild.create_text_channel(name='불참-인원-관리', category=categoryB)
    await temp.edit(overwrites=teamC_team_out_temp)
    
    await teamC_team_out.delete()
    #  - 주장-토크
    teamD_team_coach = get(ctx.guild.channels, name='team-d-감독-토크')
    teamD_team_coach_temp = teamD_team_coach.overwrites
    temp = await ctx.guild.create_text_channel(name='team-d-감독-토크', category=categoryD)
    await temp.edit(overwrites=teamD_team_coach_temp)
    await teamD_team_coach.delete()

    # E팀 카테고리
    categoryE = get(ctx.guild.categories, name='⚽ TEAM E')
    #  - 팀채팅
    teamE_team_chat = get(ctx.guild.channels, name='team-e-팀채팅')
    teamE_team_chat_temp = teamE_team_chat.overwrites
    temp = await ctx.guild.create_text_channel(name='team-e-팀채팅', category=categoryE)
    await temp.edit(overwrites=teamE_team_chat_temp)
    await teamE_team_chat.delete()
    #  - 전술노트
    teamE_team_tatic = get(ctx.guild.channels, name='team-e-전술노트')
    teamE_team_tatic_temp = teamE_team_tatic.overwrites
    temp = await ctx.guild.create_text_channel(name='team-e-전술노트', category=categoryE)
    await temp.edit(overwrites=teamE_team_tatic_temp)
    await teamE_team_tatic.delete()
    #  - 선발명단
    teamE_team_lineup = get(ctx.guild.channels, name='team-e-선발명단')
    teamE_team_lineup_temp = teamE_team_lineup.overwrites
    temp = await ctx.guild.create_text_channel(name='team-e-선발명단', category=categoryE)
    await temp.edit(overwrites=teamE_team_lineup_temp)
    await teamE_team_lineup.delete()
    #  - 출석조사
    teamE_team_check = get(ctx.guild.channels, name='team-e-출석조사')
    teamE_team_check_temp = teamE_team_check.overwrites
    temp = await ctx.guild.create_text_channel(name='team-e-출석조사', category=categoryE)
    await temp.edit(overwrites=teamE_team_check_temp)
    await teamE_team_check.delete()
    #  - 불참-인원관리
    teamC_team_out = get(ctx.guild.channels, name='불참-인원-관리')
    teamC_team_out_temp = teamC_team_out.overwrites
    temp = await ctx.guild.create_text_channel(name='불참-인원-관리', category=categoryB)
    await temp.edit(overwrites=teamC_team_out_temp)
    await teamC_team_out.delete()
    #  - 주장-토크
    teamE_team_coach = get(ctx.guild.channels, name='team-e-감독-토크')
    teamE_team_coach_temp = teamE_team_coach.overwrites
    temp = await ctx.guild.create_text_channel(name='team-e-감독-토크', category=categoryE)
    await temp.edit(overwrites=teamE_team_coach_temp)
    await teamE_team_coach.delete()
'''
'''
@bot.command()
async def 이적(ctx, before, current, member: discord.Member, price):
    role_names = [role.name for role in ctx.author.roles]
    id_num = "" + str(member.id)
    if "스태프" in role_names:
        if fun.teamNameConvert(before) != fun.teamNameConvert(current):
            li = ['TEAM A', 'TEAM B', 'TEAM C', 'TEAM D', 'TEAM E']
            for role in li:
                await member.remove_roles(role)
            # 역할 변경
            beforeRole = get(member.guild.roles, name=fun.teamNameConvert(before))
            await member.remove_roles(beforeRole)
            currentRole = get(member.guild.roles, name=fun.teamNameConvert(current))
            await member.add_roles(currentRole)
            # 자산 계산
            #  - 원소속팀 +
            if fun.teamNameConvert(before) == 'TEAM_A':
                money = int(worksheet_info.acell('A2').value)
                money = money + int(price)
                worksheet_info.update_acell('A2', str(money))
                # 원소속팀 출석체크 제거
                max = str(int(worksheet_check_A.acell('A1').value) + 1)
                team_list = worksheet_check_A.range('C3:C' + max)
                for i, cell in enumerate(team_list):
                    if str(cell.value) == str(member.id):
                        point = i + 3
                        worksheet_check_A.delete_rows(point)
            elif fun.teamNameConvert(before) == 'TEAM_B':
                money = int(worksheet_info.acell('B2').value)
                money = money + int(price)
                worksheet_info.update_acell('B2', str(money))
                # 원소속팀 출석체크 제거
                max = str(int(worksheet_check_B.acell('A1').value) + 1)
                team_list = worksheet_check_B.range('C3:C' + max)
                for i, cell in enumerate(team_list):
                    if str(cell.value) == str(member.id):
                        point = i + 3
                        print(point)
                        worksheet_check_B.delete_rows(point)
            elif fun.teamNameConvert(before) == 'TEAM_C':
                money = int(worksheet_info.acell('C2').value)
                money = money + int(price)
                worksheet_info.update_acell('C2', str(money))
                # 원소속팀 출석체크 제거
                max = str(int(worksheet_check_C.acell('A1').value) + 1)
                team_list = worksheet_check_C.range('C3:C' + max)
                for i, cell in enumerate(team_list):
                    if str(cell.value) == str(member.id):
                        point = i + 3
                        worksheet_check_C.delete_rows(point)
            elif fun.teamNameConvert(before) == 'TEAM_D':
                money = int(worksheet_info.acell('D2').value)
                money = money + int(price)
                worksheet_info.update_acell('D2', str(money))
                # 원소속팀 출석체크 제거
                max = str(int(worksheet_check_D.acell('A1').value) + 1)
                team_list = worksheet_check_D.range('C3:C' + max)
                for i, cell in enumerate(team_list):
                    if str(cell.value) == str(member.id):
                        print(i)
                        point = i + 3
                        worksheet_check_D.delete_rows(point)
            elif fun.teamNameConvert(before) == 'TEAM_E':
                money = int(worksheet_info.acell('E2').value)
                money = money + int(price)
                worksheet_info.update_acell('E2', str(money))
                # 원소속팀 출석체크 제거
                max = str(int(worksheet_check_E.acell('A1').value) + 1)
                team_list = worksheet_check_E.range('C3:C' + max)
                for i, cell in enumerate(team_list) :
                    if str(cell.value) == str(member.id) :
                        print(i)
                        point = i + 3
                        worksheet_check_E.delete_rows(point)

            #  - 이적팀 -
            if fun.teamNameConvert(current) == 'TEAM_A':
                money = int(worksheet_info.acell('A2').value)
                money = money - int(price)
                worksheet_info.update_acell('A2', str(money))
                # 이적팀 출석체크 추가
                amax = worksheet_check_A.acell('A1').value
                worksheet_check_A.insert_row(["", fun.convertNickname(member.display_name), id_num, fun.convertJupo(member.display_name), 0, 0, 0], int(amax) + 2)
            elif fun.teamNameConvert(current) == 'TEAM_B':
                money = int(worksheet_info.acell('B2').value)
                money = money - int(price)
                worksheet_info.update_acell('B2', str(money))
                # 이적팀 출석체크 추가
                bmax = worksheet_check_B.acell('A1').value
                worksheet_check_B.insert_row(["", fun.convertNickname(member.display_name), id_num, fun.convertJupo(member.display_name), 0, 0, 0], int(bmax) + 2)
            elif fun.teamNameConvert(current) == 'TEAM_C':
                money = int(worksheet_info.acell('C2').value)
                money = money - int(price)
                worksheet_info.update_acell('C2', str(money))
                # 이적팀 출석체크 추가
                cmax = worksheet_check_C.acell('A1').value
                worksheet_check_C.insert_row(["", fun.convertNickname(member.display_name), id_num, fun.convertJupo(member.display_name), 0, 0, 0], int(cmax) + 2)
            elif fun.teamNameConvert(current) == 'TEAM_D':
                money = int(worksheet_info.acell('D2').value)
                money = money - int(price)
                worksheet_info.update_acell('D2', str(money))
                # 이적팀 출석체크 추가
                dmax = worksheet_check_D.acell('A1').value
                worksheet_check_D.insert_row(["", fun.convertNickname(member.display_name), id_num, fun.convertJupo(member.display_name), 0, 0, 0], int(dmax) + 2)
            elif fun.teamNameConvert(current) == 'TEAM_E':
                money = int(worksheet_info.acell('E2').value)
                money = money - int(price)
                worksheet_info.update_acell('E2', str(money))
                # 이적팀 출석체크 추가
                dmax = worksheet_check_E.acell('A1').value
                worksheet_check_E.insert_row(["", fun.convertNickname(member.display_name), id_num, fun.convertJupo(member.display_name), 0, 0, 0], int(dmax) + 2)

            await ctx.send(content=f"<이적> {fun.convertNickname(member.mention)}, {fun.teamNameConvert(before)} -> {fun.teamNameConvert(current)}, {price} 억원으로 이적")


        else:
            ctx.send("```입력한 전 소속팀과 현 소속팀이 같습니다. 다시 입력해주세요.```")
    else:
        await ctx.send("```해당 명령어는 스태프만 사용가능합니다.```")
'''
@bot.command()
async def 팀명단(ctx, *, team_name):
    total = 0
    st = []
    lw = []
    rw = []
    cam = []
    cm = []
    cdm = []
    lb = []
    cb = []
    rb = []
    gk = []
    st_str = ''
    lw_str = ''
    rw_str = ''
    cam_str = ''
    cm_str = ''
    cdm_str = ''
    lb_str = ''
    cb_str = ''
    rb_str = ''
    gk_str = ''

    Role = get(ctx.guild.roles, name=team_name)
    # Role = get(ctx.guild.roles, name="FC Barcelona")
    for member in Role.members :

        if "[" in member.display_name :
            print(member.display_name, myfun.getJupoFromDisplayname2(member.display_name))
            if myfun.getJupoFromDisplayname2(member.display_name) == 'ST' :
                st.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'LW' :
                lw.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'RW' :
                rw.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'CAM' :
                cam.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'CM' :
                cm.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'CDM' :
                cdm.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'LB' :
                lb.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'CB' :
                cb.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'RB' :
                rb.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'GK' :
                gk.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1

    for i in st :
        st_str = st_str + i + "\n"
    for i in lw :
        lw_str = lw_str + i + "\n"
    for i in rw :
        rw_str = rw_str + i + "\n"
    for i in cam :
        cam_str = cam_str + i + "\n"
    for i in cm :
        cm_str = cm_str + i + "\n"
    for i in cdm :
        cdm_str = cdm_str + i + "\n"
    for i in lb :
        lb_str = lb_str + i + "\n"
    for i in cb :
        cb_str = cb_str + i + "\n"
    for i in rb :
        rb_str = rb_str + i + "\n"
    for i in gk :
        gk_str = gk_str + i + "\n"

    embed = discord.Embed(title=f"{team_name} 현황", description=f"총원 : {total} 명", color=0xFF007F)
    embed.add_field(name="ST", value=st_str, inline=True)
    embed.add_field(name="LW", value=lw_str, inline=True)
    embed.add_field(name="RW", value=rw_str, inline=True)
    embed.add_field(name="CAM", value=cam_str, inline=True)
    embed.add_field(name="CM", value=cm_str, inline=True)
    embed.add_field(name="CDM", value=cdm_str, inline=True)
    embed.add_field(name="LB", value=lb_str, inline=True)
    embed.add_field(name="CB", value=cb_str, inline=True)
    embed.add_field(name="RB", value=rb_str, inline=True)
    embed.add_field(name="GK", value=gk_str, inline=True)

    await ctx.send(embed=embed)


@bot.command()
async def 포지션현황(ctx, *, role_name):
#async def 포지션현황(ctx, role:discord.Role):
    st_count = 0
    lw_count = 0
    rw_count = 0
    cam_count = 0
    cm_count = 0
    cdm_count = 0
    lb_count = 0
    cb_count = 0
    rb_count = 0
    gk_count = 0
    num = 0
    total = 0
    newbie_count = 0
    role = get(ctx.guild.roles, name=role_name)

    if role_name == "FA (무소속)":
        fa_role = get(ctx.guild.roles, name="FA (무소속)")
        for member in fa_role.members:
            role_names = [role.name for role in member.roles]
            if "신규" in role_names:
                newbie_count += 1

    for member in role.members:
        total += 1
        if "[" in member.display_name :
            print(member.display_name, myfun.getJupoFromDisplayname2(member.display_name))
            if myfun.getJupoFromDisplayname2(member.display_name) == 'ST' :
                st_count = st_count + 1
                num = num + 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'LW' :
                lw_count = st_count + 1
                num = num + 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'RW' :
                rw_count = rw_count + 1
                num = num + 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'CAM' :
                cam_count = cam_count + 1
                num = num + 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'CM' :
                cm_count = cm_count + 1
                num = num + 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'CDM' :
                cdm_count = cdm_count + 1
                num = num + 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'LB' :
                lb_count = lb_count + 1
                num = num + 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'CB' :
                cb_count = cb_count + 1
                num = num + 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'RB' :
                rb_count = rb_count + 1
                num = num + 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'GK' :
                gk_count = gk_count + 1
                num = num + 1

    embed = discord.Embed(title=f"{role_name} 역할 주포지션 현황", description=f"총원 : {total} 명", color=0xFF007F)
    embed.add_field(name="ST", value=str(st_count) + " 명", inline=True)
    embed.add_field(name="LW", value=str(lw_count) + " 명", inline=True)
    embed.add_field(name="RW", value=str(rw_count) + " 명", inline=True)
    embed.add_field(name="CAM", value=str(cam_count) + " 명", inline=True)
    embed.add_field(name="CM", value=str(cm_count) + " 명", inline=True)
    embed.add_field(name="CDM", value=str(cdm_count) + " 명", inline=True)
    embed.add_field(name="LB", value=str(lb_count) + " 명", inline=True)
    embed.add_field(name="CB", value=str(cb_count) + " 명", inline=True)
    embed.add_field(name="RB", value=str(rb_count) + " 명", inline=True)
    embed.add_field(name="GK", value=str(gk_count) + " 명", inline=True)
    if role_name == "FA (무소속)":
        embed.add_field(name="신규", value=str(newbie_count) + " 명", inline=True)
        embed.add_field(name="기존", value=str(total-newbie_count) + " 명", inline=True)
    embed.set_footer(text="Copyright ⓒ 2020-2023 타임제이(TimeJ) in C.E.F All Right Reserved.")
    await ctx.message.delete()
    await ctx.send(embed=embed)
'''

    await ctx.send(content=f"{role_name} 주포지션 현황\n"
                           f"총 집계 인원 : {total} 명\n"
                           f"ST : {st_count} 명, LW : {lw_count} 명, RW : {rw_count} 명\n"
                           f"CAM : {cam_count} 명, CM : {cm_count} 명, CDM : {cdm_count} 명\n"
                           f"LB : {lb_count} 명, CB : {cb_count}, RB : {rb_count} 명\n"
                           f"GK : {gk_count} 명")'''

@bot.command()
async def 잠수제거(ctx):
    role_names = [role.name for role in ctx.author.roles]
    if "스태프" in role_names:
        CEF_ROLE = get(ctx.guild.roles, name='CEF')
        FIFA23_ROLE = get(ctx.guild.roles, name='피파23 구매자')

        now = datetime.datetime.now()
        now_time = now.strftime('%Y-%m-%d %H:%M:%S')
        #CEF_ROLE = get(ctx.guild.roles, name='테스트1')
        #FIFA23_ROLE = get(ctx.guild.roles, name='테스트2')

        for member in CEF_ROLE.members:
            print(member.display_name)
            if not FIFA23_ROLE in member.roles:
                await ctx.send(content=f"{member.mention} - CEF 권한 삭제 (역할 제거 일자 : {now_time})")
                await member.remove_roles(CEF_ROLE)
    else:
        await ctx.reply("스태프만 사용 가능합니다.")


@bot.command(aliases=["FA"])
async def FA역할부여(ctx):
    FA_Role = get(ctx.guild.roles, name="FA (무소속)")
    team_list = ["Real Madrid", "Liverpool FC", "Atlético de Madrid", "Juventus", "FC Barcelona", "Schema Of Soccer",
                 "FSV mainz 05", "EVT", "FA"]
    role_list = [role.name for role in ctx.author.roles]
    #print(role_list)
    switch = True
    for team_name in team_list:
        if not team_name in role_list:
            switch = False
            #print(team_name, switch)
        else:
            switch = True
            #print(team_name, switch)
            break

    if switch:
        await ctx.reply(content=f"{ctx.author.mention}, 이미 소속이 있습니다.")
    else:
        user = ctx.author
        await user.add_roles(FA_Role)
        await ctx.reply(content=f"{ctx.author.mention}, FA 권한 부여가 완료되었습니다.")


@bot.command(aliases=["FA제거"])
async def FA역할초기화(ctx):
    FA_Role = get(ctx.guild.roles, name="FA (무소속)")
    for member in FA_Role.members:
        await member.remove_roles(FA_Role)
        await ctx.send(content=f"{myfun.getNickFromDisplayname2(member.display_name)} - FA역할 제거 완료")

@bot.command(aliases=["신규제거"])
async def 신규기간초과(ctx):
    role_names = [role.name for role in ctx.author.roles]
    if "스태프" in role_names:
        newbie_Role = get(ctx.guild.roles, name="신규")
        for member in newbie_Role.members:
            key = 0
            # 범위(체크)
            cell_max = worksheet_list.acell('A1').value
            # 범위 내 셀 값 로딩
            range_list = worksheet_list.range('D2:D' + cell_max)
            # 스프레드 체크 및 업데이트
            for i, cell in enumerate(range_list) :
                if str(cell.value) == str(member.id) :
                    check = i + 2
                    key = 1
                    join_date = worksheet_list.acell('B' + str(check)).value
                    temp = join_date.split(" ")
                    print(temp[0], temp[1])
                    temp2 = temp[0].split("-")
                    year = int(temp2[0])
                    month = int(temp2[1])
                    day = int(temp2[2])

                    now_time = datetime.datetime.now()
                    join_datetime = datetime.datetime(year, month, day)
                    result = now_time - join_datetime
                    await ctx.send(content=f"{member.display_name} - 가입일 : {join_date} / {result.days}")
                    print(result.days, type(result.days))
                    if result.days >= 30:
                        nickname = member.display_name.replace('🐤', '')
                        await member.edit(nick=nickname)
                        await member.remove_roles(newbie_Role)
                        staff_channel_id = get(ctx.guild.text_channels, id=707986001036836941)
                        join_list_channel_id = get(ctx.guild.text_channels, id=853895519030083584)
                        await staff_channel_id.send(content=f"{myfun.getNickFromDisplayname2(member.display_name)}"
                                                            f" - 가입일 : {join_date} / {result.days} 일 경과로 신규 역할 제거 완료")
                        await join_list_channel_id.send(content=f"{member.mention} - 가입일 : {join_date} / {result.days} 일 경과로 신규 역할 제거")
                    time.sleep(2)
    else:
        await ctx.reply("스태프만 사용 가능합니다.")


@bot.command(aliases=["FA현황"])
async def FA유저현황(ctx):
    total = 0
    st = []
    lw = []
    rw = []
    cam = []
    cm = []
    cdm = []
    lb = []
    cb = []
    rb = []
    gk = []
    st_str = ''
    lw_str = ''
    rw_str = ''
    cam_str = ''
    cm_str = ''
    cdm_str = ''
    lb_str = ''
    cb_str = ''
    rb_str = ''
    gk_str = ''

    Role = get(ctx.guild.roles, name="FA (무소속)")
    #Role = get(ctx.guild.roles, name="FC Barcelona")
    for member in Role.members:

        if "[" in member.display_name :
            print(member.display_name, myfun.getJupoFromDisplayname2(member.display_name))
            if myfun.getJupoFromDisplayname2(member.display_name) == 'ST' :
                st.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'LW' :
                lw.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'RW' :
                rw.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'CAM' :
                cam.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'CM' :
                cm.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'CDM' :
                cdm.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'LB' :
                lb.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'CB' :
                cb.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'RB' :
                rb.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1
            elif myfun.getJupoFromDisplayname2(member.display_name) == 'GK' :
                gk.append(myfun.getNickFromDisplayname2(member.display_name))
                total += 1

    for i in st:
        st_str = st_str + i + "\n"
    for i in lw:
        lw_str = lw_str + i + "\n"
    for i in rw:
        rw_str = rw_str + i + "\n"
    for i in cam:
        cam_str = cam_str + i + "\n"
    for i in cm:
        cm_str = cm_str + i + "\n"
    for i in cdm:
        cdm_str = cdm_str + i + "\n"
    for i in lb:
        lb_str = lb_str + i + "\n"
    for i in cb:
        cb_str = cb_str + i + "\n"
    for i in rb:
        rb_str = rb_str + i + "\n"
    for i in gk:
        gk_str = gk_str + i + "\n"

    embed = discord.Embed(title=f"FA 명단 현황", description=f"총원 : {total} 명", color=0xFF007F)
    embed.add_field(name="ST", value=st_str, inline=True)
    embed.add_field(name="LW", value=lw_str, inline=True)
    embed.add_field(name="RW", value=rw_str, inline=True)
    embed.add_field(name="CAM", value=cam_str, inline=True)
    embed.add_field(name="CM", value=cm_str, inline=True)
    embed.add_field(name="CDM", value=cdm_str, inline=True)
    embed.add_field(name="LB", value=lb_str, inline=True)
    embed.add_field(name="CB", value=cb_str, inline=True)
    embed.add_field(name="RB", value=rb_str, inline=True)
    embed.add_field(name="GK", value=gk_str, inline=True)

    await ctx.send(embed=embed)


@bot.command(aliases=["신규현황"])
async def 신규유저현황(ctx):
    newbie_Role = get(ctx.guild.roles, name="신규")
    rma_count = 0
    psg_count = 0
    atm_count = 0
    sch_count = 0
    fcb_count = 0
    m05_count = 0
    eve_count = 0
    fa_count = 0
    total_count = 0
    CEF_Role = get(ctx.guild.roles, name="CEF")
    for member in newbie_Role.members:
        role_names = [role.name for role in member.roles]
        total_count += 1
        if "Real Madrid" in role_names:
            rma_count += 1
        elif "PSG" in role_names:
            psg_count += 1
        elif "Atlético de Madrid" in role_names:
            atm_count += 1
        elif "Schema Of Soccer" in role_names:
            sch_count += 1
        elif "FC Barcelona" in role_names:
            fcb_count += 1
        elif "FSV mainz 05" in role_names:
            m05_count += 1
        elif "FA (무소속)" in role_names:
            fa_count += 1

    for member in CEF_Role.members:
        role_names2 = [role.name for role in member.roles]
        if "EVT" in role_names2:
            eve_count +=1

    embed = discord.Embed(title=f"신규 유저 소속 현황", color=0xFF007F)
    # embed.set_thumbnail(url=logo_url)
    embed.add_field(name="RMA", value=str(rma_count) + " 명", inline=True)
    embed.add_field(name="PSG", value=str(psg_count) + " 명", inline=True)
    embed.add_field(name="SCH", value=str(sch_count) + " 명", inline=True)
    embed.add_field(name="ATM", value=str(atm_count) + " 명", inline=True)
    embed.add_field(name="FCB", value=str(fcb_count) + " 명", inline=True)
    embed.add_field(name="M05", value=str(m05_count) + " 명", inline=True)
    embed.add_field(name="EVE(임대)", value=str(eve_count) + " 명", inline=True)
    embed.add_field(name="FA", value=str(fa_count) + " 명", inline=True)
    embed.add_field(name="전체 신규", value=str(total_count) + " 명", inline=True)
    embed.set_footer(text="Copyright ⓒ 2020-2023 타임제이(TimeJ) in C.E.F All Right Reserved.")
    await ctx.message.delete()
    await ctx.send(embed=embed)


@bot.command()
async def 이모지제거(ctx, imoji):
    cef_role = get(ctx.guild.roles, name="CEF")
    imoji_list = ["🌺", "🍀", "🌱"]
    if imoji == "내전리그":
        for member in cef_role.members:
            for imoji2 in imoji_list:
                if imoji2 in member.display_name:
                    nick = member.display_name.replace(imoji2, "")
                    await member.edit(nick=nick)
                    await ctx.send(content=f"{myfun.getNickFromDisplayname2(member.display_name)} - {imoji2} 제거 완료")
    else:
        for member in cef_role.members:
            if imoji in member.display_name:
                nick = member.display_name.replace(imoji, "")
                await member.edit(nick=nick)
                await ctx.send(content=f"{myfun.getNickFromDisplayname2(member.display_name)} - {imoji} 제거 완료")

    await ctx.reply(content=f"{imoji} 이모지 제거 완료")

@bot.command()
async def 바르샤정보기입(ctx):

    conn = sqlite3.connect("FCB.db")
    fcb = get(ctx.guild.roles, name="FC Barcelona")
    for member in fcb.members :
        role_names = [role.name for role in member.roles]
        if "FCB 1군 계약" in role_names:
            data_list = [member.id, myfun.getNickFromDisplayname2(member.display_name),
                         myfun.getJupoFromDisplayname2(member.display_name), "1군", 0]
        elif "La Masia" in role_names:
            data_list = [member.id, myfun.getNickFromDisplayname2(member.display_name),
                         myfun.getJupoFromDisplayname2(member.display_name), "유스", 0]
        print(data_list)
        cur = conn.cursor()
        cur.execute("INSERT INTO fcb_info(id, nickname, position, belong, count) VALUES(?,?,?,?,?)", data_list)
    conn.commit()
    conn.close()

@bot.command()
async def 출석체크(ctx, num, text):
    role_names = [role.name for role in ctx.author.roles]
    # 바르셀로나 소속 확인
    if "FC Barcelona" in role_names:
        await ctx.reply("현재 해당 명령어는 테스트 단계로 바르셀로나에만 적용되어 있습니다.")
    else:
        # 테이블 존재 여부 확인
        conn = sqlite3.connect("FCB.db")
        cur = conn.cursor()

        cur.execute("SELECT COUNT(*) FROM sqlite_master WHERE name=?", )

@bot.command()
async def 임시(ctx):
    li = ["JUV", "ITA", "ITA U-20", "FCB", "LMS", "SCH", "OOL", "RAN", "WOL", "EVE"]
    #li2 = ["JUV", "ITA", "ITA U-20", "FCB", "LMS", "SCH", "OOL", "RAN", "WOL", "EVE"]
    for i in range(10):
        temp = random.choice(li)
        await ctx.send(content=f"{temp}")
        li.remove(temp)


@bot.command(aliases=["KPA"])
async def kpa(ctx):
    role_names = [role.name for role in ctx.author.roles]
    role_list = ["CEF", "EVE", "Juventus", "Atlético de Madrid", "Schema Of Soccer", "FC Barcelona", "FSV mainz 05",
                 "Rangers FC", "Incheon United FC"]
    kpa = get(ctx.guild.roles, name='KPA')
    switch = True
    for role in role_list:
        if role in role_names:
            switch = False
            break
        else:
            switch = True


    if switch:
        user = ctx.author
        await user.add_roles(kpa)
        await ctx.reply("KPA 역할 부여 완료")

    else:
        await ctx.reply("역할 부여 불가")


"""
@bot.command()
async def FA전체부여(ctx):
    CEF_ROLE = get(ctx.guild.roles, name='테스트1')
    team_list = ["Real Madrid", "Liverpool FC", "Atlético de Madrid", "Juventus", "FC Barcelona", "Schema Of Soccer", "FSV mainz 05", "EVT"]

    for member in CEF_ROLE.members:
        switch = True
        role_list = [role.name for role in member.roles]
        for team_name in team_list:
            if team_name in role_list:
                switch = False
                print(team_name, switch)
                pass

        if switch:
            FA_Role = get(ctx.guild.roles, name="FA")
            await member.add_roles(FA_Role)
            await ctx.send(content=f"{myfun.getJupoFromDisplayname2(member.display_name)} - FA 권한 부여")
"""




@bot.event
async def on_reaction_add(reaction, user):
    # 가입절차
    emo = 0
    if user.bot == 1:
        return None
    # 가입 질문 1번---------------------------------------------------------------------------------
    if str(reaction.emoji) == "❤":
        check_key = 1
        key = 0
        now = datetime.datetime.now()
        now_time = now.strftime('%Y-%m-%d %H:%M:%S')
        # 범위(체크)
        cell_max = worksheet_join.acell('A1').value
        cell_data = int(cell_max) + 1
        # 범위 내 셀 값 로딩
        range_list = worksheet_join.range('D2:D' + str(cell_data))

        for cell in range_list:
            if str(cell.value) == str(user.id):
                check_key = 0
                break
            else:
                check_key = 1
        # 가입 시트에 입력
        if check_key == 1:
            name = user.display_name.split('[')
            nickname = name[0]
            if "[" in user.display_name:
                id_num = "" + str(user.id)
                worksheet_join.insert_row(["", now_time, user.display_name, id_num, nickname, 1], int(cell_max) + 1)
                worksheet_left.insert_row(["", now_time, user.display_name, id_num, nickname, 0], int(cell_max) + 1)
    # 가입질문 2번-----------------------------------------------------------------------------------
    # 범위(체크)
    cell_max = worksheet_join.acell('A1').value
    cell_data = int(cell_max) + 1
    # 범위 내 셀 값 로딩
    range_list = worksheet_join.range('D2:D' + str(cell_data))
    for cell in range_list:
        if str(cell.value) == str(user.id):
            check_key = 0
            break
        else:
            check_key = 1
    # 스프레드 체크 및 업데이트
    if str(reaction.emoji) == "1️⃣":
        emo = 1
    elif str(reaction.emoji) == "2️⃣":
        emo = 2
    elif str(reaction.emoji) == "3️⃣":
        emo = 3
    if check_key == 0:
        for i, cell in enumerate(range_list):
            if str(cell.value) == str(user.id):
                check = i + 2
                worksheet_join.update_acell('G' + str(check), str(emo))


@bot.event
async def on_member_update(before, after):
    if before.nick != after.nick and after.nick is not None:
        nickname_log_channel = bot.get_channel(1055799480328409158)
        user = bot.get_user(before.id)
        async for entry in before.guild.audit_logs(limit=1, action=discord.AuditLogAction.member_update) :
            print(f"{entry.user} changed role {entry.target}")
        import datetime
        #embed = discord.Embed(title="닉네임 변경", description=before.name + "#" + before.discriminator, timestamp=datetime.datetime.now())
        embed = discord.Embed(timestamp=datetime.datetime.now())
        embed.set_author(name=before.name + "#" + before.discriminator, icon_url=f'{before.display_avatar}')
        embed.add_field(name="변경 전", value=before.nick)
        embed.add_field(name="변경 후", value=after.nick)
        embed.add_field(name="변경자", value=entry.user, inline=False)
        embed.set_footer(text="ID: " + str(before.id))
        await nickname_log_channel.send(embed=embed)

    elif before.roles != after.roles:
        role_log_channel = bot.get_channel(1058654744865943602)
        before_role_list = [role for role in before.roles]
        after_role_list = [role for role in after.roles]
        async for entry in before.guild.audit_logs(limit=1, action=discord.AuditLogAction.member_role_update):
            pass
        import datetime
        if len(before_role_list) > len(after_role_list):
            embed = discord.Embed(timestamp=datetime.datetime.now(), color=discord.Color.red())
            for role in after_role_list:
                before_role_list.remove(role)
            embed.add_field(name="변경 내용", value=before_role_list[0].mention + " 제거")
        elif len(before_role_list) < len(after_role_list):
            embed = discord.Embed(title=before.name + "#" + before.discriminator,
                                  timestamp=datetime.datetime.now(), color=discord.Color.blue())
            for role in before_role_list:
                after_role_list.remove(role)
            embed.add_field(name="변경 내용", value=after_role_list[0].mention + " 추가")
        embed.set_author(name=before.name + "#" + before.discriminator, icon_url=f'{before.display_avatar}')
        embed.add_field(name="변경자", value=entry.user, inline=False)
        # embed.set_footer(text="ID: " + member.id)

        embed.set_footer(text="ID: " + str(before.id))
        await role_log_channel.send(embed=embed)


@bot.event
async def on_message_edit(message_before, message_after):
    if not message_before.author.bot :
        embed = discord.Embed(timestamp=datetime.datetime.now(), color=discord.Color.yellow())
        embed.add_field(name="작성자", value=message_before.author.mention, inline=False)
        embed.add_field(name="변경 전", value=message_before.content, inline=False)
        embed.add_field(name="변경 후", value=message_after.content, inline=False)
        embed.set_author(name=message_before.name + "#" + message_before.discriminator, icon_url=f'{message_before.display_avatar}')
        embed.add_field(name="변경된 채널", value=message_before.channel.mention)
        message_log_channel = bot.get_channel(1056399063291011082)
        embed.set_footer(text="ID: " + str(message_before.id))
        await message_log_channel.send(embed=embed)


@bot.event
async def on_message_delete(message):
    if not message.author.bot :
        embed = discord.Embed(timestamp=datetime.datetime.now(), color=discord.Color.red())
        embed.add_field(name="작성자", value=message.author.mention, inline=False)
        embed.add_field(name="내용", value=message.content, inline=False)
        embed.add_field(name="삭제된 채널", value=message.channel.mention, inline=False)
        embed.set_author(name=message.author.name + "#" + message.author.discriminator, icon_url=f'{message.author.display_avatar}')
        channel = bot.get_channel(1056399063291011082)
        embed.set_footer(text="ID: " + str(message.id))
        await channel.send(embed=embed)


@bot.event
async def on_voice_state_update(member, before, after):
    voice_log_channel = bot.get_channel(1058670949764972544)
    if before.channel is None and after.channel is not None:
        embed = discord.Embed(timestamp=datetime.datetime.now(), color=discord.Color.blue(), title="입장")
        embed.set_author(name=member.name + "#" + member.discriminator, icon_url=f'{member.display_avatar}')
        embed.add_field(name="유저", value=member.mention)
        embed.add_field(name="채널", value=after.channel.mention)
    elif before.channel is not None and after.channel is None:
        embed = discord.Embed(timestamp=datetime.datetime.now(), color=discord.Color.red(), title="퇴장")
        embed.add_field(name="유저", value=member.mention)
        embed.add_field(name="채널", value=before.channel.mention)
    elif before.channel is not None and after.channel is not None:
        embed = discord.Embed(timestamp=datetime.datetime.now(), color=discord.Color.yellow(), title="이동")
        embed.add_field(name="유저", value=member.mention)
        embed.add_field(name="이전 채널", value=before.channel.mention)
        embed.add_field(name="이후 채널", value=after.channel.mention)
    embed.set_author(name=member.name + "#" + member.discriminator, icon_url=f'{member.display_avatar}')
    embed.set_footer(text="ID: " + str(member.id))

    await voice_log_channel.send(embed=embed)


@bot.event
async def on_member_join(member):
    # 로그
    joinleave_log_channel = bot.get_channel(1058676638008741898)
    create_time = member.created_at
    import datetime
    now_time = datetime.datetime.now()
    c_time = now_time - create_time

    embed = discord.Embed(timestamp=datetime.datetime.now(), color=discord.Color.red())
    embed.add_field(title="계정 생성일", value=f"{create_time.year}년 {create_time.month}월 {create_time.day}일 ({c_time.days} 일)")
    embed.set_author(name=member.mention + " " + member.name + "#" + member.discriminator, icon_url=f'{member.display_avatar}')
    embed.set_footer(text="ID: " + str(member.id))
    await joinleave_log_channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    joinleave_log_channel = bot.get_channel(1058676638008741898)
    create_time = member.created_at
    import datetime
    now_time = datetime.datetime.now()
    c_time = now_time - create_time


    embed = discord.Embed(timestamp=datetime.datetime.now(), color=discord.Color.red())
    embed.add_field(title="계정 생성일", value=f"{create_time.year}년 {create_time.month}월 {create_time.day}일 ({c_time.days} 일)")
    embed.set_author(name=member.mention + " " + member.name + "#" + member.discriminator, icon_url=f'{member.display_avatar}')
    embed.set_footer(text="ID: " + str(member.id))
    await joinleave_log_channel.send(embed=embed)

@bot.event
async def on_reaction_remove(reaction, user):
    pass


@bot.event
async def on_member_remove(member):
    channel = bot.get(member.guild.channels, name="스태프-줄빠따")
    await channel.send(content=f"{member.mention} 유저가 서버를 나갔습니다.")
    # 범위(체크)
    cell_max = worksheet_left.acell('A1').value
    cell_data = int(cell_max) + 1
    # 범위 내 셀 값 로딩
    range_list = worksheet_left.range('D2:D' + str(cell_data))
    for cell in range_list:
        if str(cell.value) == str(member.id):
            check_key = 0
            break
        else:
            check_key = 1
    if check_key == 0:
        for i, cell in enumerate(range_list):
            if str(cell.value) == str(member.id):
                check = i + 2
                temp = worksheet_left.acell('F' + str(check)).value
                left_count = temp + 1
                worksheet_left.update_acell('F' + str(check), left_count)


bot.run(key)
