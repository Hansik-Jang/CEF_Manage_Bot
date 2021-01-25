import discord
import asyncio
import string
import random
import os
import time
import datetime
from discord.ext import commands
from discord.utils import get
from PIL import Image, ImageDraw, ImageFont
from oauth2client.service_account import ServiceAccountCredentials
import pytesseract
import gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1552A1axMJDfxN7kv1TyohmJ3VqKNa7mBeQstHoIRpUQ')
# sh2 = gc.open_by_key('1OP8XMpM93DPScaHX9hGtukf-qaZyalVgzhF--8i2e7')
worksheet_list = sh.worksheet('명단')
worksheet_join = sh.worksheet('가입')
worksheet_left = sh.worksheet('탈퇴')
worksheet_career = sh.worksheet('경력')
worksheet_check_A = sh.worksheet('출첵A')
worksheet_check_B = sh.worksheet('출첵B')
worksheet_check_C = sh.worksheet('출첵C')
worksheet_check_D = sh.worksheet('출첵D')

bot = commands.Bot(command_prefix="%")
team = "무소속"
image_types = ["png", "jpeg", "jpg"]

f = open("key.txt", 'r')
key = f.readline()


@bot.event
async def on_ready():
    print("로그인 중")
    print(bot.user.name)
    print(bot.user.id)
    print('........')
    game = discord.Game("'%도움말2' | 관리봇")
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.command()
async def 테스트(ctx):
    print(key)



@bot.command()
async def 테스트2(ctx):
    time = datetime.datetime.now()
    time_before = datetime.datetime(time.year, time.month, time.day, 20, 00, 00)
    time_after = datetime.datetime(time.year, time.month, time.day, 23, 00, 00)
    test_role = get(ctx.guild.roles, name='테스트')
    A_check_channel = bot.get_channel(800389977472237618)
    if time > time_before and time < time_after:

        await ctx.send("시간 초과")
    else:
        await ctx.send(content=f"{test_role.mention}")

@bot.command()
async def 시트링크(ctx):
    await ctx.send("https://docs.google.com/spreadsheets/d/1552A1axMJDfxN7kv1TyohmJ3VqKNa7mBeQstHoIRpUQ/edit?usp=sharing")

@bot.command()
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
        embed.add_field(name="설명", value="입력한 팀 이름과 멘션에 맞춰 팀 역할이 부여되며,\n"
                                         "스프레드 시트에 업데이트 됩니다.\n"
                                         "팀 이름 : TEAM_A, TEAM_B, TEAM_C, TEAM_D", inline=False)
        embed.add_field(name="사용방법", value="%역할부여 <팀이름> @멘션", inline=True)
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
                                         "ST, LW, RW, CAM, CM, CDM, LB, CB, RB, GK, ALL 중에 입력 가능합니다.", inline=False)

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


@bot.command()
async def 가입(ctx):
    join_key = 1
    key = 0
    now = datetime.datetime.now()
    now_time = now.strftime('%Y-%m-%d %H:%M:%S')
    answer = 0
    # 범위(체크)
    cell_max = worksheet_list.acell('A1').value
    join_max = worksheet_join.acell('A1').value
    cell_data = int(cell_max) + 1
    # 범위 내 셀 값 로딩
    range_list = worksheet_list.range('D2:D' + str(cell_data))
    join_list = worksheet_join.range('D3:D' + str(join_max))

    for cell in range_list:
        if str(cell.value) == str(ctx.author.id):
            join_key = 0
            break
        else:
            join_key = 1

    for i, cell in enumerate(join_list):
        if str(cell.value) == str(ctx.author.id):
            temp = i + 2
            q1 = worksheet_join.acell('F' + str(temp)).value
            q2 = worksheet_join.acell('G' + str(temp)).value
            answer = int(q1) + int(q2)
            print(q1, q2, answer)

    # 닉네임 양식 체크, 분리 및 시트 등록
    # answer == 3:
    if join_key == 1:
        temp = ctx.author.display_name.split('[')
        nickname = temp[0]
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
                if key == 0:
                    id_num = "" + str(ctx.author.id)
                    worksheet_list.insert_row(
                        ["", now_time, ctx.author.display_name, id_num, nickname, jupo, bupo, '무소속',
                         '0000-00-00 00:00:00'], int(cell_max) + 1)
                    worksheet_career.insert_row(
                        ["", now_time, ctx.author.display_name, id_num, nickname, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0], int(cell_max) + 1)
                    await ctx.send(content=f"```{ctx.author.display_name}님 정상 등록되었습니다.```")
                    user = ctx.author
                    role = get(ctx.guild.roles, name='신CEF')
                    role2 = get(ctx.guild.roles, name='CEF')
                    await user.add_roles(role)
                    await user.add_roles(role2)
                    channel = bot.get_channel(709025283306684457)
                    await channel.send(content=f"{ctx.author.mention} 신규가입")
                    channel2 = bot.get_channel(713717100769837126)
                    await channel2.send(content=f"가입일자 : {now_time}\n"
                                                f"{ctx.author.mention}")

            else:
                a = temp[1].split(']')
                jupo = a[0]
                id_num = "" + str(ctx.author.id)
                worksheet_list.insert_row(
                    ["", now_time, ctx.author.display_name, id_num, nickname, jupo, '', '무소속',
                     '0000-00-00 00:00:00'], int(cell_max) + 1)
                worksheet_career.insert_row(
                    ["", now_time, ctx.author.display_name, id_num, nickname, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0], int(cell_max) + 1)
                await ctx.send(content=f"```{ctx.author.display_name}님 정상 등록되었습니다.```")
                user = ctx.author
                role = get(ctx.guild.roles, name='신CEF')
                role2 = get(ctx.guild.roles, name='CEF')
                await user.add_roles(role)
                await user.add_roles(role2)
                channel = bot.get_channel(709025283306684457)
                await channel.send(content=f"{ctx.author.mention} 신규가입")
                channel2 = bot.get_channel(713717100769837126)
                await channel2.send(content=f"가입일자 : {now_time}\n"
                                            f"{ctx.author.mention}")

        else:
            await ctx.send("```정확한 닉네임 양식을 지켜주세요\n닉네임 양식 : 닉네임[주포지션/부포지션] or 닉네임[주포지션]```")
    else:
        await ctx.send(content=f"{ctx.author.mention} 님은 이미 가입되었습니다.")
    # answer == 2:
    #    await ctx.send("```'1번. 클럽원 간의 과도한 경쟁' 은 정답이 아닙니다.```")
    # elif answer == 4:
    #    await ctx.send("```'3번. 반말 사용 등 클럽원간의 과한 친목' 은 C.E.F에서 가장 금지시 하는 행위입니다.```")


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


# 주 포지션 업데이트
@bot.command()
async def 주포변경(ctx, *, text):
    pos_list = ['ST', 'LW', 'RW', 'CAM', 'CM', 'CDM', 'LB', 'CB', 'RB', 'GK', 'ALL', 'AF']
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
    pos_list = ['ST', 'LW', 'RW', 'CAM', 'CM', 'CDM', 'LB', 'CB', 'RB', 'GK', 'ALL', 'AF']
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
    await ctx.send(color)


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

    await ctx.message.delete()


