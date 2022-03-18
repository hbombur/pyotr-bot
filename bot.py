import telebot
from time import sleep
import random
import configure

bot = telebot.TeleBot(configure.config['token'])


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'привет')
#текст
@bot.message_handler(сontent_types=['text'])
def text(message):
    if message.text.lower() == 'привет' :
        bot.send_message(message.chat.id, 'Приветствую, пернатый!')

bot.polling(none_stop = True, interval = 0)
