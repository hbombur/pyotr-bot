from aiogram import Dispatcher, types
from create_bot import dp, bot
# from keyboards import kb_client

# Функция
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет, я Пётр, весьма галантный попугай.')
        await message.delete()
    except:
        user_name = message.from_user.username
        await message.reply('А ну ', user_name,' пойдем отойдем в ЛС\nhttps://t.me/Bot_pyotr_bot')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help']) 
    
    # dp.register_message_handler() 
    # dp.register_message_handler() 
    
    