# 닉네임 업데이트
@bot.command()
async def 닉변(ctx):
    key = 0
    role_names = [role.name for role in ctx.author.roles]
    # 범위(체크)
    cell_max = worksheet_list.acell('A1').value
    a_max = str(int(worksheet_check_A.acell('A1').value) + 1)
    b_max = str(int(worksheet_check_B.acell('A1').value) + 1)
    c_max = str(int(worksheet_check_C.acell('A1').value) + 1)
    d_max = str(int(worksheet_check_D.acell('A1').value) + 1)
    # 범위 내 셀 값 로딩
    range_list = worksheet_list.range('D2:D' + cell_max)
    team_a_list = worksheet_check_A.range('C3:C' + a_max)
    team_b_list = worksheet_check_B.range('C3:C' + b_max)
    team_c_list = worksheet_check_C.range('C3:C' + c_max)
    team_d_list = worksheet_check_D.range('C3:C' + d_max)
    name = ctx.author.display_name.split('[')
    check = 0
    # 스프레드 체크 및 업데이트
    for i, cell in enumerate(range_list):
        if str(cell.value) == str(ctx.author.id):
            check = i + 2
            ex_name = worksheet_list.acell('C' + str(check)).value
            worksheet_list.update_acell('C' + str(check), ctx.author.display_name)
            worksheet_list.update_acell('E' + str(check), str(name[0]))
            worksheet_career.update_acell('C' + str(check), ctx.author.display_name)
            worksheet_career.update_acell('E' + str(check), str(name[0]))
            if "TEAM_A" in role_names:
                for j, cell2 in enumerate(team_a_list):
                    if str(cell2.value) == str(ctx.author.id):
                        check = i + 3
                        worksheet_check_A.update_acell('B' + str(check), ctx.author.display_name)
                        break
            elif "TEAM_B" in role_names:
                for j, cell2 in enumerate(team_b_list):
                    if str(cell2.value) == str(ctx.author.id):
                        check = i + 3
                        worksheet_check_B.update_acell('B' + str(check), ctx.author.display_name)
                        break
            elif "TEAM_C" in role_names:
                for j, cell2 in enumerate(team_c_list):
                    if str(cell2.value) == str(ctx.author.id):
                        check = i + 3
                        worksheet_check_C.update_acell('B' + str(check), ctx.author.display_name)
                        break
            elif "TEAM_D" in role_names:
                for j, cell2 in enumerate(team_d_list):
                    if str(cell2.value) == str(ctx.author.id):
                        check = i + 3
                        worksheet_check_D.update_acell('B' + str(check), ctx.author.display_name)
                        break
            key = 1
            await ctx.send(
                content=f"```닉네임 변경을 정상적으로 업데이트하였습니다.\n"
                        f"이전 닉네임 : {ex_name} --> 현재 닉네임 : {name[0]}\n"
                        f"디스코드 내 닉네임은 직접 수정해주세요.\n"
                        f"닉네임변경 명령어는 디스코드 내 닉네임을 먼저 수정한 후 사용해야 정상적으로 처리됩니다.```")
            break
        else:
            key = 0

    if key == 0:
        await ctx.send(content=f"```스프레드 시트에서 {ctx.author.display_name}님의 이름을 검색할 수 없습니다.\n"
                               f"%가입 명령어를 사용해 스프레드 시트에 등록하거나\n"
                               f"%닉변 명령어를 사용해 닉네임을 업데이트해주세요.```")

    await ctx.message.delete()


