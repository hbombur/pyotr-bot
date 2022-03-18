from aiogram import types, Dispatcher
import string, json

# with open("cenz.json") as json_file:
#     json_data = json.load(json_file)
#     print(json_data)


# @dp.message_handler()
async def echo_send(message : types.Message):
    if message.text.lower() == 'привет':
        await message.reply('Приветствую, пернатый!')
    # elif message.reply_voice():
    #     await message.reply('А ты на ушко шепни!')
    
    elif message.text.lower() == "петя поздоровайся":
        await message.answer('Приветствую вас, други двуногие! Рад знакомству!')

    elif message.text.lower() == "петух":
        await message.reply('Осторожней при наклонах, милый')
        # await message.answer_animation('Gachi1.mp4') #надо разобраться с отсылкой анимации
        
    elif message.text.lower() == 'лох' and  message.from_user.id == 282235964:
        await message.reply('И это говорит человек, который срал в пакет')


    elif message.text.lower() == 'бля' or message.text.lower() == 'сука' \
        or message.text.lower() == 'пиздец':
        await message.reply('Раскудахтался ты что-то, тут же женщины и птицы!')
    # await bot.send_message(message.from_user.id, message.text)

    elif message.text.lower() == 'пятница!' or message.text.lower() == 'пятница':
        await message.answer('УРРРРРАААААААА! Петя хороший, Петя хочет выпить')

    elif message.text.lower() == 'доброе утро' or message.text.lower() == 'утра' or \
        message.text.lower() == 'утро' or message.text.lower() == 'доброе' :
        await message.reply('Ты в зеркало забыл посмотреть?')

    elif message.text.lower() == 'мрак':
        await message.reply('Тлен, боль, мука...')

    elif message.text.lower() == 'хватит пить':
        await message.answer('ВОТ ИМЕННО! *** пссссс... Там... это... Глянь в холодильник...')

    elif message.text.lower() == 'с праздником':
        await message.answer('В России два праздника - Новый год и Каждый день')

    elif message.text.lower() == 'влад!' or message.text.lower() == 'влад' or message.text.lower() == 'владос':
        await message.reply('Влада нет, он работает (нет, просто устал)')

    elif message.text.lower() == 'эл' or message.text.lower() == 'электроник':
        await message.reply('Зачем тебе человек, который заставляет меня говорить?')


def register_handlers_other(dp: Dispatcher) :
    dp.register_message_handler(echo_send)