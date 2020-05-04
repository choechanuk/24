# -*# -*- coding:utf-8 -*-

import discord
import asyncio
import re
import requests
import asyncio
from json import loads

token = 'process.env.token'

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("방송 알림이"))
    print("Ready!") # l'm Ready! 문구 출력 print(client.user.name)
    print(client.user.id) #봇의 discord 고유 ID 를 출력 

  
    @client.event
    async def on_message(message): #메세지가 들어오면 가동됌
        
    

        if message.author.bot: #채팅을 친 사람이 봇일 경우
            return None         #반응하지 않고 문장을 종료..

        print(message.content)

        if message.content == "!명령어":
            await message.channel.send("ㅋㅋ,이잉,딱대,지건,**아(이름)")

        if message.content == "준비됐어 지?":
            await message.channel.send("물론이지. 환 (괴물쥐 on)")

        if message.content == "쓰흡":
            await message.channel.send("치이이이이이익")

        if message.content == "ㅋㅋ":
            await message.channel.send("루빵삥뽕")
            
        if message.content == "이잉":
            await message.channel.send("기뮤뤼잉~")

        if message.content == "딱대":
            await message.channel.send("시발")
            
        if message.content == "지건":
            await message.channel.send("딱대 시발!")

        if message.content == "세환아":
            await message.channel.send("공무원 시험 합격은 에듀윌")
            
        if message.content == "지훈아":
            await message.channel.send("아앙~기분조아~")

        if message.content == "찬욱아":
            await message.channel.send("까미 출현 딱대")

        if message.content == "상훈아":
            await message.channel.send("에~에~")

        if message.content == "시원아":
            await message.channel.send("말대꾸 하지마!!!!!!!!!")

        if message.content == "도헌아":
            await message.channel.send("물 마시다 뒤졌냐?")

        if message.content == "도헌이":
            await message.channel.send("또 뒤졌네 그만뒤져!!!!!!!!!!!!")

        if message.content == "강훈아":
            await message.channel.send("쉐엣~")

        if message.content == "성민아":
            await message.channel.send("타다아악!!!!!!!!!")

        if message.content == "지원아": 
            await message.channel.send("ㄷㅊ그냥  숨도 쉬지마")

        if message.content == "용은아":
            await message.channel.send("미안한데")
            
        if message.content == "솔지야":
            await message.channel.send("아진짜?")
            
        if message.content == "얼음아":
            await message.channel.send("난다요")

        if message.content == "나경아":
            await message.channel.send("네 이나경 전화 받았습니다")

        if message.content == "까미야":
            await message.channel.send("찬욱: 왜불렁~")

        if message.content == "지환아":
            await message.channel.send("역겨워")

        if message.content == "지훈":
            await message.channel.send("넣을게...")

        if message.content == "호길아":
            await message.channel.send("이거 맞아?")
                                       
        if message.content == "범수야":
            await message.channel.send("느려")

        if message.content == "리치야":
            await message.channel.send("야옹~")

        if message.content == "주언아":
            await message.channel.send("Not Bad.")

        if message.content == "루이야":
            await message.channel.send("망! 망!")

        if message.content == "재훈아":
            await message.channel.send("뭔데")
        

            
    twitch = "괴물쥐123"
    name = "괴물쥐"
    channel = client.get_channel(705809830803275926)
    a = 0
    while True:
        headers = {'client-ID': 'o5l9y7f1kkxo4j2lxvhwv6y4uvnski'}
        response = requests.get(" https://api.twitch.tv/helix/streams?user_login=" +twitch, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await channel.send(name + "괴물쥐123님이 방송중입니다.")
                a = 1
        except:
            a = 0
        await asyncio.sleep(3)
   

client.run(token)