# 역할 부여하기
@bot.command()
async def 역할부여(ctx, team_name, member: discord.Member):
    ju_po = ""
    role_names = [role.name for role in ctx.author.roles]
    await ctx.message.delete()
    if '스태프' in role_names:
        key = 0
        role = get(member.guild.roles, name=team_name)
        id_num = "" + str(member.id)
        # 오타체크
        role_list = ["TEAM_A", "TEAM_B", "TEAM_C", "TEAM_D"]
        if role.name in role_list:
            type_error = 1
        else:
            type_error = 0
        # 범위(체크)
        cell_max = worksheet_list.acell('A1').value
        a_max = worksheet_check_A.acell('A1').value
        b_max = worksheet_check_B.acell('A1').value
        c_max = worksheet_check_C.acell('A1').value
        d_max = worksheet_check_D.acell('A1').value
        # 범위 내 셀 값 로딩
        range_list = worksheet_list.range('C2:C' + cell_max)

        # 스프레드 체크 및 업데이트
        for i, cell in enumerate(range_list):
            if str(cell.value) == str(member.display_name):
                check = i + 2
                list_pos = i
                ju_po = worksheet_list.acell('F' + str(check)).value
                key = 1
                break
        if type_error == 1 & key == 1:
            worksheet_list.update_acell('H' + str(list_pos + 2), team_name)
            await member.add_roles(role)
            await ctx.send(content=f"<소속 변경>\n"
                                   f"{member.mention} -> {team_name} 배정")

            if team_name == "TEAM_A":
                worksheet_check_A.insert_row(["", member.display_name, id_num, ju_po, 0, 0, 0], int(a_max) + 2)
            if team_name == "TEAM_B":
                worksheet_check_B.insert_row(["", member.display_name, id_num, ju_po, 0, 0, 0], int(b_max) + 2)
            if team_name == "TEAM_C":
                worksheet_check_C.insert_row(["", member.display_name, id_num, ju_po, 0, 0, 0], int(c_max) + 2)
            if team_name == "TEAM_D":
                worksheet_check_D.insert_row(["", member.display_name, id_num, ju_po, 0, 0, 0], int(d_max) + 2)

        elif type_error == 0:
            await ctx.send("오타 체크 및 팀 이름 확인")
        elif key == 0:
            await ctx.send(content=f"<소속 변경 실패>\n"
                                   f"스프레드 시트에서 {member.mention}님의 이름을 검색할 수 없습니다.\n"
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
        range_list = worksheet_list.range('D2:D' + cell_max)

        # 스프레드 체크 및 업데이트
        if text == '선수':
            for i, cell in enumerate(range_list):
                if str(cell.value) == str(member.id):
                    check = i + 2
                    before = worksheet_career.acell('F' + str(check)).value
                    now = int(before) + 1
                    worksheet_career.update_acell('F' + str(check), str(now))
                    key = 1
                    await ctx.send(content=f"```cs\n"
                                           f"{name[0]}님의 선수 커리어가 정상적으로 업데이트되었습니다.\n"
                                           f"이전 선수 우승횟수 : {before} --> 현재 선수 우승횟수 : {now}```")
                else:
                    key = 0


        elif text == '코치':
            for i, cell in enumerate(range_list):
                if str(cell.value) == str(member.id):
                    check = i + 2
                    before = worksheet_career.acell('G' + str(check)).value
                    now = int(before) + 1
                    worksheet_career.update_acell('G' + str(check), str(now))
                    key = 1
                    await ctx.send(content=f"```cs\n"
                                           f"{name[0]}님의 선수 커리어가 정상적으로 업데이트되었습니다.\n"
                                           f"이전 선수 우승횟수 : {before} --> 현재 선수 우승횟수 : {now}```")
                else:
                    key = 0
        if key == 0:
            await ctx.send(content=f"```스프레드 시트에서 {ctx.author.display_name}님의 이름을 검색할 수 없습니다.\n"
                                   f"%가입 명령어를 사용해 스프레드 시트에 등록하거나\n"
                                   f"%닉변 명령어를 사용해 닉네임을 업데이트해주세요.```")

    else:
        await ctx.send("```해당 명령어는 스태프만 사용 가능합니다.```")


# 내 정보 보기
@bot.command()
async def 내정보(ctx):
    key = 0
    # 범위(체크)
    cell_max = worksheet_list.acell('A1').value
    # 범위 내 셀 값 로딩
    range_list = worksheet_list.range('D2:D' + cell_max)
    tots_list = ""
    check = 1
    # 스프레드 체크 및 업데이트
    for i, cell in enumerate(range_list):
        if str(cell.value) == str(ctx.author.id):
            check = i + 2
            key = 1
            id = worksheet_list.acell('D' + str(check)).value
            name = worksheet_list.acell('E' + str(check)).value
            jupo = worksheet_list.acell('F' + str(check)).value
            bupo = worksheet_list.acell('G' + str(check)).value
            team = worksheet_list.acell('H' + str(check)).value
            player_win = worksheet_career.acell('F' + str(check)).value
            coach_win = worksheet_career.acell('G' + str(check)).value
            to_st = worksheet_career.acell('H' + str(check)).value
            to_lw = worksheet_career.acell('I' + str(check)).value
            to_rw = worksheet_career.acell('J' + str(check)).value
            to_cm = worksheet_career.acell('K' + str(check)).value
            to_cdm = worksheet_career.acell('L' + str(check)).value
            to_lb = worksheet_career.acell('M' + str(check)).value
            to_cb = worksheet_career.acell('N' + str(check)).value
            to_rb = worksheet_career.acell('O' + str(check)).value
            to_gk = worksheet_career.acell('P' + str(check)).value
            total_to = worksheet_career.acell('Q' + str(check)).value
            val = worksheet_career.acell('R' + str(check)).value

    if key == 1:
        if "/" in ctx.author.display_name:
            if bupo != "":
                embed = discord.Embed(title=f"내 정보", description=f"{ctx.author.display_name} 님의 정보창", color=0xFF007F)
                embed.add_field(name="고유 ID 번호", value=id, inline=False)
                embed.add_field(name="닉네임", value=name, inline=True)
                embed.add_field(name="주포지션", value=jupo, inline=True)
                embed.add_field(name="부포지션", value=bupo, inline=True)
                embed.add_field(name="소속팀", value=f"{team}", inline=True)
                embed.add_field(name="선수 우승", value=f"{player_win} 회", inline=True)
                embed.add_field(name="코치 우승", value=f"{coach_win} 회", inline=True)
                embed.add_field(name="발롱도르", value=f"{val} 회", inline=True)
                embed.add_field(name="토츠",
                                value=f"총 수상 횟수 : {total_to} 회\nST : {to_st} 회   / LB : {to_lb} 회\nLW : {to_lw} 회  / CB : {to_cb} 회\n"
                                      f"RW : {to_rw} 회  / RB : {to_rb} 회\nCAM/CM : {to_cm} 회\nCDM : {to_cdm} 회 / GK : {to_gk} 회",
                                inline=True)
                embed.set_footer(text="Copyright ⓒ 2020-2021 타임제이(TimeJ) in C.E.F All Right Reserved.")

                await ctx.send(embed=embed)
            else:
                await ctx.send("디스코드 닉네임과 시트 상의 데이터가 일치하지 않습니다.\n")
        else:
            if bupo == "":
                embed = discord.Embed(title=f"내 정보", description=f"{ctx.author.display_name} 님의 정보창", color=0xFF007F)
                embed.add_field(name="고유 ID 번호", value=id, inline=False)
                embed.add_field(name="닉네임", value=name, inline=True)
                embed.add_field(name="주포지션", value=jupo, inline=True)
                embed.add_field(name="부포지션", value="없음", inline=True)
                embed.add_field(name="소속팀", value=f"{team}", inline=False)
                embed.add_field(name="선수 우승", value=f"{player_win} 회", inline=True)
                embed.add_field(name="코치 우승", value=f"{coach_win} 회", inline=True)
                embed.add_field(name="발롱도르", value=f"{val} 회", inline=True)
                embed.add_field(name="토츠",
                                value=f"총 수상 횟수 : {total_to} 회\nST : {to_st} 회   / LB : {to_lb} 회\nLW : {to_lw} 회  / CB : {to_cb} 회\n"
                                      f"RW : {to_rw} 회  / RB : {to_rb} 회\nCAM/CM : {to_cm} 회\nCDM : {to_cdm} 회 / GK : {to_gk} 회",
                                inline=True)

                embed.set_footer(text="Copyright ⓒ 2020-2021 타임제이(TimeJ) in C.E.F All Right Reserved.")

                await ctx.send(embed=embed)
            else:
                await ctx.send(content=f"```스프레드 시트에서 {ctx.author.display_name}님의 이름을 검색할 수 없습니다.\n"
                                       f"%가입 명령어를 사용해 스프레드 시트에 등록하거나\n"
                                       f"%닉변 명령어를 사용해 닉네임을 업데이트해주세요.")
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
    range_list = worksheet_list.range('C2:C' + cell_max)
    if "스태프" in role_names:
        # 중복 체크
        for cell in range_list:
            if cell.value == member.display_name:
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
                if str(cell.value) == str(member.display_name):
                    print(1)
                    check = i + 2
                    before = worksheet_career.acell('R' + str(check)).value
                    now_num = int(before) + 1
                    worksheet_career.update_acell('R' + str(check), str(now_num))
                    await ctx.send(content=f"```cs\n"
                                           f"{member.display_name} 님의 발롱도르 업데이트가 정상적으로 되었습니다.\n"
                                           f"이전 기록 : {before}회 --> 현재 기록 : {now_num}회```")
                else:
                    print(2)
        else:
            await ctx.send(content=f"```스프레드 시트에서 {ctx.author.display_name}님의 이름을 검색할 수 없습니다.\n"
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
    range_list = worksheet_list.range('C2:C' + cell_max)

    # 중복 체크
    for cell in range_list:
        if cell.value == member.display_name:
            key = 1
            break
            print("성공")
        else:
            key = 0
            print(key)
            print(str(cell.value) + " / " + str(member.display_name))
            print("실패")
    check = 1
    if "스태프" in role_names:
        # 스프레드 체크 및 업데이트
        if key == 1:
            if position == 'ST':
                for i, cell in enumerate(range_list):
                    if str(cell.value) == str(member.display_name):
                        check = i + 2
                        before = worksheet_career.acell('H' + str(check)).value
                        before_to = worksheet_career.acell('Q' + str(check)).value
                        now_to = int(before_to) + 1
                        now_num = int(before) + 1
                        worksheet_career.update_acell('H' + str(check), now_num)
                        worksheet_career.update_acell('Q' + str(check), now_to)
                        await ctx.send(content=f"```cs\n"
                                               f"{member.display_name} 님의 토츠 ST 항목이 정상적으로 업데이트 되었습니다.\n"
                                               f"이전 ST 토츠 기록 : {before}회 --> 현재 토츠 ST 기록 : {now_num}회\n"
                                               f"이전 총 토츠 기록 : {before_to}회 --> 현재 총 토츠 기록 : {now_to}회```")
            elif position == 'LW':
                for i, cell in enumerate(range_list):
                    if str(cell.value) == str(member.display_name):
                        check = i + 2
                        before = worksheet_career.acell('I' + str(check)).value
                        before_to = worksheet_career.acell('Q' + str(check)).value
                        now_to = int(before_to) + 1
                        now_num = int(before) + 1
                        worksheet_career.update_acell('I' + str(check), now_num)
                        worksheet_career.update_acell('Q' + str(check), now_to)
                        await ctx.send(content=f"```cs\n"
                                               f"{member.display_name} 님의 토츠 LW 항목이 정상적으로 업데이트 되었습니다.\n"
                                               f"이전 LW 토츠 기록 : {before}회 --> 현재 토츠 LW 기록 : {now_num}회\n"
                                               f"이전 총 토츠 기록 : {before_to}회 --> 현재 총 토츠 기록 : {now_to}회```")
            elif position == 'RW':
                for i, cell in enumerate(range_list):
                    if str(cell.value) == str(member.display_name):
                        check = i + 2
                        before = worksheet_career.acell('J' + str(check)).value
                        before_to = worksheet_career.acell('Q' + str(check)).value
                        now_to = int(before_to) + 1
                        now_num = int(before) + 1
                        worksheet_career.update_acell('J' + str(check), now_num)
                        worksheet_career.update_acell('Q' + str(check), now_to)
                        await ctx.send(content=f"```cs\n"
                                               f"{member.display_name} 님의 토츠 RW 항목이 정상적으로 업데이트 되었습니다.\n"
                                               f"이전 RW 토츠 기록 : {before}회 --> 현재 토츠 RW 기록 : {now_num}회\n"
                                               f"이전 총 토츠 기록 : {before_to}회 --> 현재 총 토츠 기록 : {now_to}회```")
            elif position == 'CM':
                for i, cell in enumerate(range_list):
                    if str(cell.value) == str(member.display_name):
                        check = i + 2
                        before = worksheet_career.acell('K' + str(check)).value
                        before_to = worksheet_career.acell('Q' + str(check)).value
                        now_to = int(before_to) + 1
                        now_num = int(before) + 1
                        worksheet_career.update_acell('K' + str(check), now_num)
                        worksheet_career.update_acell('Q' + str(check), now_to)
                        await ctx.send(content=f"```cs\n"
                                               f"{member.display_name} 님의 토츠 CM 항목이 정상적으로 업데이트 되었습니다.\n"
                                               f"이전 CM 토츠 기록 : {before}회 --> 현재 토츠 CM 기록 : {now_num}회\n"
                                               f"이전 총 토츠 기록 : {before_to}회 --> 현재 총 토츠 기록 : {now_to}회```")
            elif position == 'CDM':
                for i, cell in enumerate(range_list):
                    if str(cell.value) == str(member.display_name):
                        check = i + 2
                        before = worksheet_career.acell('L' + str(check)).value
                        before_to = worksheet_career.acell('Q' + str(check)).value
                        now_to = int(before_to) + 1
                        now_num = int(before) + 1
                        worksheet_career.update_acell('L' + str(check), now_num)
                        worksheet_career.update_acell('Q' + str(check), now_to)
                        await ctx.send(content=f"```cs\n"
                                               f"{member.display_name} 님의 토츠 CDM 항목이 정상적으로 업데이트 되었습니다.\n"
                                               f"이전 CDM 토츠 기록 : {before}회 --> 현재 토츠 CDM 기록 : {now_num}회\n"
                                               f"이전 총 토츠 기록 : {before_to}회 --> 현재 총 토츠 기록 : {now_to}회```")
            elif position == 'LB':
                for i, cell in enumerate(range_list):
                    if str(cell.value) == str(member.display_name):
                        check = i + 2
                        before = worksheet_career.acell('M' + str(check)).value
                        before_to = worksheet_career.acell('Q' + str(check)).value
                        now_to = int(before_to) + 1
                        now_num = int(before) + 1
                        worksheet_career.update_acell('M' + str(check), now_num)
                        worksheet_career.update_acell('Q' + str(check), now_to)
                        await ctx.send(content=f"```cs\n"
                                               f"{member.display_name} 님의 토츠 LB 항목이 정상적으로 업데이트 되었습니다.\n"
                                               f"이전 LB 토츠 기록 : {before}회 --> 현재 토츠 LB 기록 : {now_num}회\n"
                                               f"이전 총 토츠 기록 : {before_to}회 --> 현재 총 토츠 기록 : {now_to}회```")
            elif position == 'CB':
                for i, cell in enumerate(range_list):
                    if str(cell.value) == str(member.display_name):
                        check = i + 2
                        before = worksheet_career.acell('N' + str(check)).value
                        before_to = worksheet_career.acell('Q' + str(check)).value
                        now_to = int(before_to) + 1
                        now_num = int(before) + 1
                        worksheet_career.update_acell('N' + str(check), now_num)
                        worksheet_career.update_acell('Q' + str(check), now_to)
                        await ctx.send(content=f"```cs\n"
                                               f"{member.display_name} 님의 토츠 CB 항목이 정상적으로 업데이트 되었습니다.\n"
                                               f"이전 CB 토츠 기록 : {before}회 --> 현재 토츠 CB 기록 : {now_num}회\n"
                                               f"이전 총 토츠 기록 : {before_to}회 --> 현재 총 토츠 기록 : {now_to}회```")
            elif position == 'RB':
                for i, cell in enumerate(range_list):
                    if str(cell.value) == str(member.display_name):
                        check = i + 2
                        before = worksheet_career.acell('O' + str(check)).value
                        before_to = worksheet_career.acell('Q' + str(check)).value
                        now_to = int(before_to) + 1
                        now_num = int(before) + 1
                        worksheet_career.update_acell('O' + str(check), now_num)
                        worksheet_career.update_acell('Q' + str(check), now_to)
                        await ctx.send(content=f"```cs\n"
                                               f"{member.display_name} 님의 토츠 RB 항목이 정상적으로 업데이트 되었습니다.\n"
                                               f"이전 RB 토츠 기록 : {before}회 --> 현재 토츠 RB 기록 : {now_num}회\n"
                                               f"이전 총 토츠 기록 : {before_to}회 --> 현재 총 토츠 기록 : {now_to}회```")
            elif position == 'GK':
                for i, cell in enumerate(range_list):
                    if str(cell.value) == str(member.display_name):
                        check = i + 2
                        before = worksheet_career.acell('P' + str(check)).value
                        before_to = worksheet_career.acell('Q' + str(check)).value
                        now_to = int(before_to) + 1
                        now_num = int(before) + 1
                        worksheet_career.update_acell('P' + str(check), now_num)
                        worksheet_career.update_acell('Q' + str(check), now_to)
                        await ctx.send(content=f"```cs\n"
                                               f"{member.display_name} 님의 토츠 GK 항목이 정상적으로 업데이트 되었습니다.\n"
                                               f"이전 GK 토츠 기록 : {before}회 --> 현재 토츠 GK 기록 : {now_num}회\n"
                                               f"이전 총 토츠 기록 : {before_to}회 --> 현재 총 토츠 기록 : {now_to}회```")
            else:
                await ctx.send("포지션이 잘못 입력되었습니다.")
        else:
            await ctx.send(content=f"```스프레드 시트에서 {ctx.author.display_name}님의 이름을 검색할 수 없습니다.\n"
                                   f"%가입 명령어를 사용해 스프레드 시트에 등록하거나\n"
                                   f"%닉변 명령어를 사용해 닉네임을 업데이트해주세요.```")
    else:
        await ctx.send("```해당 명령어는 스태프만 사용가능합니다.```")


@bot.command()
async def 출석(ctx, game):
    time_now = datetime.datetime.now()
    time_1st = datetime.datetime(time_now.year, time_now.month, time_now.day, 20, 30, 00)
    time_2nd = datetime.datetime(time_now.year, time_now.month, time_now.day, 21, 00, 00)
    time_3rd = datetime.datetime(time_now.year, time_now.month, time_now.day, 21, 30, 00)
    time_after = datetime.datetime(time_now.year, time_now.month, time_now.day, 23, 00, 00)
    now_month = time_now.strftime('%m')
    now_day = time_now.strftime('%d')
    role_names = [role.name for role in ctx.author.roles]
    # 범위(체크)
    # 범위 내 셀 값 로딩
    name = ctx.author.display_name.split('[')

    if str(ctx.message.channel) == 'team-a-출석조사':
        if "TEAM_A" in role_names:  # A팀 역할 있는지 체크
            a_max = str(int(worksheet_check_A.acell('A1').value) + 1)
            team_a_list = worksheet_check_A.range('C3:C' + a_max)
            for i, cell in enumerate(team_a_list):  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id):
                    temp = i + 3
                    jupo = worksheet_check_A.acell('D' + str(temp)).value
                    if game == '1':
                        if time_1st < time_now and time_now < time_after:
                            await ctx.send("1경기 출석 가능한 시간이 아닙니다.\n"
                                           "출석 가능 시간 - 20:30 까지")
                        else:
                            worksheet_check_A.update_acell('E' + str(temp), '체크')
                            await ctx.send(content=f"```{now_month}월 {now_day}일 A팀 {game}경기\n"
                                                   f"닉네임 : {ctx.author.display_name}\n"
                                                   f"정상적으로 출석참가 되었습니다.```")
                    elif game == '2':
                        if time_2nd < time_now and time_now < time_after:
                            await ctx.send("2경기 출석 가능한 시간이 아닙니다.\n"
                                           "출석 가능 시간 - 21:00 까지")
                        else:
                            worksheet_check_A.update_acell('F' + str(temp), '체크')
                            await ctx.send(content=f"```{now_month}월 {now_day}일 A팀 {game}경기\n"
                                                   f"닉네임 : {ctx.author.display_name}\n"
                                                   f"정상적으로 출석참가 되었습니다.```")
                    elif game == '3':
                        if time_3rd < time_now and time_now < time_after:
                            await ctx.send("2경기 출석 가능한 시간이 아닙니다.\n"
                                           "출석 가능 시간 - 21:00 까지")
                        else:
                            worksheet_check_A.update_acell('G' + str(temp), '체크')
                            await ctx.send(content=f"```{now_month}월 {now_day}일 A팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}\n"
                                               f"정상적으로 출석참가 되었습니다.```")
                    else:
                        await ctx.send("```입력이 잘못되었습니다.```")
        else:
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_A 소속이 아닙니다.```")
    elif str(ctx.message.channel) == 'team-b-출석조사':
        if "TEAM_B" in role_names:  # B팀 역할 있는지 체크
            b_max = str(int(worksheet_check_B.acell('A1').value) + 1)
            team_b_list = worksheet_check_B.range('C3:C' + b_max)
            for i, cell in enumerate(team_b_list):  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id):
                    temp = i + 3
                    jupo = worksheet_check_B.acell('D' + str(temp)).value
                    if game == '1':
                        worksheet_check_B.update_acell('E' + str(temp), '체크')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 B팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}\n"
                                               f"정상적으로 출석참가 되었습니다.```")
                    elif game == '2':
                        worksheet_check_B.update_acell('F' + str(temp), '체크')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 B팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}\n"
                                               f"정상적으로 출석참가 되었습니다.```")
                    elif game == '3':
                        worksheet_check_B.update_acell('G' + str(temp), '체크')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 B팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}\n"
                                               f"정상적으로 출석참가 되었습니다.```")
                    else:
                        await ctx.send("```입력이 잘못되었습니다.```")
        else:
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_B 소속이 아닙니다.```")

    elif str(ctx.message.channel) == 'team-c-출석조사':
        if "TEAM_C" in role_names:  # C팀 역할 있는지 체크
            c_max = str(int(worksheet_check_C.acell('A1').value) + 1)
            team_c_list = worksheet_check_C.range('C3:C' + c_max)
            for i, cell in enumerate(team_c_list):  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id):
                    temp = i + 3
                    jupo = worksheet_check_C.acell('D' + str(temp)).value
                    if game == '1':
                        worksheet_check_C.update_acell('E' + str(temp), '체크')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 C팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}\n"
                                               f"정상적으로 출석참가 되었습니다.```")
                    elif game == '2':
                        worksheet_check_C.update_acell('F' + str(temp), '체크')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 C팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}\n"
                                               f"정상적으로 출석참가 되었습니다.```")
                    elif game == '3':
                        worksheet_check_C.update_acell('G' + str(temp), '체크')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 C팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}\n"
                                               f"정상적으로 출석참가 되었습니다.```")
                    else:
                        await ctx.send("```입력이 잘못되었습니다.```")
        else:
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_C 소속이 아닙니다.```")

    elif str(ctx.message.channel) == 'team-d-출석조사':
        if "TEAM_D" in role_names:  # A팀 역할 있는지 체크
            d_max = str(int(worksheet_check_D.acell('A1').value) + 1)
            team_d_list = worksheet_check_D.range('C3:C' + d_max)
            for i, cell in enumerate(team_d_list):  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id):
                    temp = i + 3
                    jupo = worksheet_check_D.acell('D' + str(temp)).value
                    if game == '1':
                        worksheet_check_D.update_acell('E' + str(temp), '체크')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 D팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}\n"
                                               f"정상적으로 출석참가 되었습니다.```")
                    elif game == '2':
                        worksheet_check_D.update_acell('F' + str(temp), '체크')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 D팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}\n"
                                               f"정상적으로 출석참가 되었습니다.```")
                    elif game == '3':
                        worksheet_check_D.update_acell('G' + str(temp), '체크')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 D팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}\n"
                                               f"정상적으로 출석참가 되었습니다.```")
                    else:
                        await ctx.send("```입력이 잘못되었습니다.```")
        else:
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_D 소속이 아닙니다.```")
    else:
        await ctx.send("각 팀 출석조사 채널에 입력해주세요.")

@bot.command()
async def 출석취소(ctx, game):
    now = datetime.datetime.now()
    now_month = now.strftime('%m')
    now_day = now.strftime('%d')
    role_names = [role.name for role in ctx.author.roles]

    # 범위(체크)
    cell_max = worksheet_list.acell('A1').value
    a_max = str(int(worksheet_check_A.acell('A1').value) + 1)
    b_max = str(int(worksheet_check_B.acell('A1').value) + 1)
    c_max = str(int(worksheet_check_C.acell('A1').value) + 1)
    d_max = str(int(worksheet_check_D.acell('A1').value) + 1)
    # 범위 내 셀 값 로딩
    range_list = worksheet_list.range('D2:D' + cell_max)
    team_a_list = worksheet_check_A.range('C3:C' + a_max)
    team_b_list = worksheet_check_B.range('C3:C' + b_max)
    team_c_list = worksheet_check_C.range('C3:C' + c_max)
    team_d_list = worksheet_check_D.range('C3:C' + d_max)
    name = ctx.author.display_name.split('[')

    ctx.message.delete()

    if str(ctx.message.channel) == 'team-a-출석조사':
        if "TEAM_A" in role_names:  # A팀 역할 있는지 체크
            for i, cell in enumerate(team_a_list):  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id):
                    temp = i + 3
                    print(temp)
                    jupo = worksheet_check_A.acell('D' + str(temp)).value
                    print(jupo)
                    if game == '1':
                        worksheet_check_A.update_acell('E' + str(temp), '0')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 A팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}, 포지션 : {jupo}\n"
                                               f"정상적으로 출석취소 되었습니다.```")
                    elif game == '2':
                        worksheet_check_A.update_acell('F' + str(temp), '0')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 A팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}, 포지션 : {jupo}\n"
                                               f"정상적으로 출석취소 되었습니다.```")
                    elif game == '3':
                        worksheet_check_A.update_acell('G' + str(temp), '0')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 A팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}, 포지션 : {jupo}\n"
                                               f"정상적으로 출석취소 되었습니다.```")
                    else:
                        await ctx.send("```입력이 잘못되었습니다.```")
        else:
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_A 소속이 아닙니다.```")
    elif str(ctx.message.channel) == 'team-b-출석조사':
        if "TEAM_B" in role_names:  # A팀 역할 있는지 체크
            for i, cell in enumerate(team_b_list):  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id):
                    temp = i + 3
                    jupo = worksheet_check_B.acell('D' + str(temp)).value
                    if game == '1':
                        worksheet_check_B.update_acell('E' + str(temp), '0')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 B팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}, 포지션 : {jupo}\n"
                                               f"정상적으로 출석취소 되었습니다.```")
                    elif game == '2':
                        worksheet_check_B.update_acell('F' + str(temp), '0')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 B팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}, 포지션 : {jupo}\n"
                                               f"정상적으로 출석취소 되었습니다.```")
                    elif game == '3':
                        worksheet_check_B.update_acell('G' + str(temp), '0')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 B팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}, 포지션 : {jupo}\n"
                                               f"정상적으로 출석취소 되었습니다.```")
                    else:
                        await ctx.send("```입력이 잘못되었습니다.```")
        else:
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_B 소속이 아닙니다.```")

    elif str(ctx.message.channel) == 'team-c-출석조사':
        if "TEAM_C" in role_names:  # A팀 역할 있는지 체크
            for i, cell in enumerate(team_c_list):  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id):
                    temp = i + 3
                    jupo = worksheet_check_C.acell('D' + str(temp)).value
                    if game == '1':
                        worksheet_check_C.update_acell('E' + str(temp), '0')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 C팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}, 포지션 : {jupo}\n"
                                               f"정상적으로 출석취소 되었습니다.```")
                    elif game == '2':
                        worksheet_check_C.update_acell('F' + str(temp), '0')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 C팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}, 포지션 : {jupo}\n"
                                               f"정상적으로 출석취소 되었습니다.```")
                    elif game == '3':
                        worksheet_check_C.update_acell('G' + str(temp), '0')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 C팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}, 포지션 : {jupo}\n"
                                               f"정상적으로 출석취소 되었습니다.```")
                    else:
                        await ctx.send("```입력이 잘못되었습니다.```")
        else:
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_C 소속이 아닙니다.```")

    elif str(ctx.message.channel) == 'team-d-출석조사':
        if "TEAM_D" in role_names:  # A팀 역할 있는지 체크
            for i, cell in enumerate(team_d_list):  # 1팀 1경기
                if str(cell.value) == str(ctx.author.id):
                    temp = i + 3
                    jupo = worksheet_check_D.acell('D' + str(temp)).value
                    if game == '1':
                        worksheet_check_D.update_acell('E' + str(temp), '0')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 D팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}, 포지션 : {jupo}\n"
                                               f"정상적으로 출석취소 되었습니다.```")
                    elif game == '2':
                        worksheet_check_D.update_acell('F' + str(temp), '0')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 D팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}, 포지션 : {jupo}\n"
                                               f"정상적으로 출석취소 되었습니다.```")
                    elif game == '3':
                        worksheet_check_D.update_acell('G' + str(temp), '0')
                        await ctx.send(content=f"```{now_month}월 {now_day}일 D팀 {game}경기\n"
                                               f"닉네임 : {ctx.author.display_name}, 포지션 : {jupo}\n"
                                               f"정상적으로 출석취소 되었습니다.```")
                    else:
                        await ctx.send("```입력이 잘못되었습니다.```")
        else:
            await ctx.send(content=f"```{ctx.author.display_name} 님은 TEAM_D 소속이 아닙니다.```")
    else:
        await ctx.send("각 팀 출석조사 채널에 입력해주세요.")


