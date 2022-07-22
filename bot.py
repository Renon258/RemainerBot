from pydoc import cli
from create_bot import dp
from aiogram.utils import executor

from handlers import client, admin, other

from datetime import datetime

async def on_startup(_):
    now = datetime.now()
    print(now.strftime('%d-%m-%Y %H:%M:%S') + ' - Bot is working')
    with open('logs.txt', 'a') as file:
        file.write('-------------------------------------------------------\n')
        file.write(now.strftime('%d-%m-%Y %H:%M:%S') + ' - Bot is working\n')

async def on_shudown(_):
    now = datetime.now()
    print(now.strftime('%d-%m-%Y %H:%M:%S') + ' - Bot stops working')
    with open('logs.txt', 'a') as file:
        file.write(now.strftime('%d-%m-%Y %H:%M:%S') + ' - Bot stops working\n')
        file.write('-------------------------------------------------------\n')

client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shudown)