from aiogram.dispatcher import filters
from aiogram import types, Dispatcher
# from telegram import InlineKeyboardButton
from create_bot import dp, bot
# from keyboards.client_kb import kb_client


# не работающая инлайн кнопка на вето
# async def command_veto(message : types.Message) :
#     if message.text.upper() == 'ВЕТО':
#         keyboard = types.InlineKeyboardMarkup()
#         keyboard.add(types.InlineKeyboardButton(text='ЗА', callback_data = "+"))    
#         # keyboard.add(types.InlineKeyboardButton(text='ПРОТИВ', callback_data = "-"))    
#         await message.reply('Кто-то инициировал протокол ВЕТО.\n \
#             Теперь вы должны проголосовать за ограничение свободы ', message.from_user.id, ' на 1 час\n \
#             Голосование началось')


# async def command_news(message : types.Message):
#     await bot.send_message(message.from_user.id, 'Хочешь новостей?', reply_markup=kb_client)


# def register_handlers_admin(dp: Dispatcher):
    # dp.register_message_handler(command_news, commands=['news']) 


