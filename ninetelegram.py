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

    #message = "오늘도 힘내보자, 시연이 컨디션 물어보자"
    message = message
    await bot.send_message(chat_id,message)


target_time = "2024-01-12 08:30:10"
target_time2 = "2024-01-12 15:00:10"
clock = datetime.datetime.strptime(target_time, "%Y-%m-%d %H:%M:%S")
clock2 = datetime.datetime.strptime(target_time2, "%Y-%m-%d %H:%M:%S")
import time



while True:
    time.sleep(1)
    now = datetime.datetime.now()
    print(now)
    #print("now", now)
    if now > clock:
        message = "오늘도 힘내보자, 시연이 컨디션 물어보자"
        asyncio.run(send_daily_message(message))
        print("백그라운드 종료")
        break

while True:
    time.sleep(1)
    now = datetime.datetime.now()
    print(now)
    #print("now", now)
    if now > clock2:
        message = "긍정적으로, 무조건 잘 될거다. 잘 이야기하고 오자!"
        asyncio.run(send_daily_message(message))
        print("백그라운드 종료")
        break


