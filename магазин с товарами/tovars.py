from verification import bot, tovars_text, tovars_photo, tovars_name
from call_back import get_ret_tov, temp_k, ret_tov, send_keyboard
from telebot import types

k = 0
korz = []
counter = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Пиши Товары')

@bot.message_handler(content_types=['text'])
def answer(message):
    global k
    if message.text == 'Товары' or message.text =='товары':
        markup = types.InlineKeyboardMarkup(row_width=4)
        item1 = types.InlineKeyboardButton('<', callback_data='<')
        item2 = types.InlineKeyboardButton(f'{k}/{len(tovars_photo)}', callback_data='schet')
        item3 = types.InlineKeyboardButton('>', callback_data='>')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'Здесь ты можешь посмотреть товары нашего маркетплейса\nЧтобы начать перемещение, нажми на одну из стрелочек', reply_markup=markup)
    elif message.text == f'Добавить в корзину':
        ret_tov = get_ret_tov()
        korz.append(ret_tov)  # Добавляем товар в список корзины
        if ret_tov not in counter:
            counter[ret_tov] = 1
        else:
            counter[ret_tov] += 1
        bot.send_message(message.chat.id, f'Товар {ret_tov} добавлен в корзину. '
                                          f'Количество: {counter[ret_tov]}')
        # Удаляем кнопки после их нажатия
        bot.delete_message(message.chat.id, message.message_id)
    elif message.text == f'Убрать из корзины':
        ret_tov = get_ret_tov()
        if ret_tov in counter:
            counter[ret_tov] -= 1
            if counter[ret_tov] < 0:
                counter[ret_tov] = 0
            if counter[ret_tov]==0:
                korz.remove(ret_tov)
            bot.send_message(message.chat.id, f'Товар {ret_tov} удален из корзины. '
                                              f'Количество: {counter[ret_tov]}')
            # Удаляем кнопки после их нажатия
            bot.delete_message(message.chat.id, message.message_id)
        else:
            bot.send_message(message.chat.id, f'Товар {ret_tov} не найден в корзине.')
    elif message.text == 'Корзина':
        mes=''
        for i in korz:
            mes = ''.join(i)
        bot.send_message(message.chat.id,mes)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понял😢\nДля начала работы напиши /start')


