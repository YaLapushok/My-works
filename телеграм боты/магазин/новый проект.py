import telebot
from telebot import types

token = '5826717307:AAFU1EZDSE46jfmCUIAF0kFIw4vxLk1yzBw'
bot = telebot.TeleBot(token)
print('Бот работает!')

'''Библиотека'''
photo1 = open('фото для проекта/banana-strawberry.jpg', 'rb')
photo2 = open("фото для проекта/grapes.jpg", 'rb')
p1 = 0
p2 = 0
txt = 'Ваш товар:\n'
b_s = 'Под банан-клубника: '
gr = 'Под виноград: '
product = ['Ничего']
sold = 500

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = 'Корзина'
    item2 = 'Каталог'
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Приветствую Вас в нашем магазине😇\n'
                                      'Мы продаем жижи,вейпы и т.д.\n'
                                      'Самое лучшее курево только у нас, переходите в каталог и выберите что-то для '
                                      'себя и своих друзей🤟', reply_markup=markup)

'''Каталог'''
@bot.message_handler(content_types=['text'])
def catalog(message):
    if message.text == 'Каталог':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = 'Поды'
        markup.add(item1)
        bot.send_message(message.chat.id, 'Что именно вас интересует?', reply_markup=markup)

    elif message.text == 'Поды':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = 'Банан-клубника'
        item2 = 'Виноград'
        markup.add(item1,item2)
        bot.send_message(message.chat.id, 'Выберите вкус:', reply_markup=markup)

        '''Описываем вкусы'''
    elif message.text == 'Банан-клубника':
        markup = types.InlineKeyboardMarkup(row_width=8)
        item = types.InlineKeyboardButton('Добавить в корзину', callback_data='корзина1')
        bot.send_photo(message.chat.id, photo1)
        markup.add(item)
        bot.send_message(message.chat.id, 'Это наш бананово-клубничный под, оч вкусный!'
                                          f'\nЦена {sold} руб', reply_markup=markup)

    elif message.text == 'Виноград':
        markup = types.InlineKeyboardMarkup(row_width=8)
        item = types.InlineKeyboardButton('Добавить в корзину', callback_data='корзина2')
        bot.send_photo(message.chat.id, photo2)
        markup.add(item)
        bot.send_message(message.chat.id, 'Виноградный под с ебейшим запахом!!!'
                                          f'\nЦена {sold} руб', reply_markup=markup)

    elif message.text == 'Корзина': #Тут описываю мусорку
        global txt
        if p1 == 0 and p2 == 0:
            bot.send_message(message.chat.id, f'Вы ничего не приобрели')
        elif p1 > 0 and p2 > 0:
            bot.send_message(message.chat.id, f'{txt}{b_s}{p1}\n{gr}{p2}'
                                              f'\nОбщая сумма = {(p1*sold)+(p2*sold)} ')
        elif p1 > 0:
            bot.send_message(message.chat.id, f'{txt}{b_s}{p1}'
                                              f'\nОбщая сумма = {(p1*sold)}')
        elif p2 > 0:
            bot.send_message(message.chat.id, f'{txt}{gr}{p2}'
                                              f'\nОбщая сумма = {(p2*sold)}')
    else:
        bot.send_message(message.chat.id, 'Напишите /start')
        answer = message.text
        author = message.from_user.username
        print(author+' - '+answer)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    try:
        if call.message:
            if call.data == 'корзина1':
                global p1
                p1 += 1
                bot.send_message(call.message.chat.id, f'Количество товара в корзине:{p1}')
            elif call.data == 'корзина2':
                global p2
                p2 += 1
                bot.send_message(call.message.chat.id, f'Количество товара в корзине:{p2}')


    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
