from aiogram import Bot, Dispatcher, types
from config import TOKEN, YKASSA_TOKEN
from keyboard import sub_verefication_menu, menu_keyboard

bot = Bot(TOKEN)
dp = Dispatcher(bot)

def sub_verefication(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False



@dp.message.handlers(commands = ['start'])
def start(message: types.Message):
    if sub_verefication(await bot.get_chat_member(chat_id='@mamylov_bot', user_id=message.from_user.id)):
        await message.answer('Выберите действие из меню:', reply_markup=menu_keyboard)
    else:
        await message.answer('Сначало подпишись на канал!', reply_markup=sub_verefication_menu)

@dp.callback_query_handler(text = 'sub_check')
async def sub_check(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message.id)
    if sub_verefication(await bot.get_chat_member(chat_id='@mamylov_bot', user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, 'Выберите действие из меню:', reply_markup=menu_keyboard)
    else:
        await bot.send_message(message.from_user.id, 'Сначало подпишись на канал!', reply_markup=sub_verefication_menu)


if __name__ == '__main__':
    dp.start_polling(skip_updates = True)






