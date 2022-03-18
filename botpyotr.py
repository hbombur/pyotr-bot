# , Dispatcher, types

from aiogram.utils import executor
from create_bot import dp


#функция для старта бота, действия для начальныхз взаимодействий с ботом
async def on_startup(_):
    print('Петух проснулся') 

#обращаемся к папке с файлами функций бота и импортируем ее
from handlers import client, other, admin

#вызываем каждую из функций
client.register_handlers_client(dp)
# admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

#активация бота
executor.start_polling(dp, skip_updates = True, on_startup=on_startup)