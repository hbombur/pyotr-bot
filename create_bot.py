from aiogram import Bot
from aiogram.dispatcher import Dispatcher

#объявляем токен
TOKEN = '5125100454:AAGKIHhck4vfhVXYL1XC7293Sh0xK_y-3Lc'

#объявляем бота и декоратор 
bot = Bot(TOKEN)
dp = Dispatcher(bot)