@bot.command()
async def 출석결과(ctx, team_name, match_num):
    role_names = [role.name for role in ctx.author.roles]
    switch_name = 0
    switch_num = 0
    st_text = ''
    lw_text = ''
    rw_text = ''
    cam_text = ''
    cm_text = ''
    cdm_text = ''
    lb_text = ''
    cb_text = ''
    rb_text = ''
    gk_text = ''
    allpo_text = ''
    af_text = ''
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
    allpo = []
    af = []
    team_list = []
    nickname = ""
    jupo = ""
    # 범위 체크 및 범위 내 셀 값 로딩
    if team_name == "TEAM_A":
        a_max = str(int(worksheet_check_A.acell('A1').value) + 1)
        a1_list = worksheet_check_A.range('E3:E' + a_max)
        a2_list = worksheet_check_A.range('F3:F' + a_max)
        a3_list = worksheet_check_A.range('G3:G' + a_max)
    elif team_name == "TEAM_B":
        b_max = str(int(worksheet_check_B.acell('A1').value) + 1)
        b1_list = worksheet_check_B.range('E3:E' + b_max)
        b2_list = worksheet_check_B.range('F3:F' + b_max)
        b3_list = worksheet_check_B.range('G3:G' + b_max)
    elif team_name == "TEAM_C":
        c_max = str(int(worksheet_check_C.acell('A1').value) + 1)
        c1_list = worksheet_check_C.range('E3:E' + c_max)
        c2_list = worksheet_check_C.range('F3:F' + c_max)
        c3_list = worksheet_check_C.range('G3:G' + c_max)
    elif team_name == "TEAM_C":
        d_max = str(int(worksheet_check_D.acell('A1').value) + 1)
        d1_list = worksheet_check_D.range('E3:E' + d_max)
        d2_list = worksheet_check_D.range('F3:F' + d_max)
        d3_list = worksheet_check_D.range('G3:G' + d_max)

    # 팀 이름 및 경기 체크
    if team_name == "TEAM_A":
        switch_name = 1
        if match_num == '1':
            for i, cell in enumerate(a1_list):
                if str(cell.value) == '체크':
                    print(1)
                    temp = i + 3
                    nickname = worksheet_check_A.acell('B' + str(temp)).value
                    ju_po = worksheet_check_A.acell('D' + str(temp)).value
                    team_list.append(ju_po + '!' + nickname)
                    switch_num = 1
        elif match_num == '2':
            for i, cell in enumerate(a2_list):
                if str(cell.value) == '체크':
                    print(2)
                    temp = i + 3
                    nickname = worksheet_check_A.acell('B' + str(temp)).value
                    ju_po = worksheet_check_A.acell('D' + str(temp)).value
                    team_list.append(ju_po + '!' + nickname)
                    switch_num = 1
        elif match_num == '3':
            for i, cell in enumerate(a3_list):
                if str(cell.value) == '체크':
                    print(3)
                    temp = i + 3
                    nickname = worksheet_check_A.acell('B' + str(temp)).value
                    ju_po = worksheet_check_A.acell('D' + str(temp)).value
                    team_list.append(ju_po + '!' + nickname)
                    switch_num = 1
        else:
            switch_num = 0

    elif team_name == "TEAM_B":
        switch_name = 1
        if match_num == '1':
            for i, cell in enumerate(b1_list):
                if str(cell.value) == '체크':
                    print(1)
                    temp = i + 3
                    nickname = worksheet_check_B.acell('B' + str(temp)).value
                    ju_po = worksheet_check_B.acell('D' + str(temp)).value
                    team_list.append(ju_po + '!' + nickname)
                    switch_num = 1
        elif match_num == '2':
            for i, cell in enumerate(b2_list):
                if str(cell.value) == '체크':
                    print(2)
                    temp = i + 3
                    nickname = worksheet_check_B.acell('B' + str(temp)).value
                    ju_po = worksheet_check_B.acell('D' + str(temp)).value
                    team_list.append(ju_po + '!' + nickname)
                    switch_num = 1
        elif match_num == '3':
            for i, cell in enumerate(b3_list):
                if str(cell.value) == '체크':
                    print(3)
                    temp = i + 3
                    nickname = worksheet_check_B.acell('B' + str(temp)).value
                    ju_po = worksheet_check_B.acell('D' + str(temp)).value
                    team_list.append(ju_po + '!' + nickname)
                    switch_num = 1
        else:
            switch_num = 0

    elif team_name == "TEAM_C":
        switch_name = 1
        if match_num == '1':
            for i, cell in enumerate(c1_list):
                if str(cell.value) == '체크':
                    print(1)
                    temp = i + 3
                    nickname = worksheet_check_C.acell('B' + str(temp)).value
                    ju_po = worksheet_check_C.acell('D' + str(temp)).value
                    team_list.append(ju_po + '!' + nickname)
                    switch_num = 1
        elif match_num == '2':
            for i, cell in enumerate(c2_list):
                if str(cell.value) == '체크':
                    print(2)
                    temp = i + 3
                    nickname = worksheet_check_C.acell('B' + str(temp)).value
                    ju_po = worksheet_check_C.acell('D' + str(temp)).value
                    team_list.append(ju_po + '!' + nickname)
                    switch_num = 1
        elif match_num == '3':
            for i, cell in enumerate(c3_list):
                if str(cell.value) == '체크':
                    print(3)
                    temp = i + 3
                    nickname = worksheet_check_C.acell('B' + str(temp)).value
                    ju_po = worksheet_check_C.acell('D' + str(temp)).value
                    team_list.append(ju_po + '!' + nickname)
                    switch_num = 1
        else:
            switch_num = 0

    elif team_name == "TEAM_D":
        switch_name = 1
        if match_num == '1':
            for i, cell in enumerate(d1_list):
                if str(cell.value) == '체크':
                    print(1)
                    temp = i + 3
                    nickname = worksheet_check_D.acell('B' + str(temp)).value
                    ju_po = worksheet_check_D.acell('D' + str(temp)).value
                    team_list.append(ju_po + '!' + nickname)
                    switch_num = 1
        elif match_num == '2':
            for i, cell in enumerate(d2_list):
                if str(cell.value) == '체크':
                    print(2)
                    temp = i + 3
                    nickname = worksheet_check_D.acell('B' + str(temp)).value
                    ju_po = worksheet_check_D.acell('D' + str(temp)).value
                    team_list.append(ju_po + '!' + nickname)
                    switch_num = 1
        elif match_num == '3':
            for i, cell in enumerate(d3_list):
                if str(cell.value) == '체크':
                    print(3)
                    temp = i + 3
                    nickname = worksheet_check_D.acell('B' + str(temp)).value
                    ju_po = worksheet_check_D.acell('D' + str(temp)).value
                    team_list.append(ju_po + '!' + nickname)
                    switch_num = 1
        else:
            switch_num = 0
    else:
        switch_name = 0

    print(team_list)
    if switch_name == 1:
        if switch_num == 1:
            # 전체 목록을 포지션에 맞게 분배
            for i in range(0, len(team_list)):
                if team_list[i].startswith("ST"):
                    st.append(team_list[i])
                    print(st)
                if team_list[i].startswith("LW"):
                    lw.append(team_list[i])
                if team_list[i].startswith("RW"):
                    rw.append(team_list[i])
                if team_list[i].startswith("CAM"):
                    cam.append(team_list[i])
                if team_list[i].startswith("CM"):
                    cm.append(team_list[i])
                if team_list[i].startswith("CDM"):
                    cdm.append(team_list[i])
                if team_list[i].startswith("LB"):
                    lb.append(team_list[i])
                if team_list[i].startswith("CB"):
                    cb.append(team_list[i])
                if team_list[i].startswith("RB"):
                    rb.append(team_list[i])
                if team_list[i].startswith("GK"):
                    gk.append(team_list[i])
                if team_list[i].startswith("ALL"):
                    allpo.append(team_list[i])
                if team_list[i].startswith("AF"):
                    af.append(team_list[i])

            # 닉네임 정리------------------------------------------
            for i in range(0, len(st)):
                temp = st[i].split('!')
                print(temp)
                temp_name = temp[1]
                print(temp_name)
                st[i] = temp_name
                print(st[i])
                if i == 0:
                    st_text = st_text + st[i]
                    print(st_text)
                else:
                    st_text = st_text + ", " + st[i]
                    print(st_text)
            for i in range(0, len(lw)):
                temp = lw[i].split('!')
                temp_name = temp[1]
                lw[i] = temp_name
                if i == 0:
                    lw_text = lw_text + lw[i]
                else:
                    lw_text = lw_text + ", " + lw[i]
            for i in range(0, len(rw)):
                temp = rw[i].split('!')
                temp_name = temp[1]
                rw[i] = temp_name
                if i == 0:
                    rw_text = rw_text + rw[i]
                else:
                    rw_text = rw_text + ", " + rw[i]
            for i in range(0, len(cam)):
                temp = cam[i].split('!')
                temp_name = temp[1]
                cam[i] = temp_name
                if i == 0:
                    cam_text = cam_text + cam[i]
                else:
                    cam_text = cam_text + ", " + cam[i]
            for i in range(0, len(cm)):
                temp = cm[i].split('!')
                temp_name = temp[1]
                cm[i] = temp_name
                if i == 0:
                    cm_text = cm_text + cm[i]
                else:
                    cm_text = cm_text + ", " + cm[i]
            for i in range(0, len(cdm)):
                temp = cdm[i].split('!')
                temp_name = temp[1]
                cdm[i] = temp_name
                if i == 0:
                    cdm_text = cdm_text + cdm[i]
                else:
                    cdm_text = cdm_text + ", " + cdm[i]
            for i in range(0, len(lb)):
                temp = lb[i].split('!')
                temp_name = temp[1]
                lb[i] = temp_name
                if i == 0:
                    lb_text = lb_text + lb[i]
                else:
                    lb_text = lb_text + ", " + lb[i]
            for i in range(0, len(cb)):
                temp = cb[i].split('!')
                temp_name = temp[1]
                cb[i] = temp_name
                if i == 0:
                    cb_text = cb_text + cb[i]
                else:
                    cb_text = cb_text + ", " + cb[i]
            for i in range(0, len(rb)):
                temp = rb[i].split('!')
                temp_name = temp[1]
                rb[i] = temp_name
                if i == 0:
                    rb_text = rb_text + rb[i]
                else:
                    rb_text = rb_text + ", " + rb[i]
            for i in range(0, len(gk)):
                temp = gk[i].split('!')
                temp_name = temp[1]
                gk[i] = temp_name
                if i == 0:
                    gk_text = gk_text + gk[i]
                else:
                    gk_text = gk_text + ", " + gk[i]
            for i in range(0, len(allpo)):
                temp = allpo[i].split('!')
                temp_name = temp[1]
                allpo[i] = temp_name
                if i == 0:
                    allpo_text = allpo_text + allpo[i]
                else:
                    allpo_text = allpo_text + ", " + allpo[i]
            for i in range(0, len(af)):
                temp = af[i].split('!')
                temp_name = temp[1]
                af[i] = temp_name
                if i == 0:
                    af_text = af_text + af[i]
                else:
                    af_text = af_text + ", " + af[i]

            await ctx.send(content=f"```{team_name} {match_num}경기 출석체크 결과\n\n"
                                   f" ST : {st_text}\n"
                                   f" LW : {lw_text}\n"
                                   f" RW : {rw_text}\n"
                                   f"CAM : {cam_text}\n"
                                   f" CM : {cm_text}\n"
                                   f"CDM : {cdm_text}\n"
                                   f" LB : {lb_text}\n"
                                   f" CB : {cb_text}\n"
                                   f" RB : {rb_text}\n"
                                   f" GK : {gk_text}\n"
                                   f"ALL : {allpo_text}\n"
                                   f" AF : {af_text}```")
        else:
            await ctx.send("```경기 번호가 잘못 입력하였습니다.\n"
                           "1, 2, 3 중 입력해주세요.```")
    else:
        await ctx.send("```팀 이름이 잘못 입력하였습니다.\n"
                       "오타를 체크해주세요.```")


