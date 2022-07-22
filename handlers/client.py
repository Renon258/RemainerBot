from create_bot import bot, dp
from aiogram import Dispatcher, types

# @dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приветствую вас!')
    except:
        await message.delete()

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
