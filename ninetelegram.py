import telegram
import asyncio
import pyupbit
import numpy as np
import datetime

print("백그라운드 실행")
async def send_daily_message(): #실행시킬 함수명 임의지정
    token = '6685542208:AAEGYx8Z0xRBAq1bWXxUEOOuc3Qw2Kgy6M0'
    chat_id = 5959976794
    bot = telegram.Bot(token = token)

    message = "오늘도 힘내보자"
    await bot.send_message(chat_id,message)


target_time = "2024-01-11 09:00:10"
clock = datetime.datetime.strptime(target_time, "%Y-%m-%d %H:%M:%S")
import time



while True:
    time.sleep(1)
    now = datetime.datetime.now()
    print(now)
    #print("now", now)
    if now > clock:
        asyncio.run(send_daily_message())
        print("백그라운드 종료")
        break