@bot.command()
async def 출석초기화(ctx):
    role_names = [role.name for role in ctx.author.roles]
    A_check_channel = bot.get_channel(800389977472237618)
    B_check_channel = bot.get_channel(800390440145649664)
    C_check_channel = bot.get_channel(800390149904007188)
    D_check_channel = bot.get_channel(798834938874560552)
    if '스태프' in role_names:
        # 범위(체크)
        a_max = str(int(worksheet_check_A.acell('A1').value) + 1)
        b_max = str(int(worksheet_check_B.acell('A1').value) + 1)
        c_max = str(int(worksheet_check_C.acell('A1').value) + 1)
        d_max = str(int(worksheet_check_D.acell('A1').value) + 1)
        # 범위 내 셀 값 로딩
        team_a_reset_list = worksheet_check_A.range('E3:G' + a_max)
        team_b_reset_list = worksheet_check_B.range('E3:G' + b_max)
        team_c_reset_list = worksheet_check_C.range('E3:G' + c_max)
        team_d_reset_list = worksheet_check_D.range('E3:G' + d_max)

        for cell in team_a_reset_list:
            cell.value = '0'
        for cell in team_b_reset_list:
            cell.value = '0'
        for cell in team_c_reset_list:
            cell.value = '0'
        for cell in team_d_reset_list:
            cell.value = '0'
        worksheet_check_A.update_cells(team_a_reset_list)
        worksheet_check_B.update_cells(team_b_reset_list)
        worksheet_check_C.update_cells(team_c_reset_list)
        worksheet_check_D.update_cells(team_d_reset_list)

        await A_check_channel.send("```출석체크 시트가 모두 초기화 되었습니다.```")
        await B_check_channel.send("```출석체크 시트가 모두 초기화 되었습니다.```")
        await C_check_channel.send("```출석체크 시트가 모두 초기화 되었습니다.```")
        await D_check_channel.send("```출석체크 시트가 모두 초기화 되었습니다.```")
    else:
        await ctx.send("```해당 명령어는 스태프만 사용 가능합니다.```")

