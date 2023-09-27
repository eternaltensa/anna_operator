import requests
import aiogram
import json
import telebot
import time
import datetime
import pytz
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters import Text
timezone = pytz.timezone('Etc/GMT')

bot = Bot(token="6610536065:AAEzvNiLgFtUYi5a0lxgcbNYJwukwahiGXc")
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)


@dispatcher.message_handler(Text("Anna"))
async def start_command(message: types.Message):
    print("START")
    global output
    i=0
    while i!=1:
        url = 'https://tropico.op.axcapital.ae/api/auth/token/'
        otvet = requests.post(url, headers={'x-token-id': "hello-bob"},
                              data={
                                  "username": "sardor",
                                  "password": "admin"
                              })
        tokenmain = otvet.json()
        token_start = tokenmain['access']
        refresh = tokenmain['refresh']

        response_start = requests.get('https://tropico.op.axcapital.ae/report/chats/?page=1&ordering=-updated_at',
                                      headers={'Authorization': f'Bearer {str(token_start)}'})
        data = response_start.json()
        print(data)
        count_start = 8
        i = 0
        while i <= int(count_start):
            status_start = data['results'][i]['status']
            id_num_start = data['results'][i]['id']
            name_start = data['results'][i]['name']
            time1 = data['results'][i]['created_at']
            print(f'{status_start}       {id_num_start}         {time1}')
            now = datetime.datetime.now()
            now1 = now.astimezone(timezone)
            nowreal = str(now1).split("+")[0]
            datetime_real = datetime.datetime.fromisoformat(nowreal)
            datetime_obj = datetime.datetime.fromisoformat(time1)
            print(datetime_real)
            print(datetime_obj)
            dif = datetime_real - datetime_obj
            print(str(dif))
            if int(status_start) == 1 and (dif.seconds > 70) and (dif.seconds < 28800):
                print(f'Разница  {id_num_start} больше минуты')
                await bot.send_message(message.chat.id, text=f' Pending messages remain unanswered please take action:  {name_start}')
            i += 1
        time.sleep(70)

if __name__ == "__main__":
    from aiogram import executor

    executor.start_polling(dispatcher)