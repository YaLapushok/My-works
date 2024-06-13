from verification import bot, tovars_name, tovars_photo, tovars_text
from telebot import types

temp_k = 0
ret_tov = ''

@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    global temp_k, ret_tov  # Объявляем переменные как глобальные
    try:
        if call.message:
            if call.data == '<':
                '''Выполнение команды при нажатии кнопки <'''
                temp_k -= 1
                if temp_k < 0:
                    temp_k = len(tovars_photo) - 1

            if call.data == '>':
                '''Выполнение команды при нажатии кнопки >'''
                temp_k += 1
                if temp_k >= len(tovars_photo):
                    temp_k = 0

            if call.data == 'schet':
                '''Выполнение команды при нажатии кнопки schet'''
                temp_k = 0

            send_keyboard(call.message.chat.id, temp_k)
            ret_tov = tovars_name[temp_k]
            # Удаляем кнопки после их нажатия
            bot.delete_message(call.message.chat.id, call.message.message_id)

    except Exception as e:
        print(e)

def get_ret_tov():
    return ret_tov

def send_keyboard(chat_id, k):
    # Создаем InlineMarkup
    inline_markup = types.InlineKeyboardMarkup(row_width=3)
    inline_markup.add(types.InlineKeyboardButton('<', callback_data='<'),
                      types.InlineKeyboardButton(f'{k + 1}/{len(tovars_photo)}', callback_data='schet'),
                      types.InlineKeyboardButton('>', callback_data='>'))
    reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    reply_markup.add(f'Добавить в корзину', f'Убрать из корзины')

    bot.send_photo(chat_id, open(tovars_photo[k], 'rb'))
    bot.send_message(chat_id, tovars_text[k], reply_markup=reply_markup)
    bot.send_message(chat_id, 'Я стрелочка', reply_markup=inline_markup)