@bot.command()
async def 출석공지(ctx):
    role_names = [role.name for role in ctx.author.roles]
    A_role = get(ctx.guild.roles, name='TEAM_A')
    B_role = get(ctx.guild.roles, name='TEAM_B')
    C_role = get(ctx.guild.roles, name='TEAM_C')
    D_role = get(ctx.guild.roles, name='TEAM_D')
    A_check_channel = bot.get_channel(800389977472237618)
    B_check_channel = bot.get_channel(800390440145649664)
    C_check_channel = bot.get_channel(800390149904007188)
    D_check_channel = bot.get_channel(798834938874560552)

    if '스태프' in role_names:
        await A_check_channel.send(content=f"{A_role.mention}\n"
                                           f"출석체크 및 확인 바랍니다.\n"
                                           f"1경기 출석 가능 시간 : 전날 23:00 ~ 당일 20:30\n"
                                           f"2경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:00\n"
                                           f"3경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:00\n")
        await B_check_channel.send(content=f"{B_role.mention}\n"
                                           f"출석체크 및 확인 바랍니다.\n"
                                           f"1경기 출석 가능 시간 : 전날 23:00 ~ 당일 20:30\n"
                                           f"2경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:00\n"
                                           f"3경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:00\n")
        await C_check_channel.send(content=f"{C_role.mention}\n"
                                           f"출석체크 및 확인 바랍니다.\n"
                                           f"1경기 출석 가능 시간 : 전날 23:00 ~ 당일 20:30\n"
                                           f"2경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:00\n"
                                           f"3경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:00\n")
        await D_check_channel.send(content=f"{D_role.mention}\n"
                                           f"출석체크 및 확인 바랍니다.\n"
                                           f"1경기 출석 가능 시간 : 전날 23:00 ~ 당일 20:30\n"
                                           f"2경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:00\n"
                                           f"3경기 출석 가능 시간 : 전날 23:00 ~ 당일 21:00\n")
    else:
        await ctx.send("```해당 명령어는 스태프만 사용 가능합니다.```")


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
