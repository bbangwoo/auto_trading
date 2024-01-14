import telegram
import asyncio
import pyupbit
import numpy as np
import datetime

print("백그라운드 실행")
async def send_daily_message(message): #실행시킬 함수명 임의지정
    token = '6685542208:AAEGYx8Z0xRBAq1bWXxUEOOuc3Qw2Kgy6M0'
    chat_id = 5959976794
    bot = telegram.Bot(token = token)
    
    message = message
    await bot.send_message(chat_id,message)


target_time = "2024-01-15 08:30:10"
target_time2 = "2024-01-15 15:00:10"
target_time3 = "2024-01-15 18:00:10"

clock = datetime.datetime.strptime(target_time, "%Y-%m-%d %H:%M:%S")
clock2 = datetime.datetime.strptime(target_time2, "%Y-%m-%d %H:%M:%S")
clock3 = datetime.datetime.strptime(target_time3, "%Y-%m-%d %H:%M:%S")
import time



while True:
    time.sleep(1)
    now = datetime.datetime.now()
    print(now)
    #print("now", now)
    if now > clock:
        message = "오늘도 힘내보자!, 시연이 컨디션 물어보자"
        asyncio.run(send_daily_message(message))
        print("백그라운드 종료")
        break

while True:
    time.sleep(1)
    now = datetime.datetime.now()
    print(now)
    #print("now", now)
    if now > clock2:
        message = "긍정적으로, 무조건 잘 될거다. 근성있게 공부하고 일하자"
        asyncio.run(send_daily_message(message))
        print("백그라운드 종료")
        break

while True:
    time.sleep(1)
    now = datetime.datetime.now()
    print(now)
    #print("now", now)
    if now > clock3:
        message = "오늘 하루도 수고했다! 집에가서 운동도 조금은 하고 공부해보자!"
        asyncio.run(send_daily_message(message))
        print("백그라운드 종료")
        break

