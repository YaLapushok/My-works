import telebot
from telebot import types

'''Библиотека с данными'''
token = '5826717307:AAFU1EZDSE46jfmCUIAF0kFIw4vxLk1yzBw'
bot = telebot.TeleBot(token)
print('Бот начал работу!')
i = 0
banana_strawberry = 'Банан клубника'

@bot.message_handler(commands=['start'])
def start(message):
    '''Команда /start'''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = 'Вейпы'
    item2 = 'Корзина'
    markup.add(item1,item2)
    bot.send_message(message.chat.id, 'Приветствую в нашем вейп онлайн магазине'
                                      '\nДелайте выбор:', reply_markup=markup)
class vape():
    def __init__(self, taste, count, price):
        '''Инициализирую '''
        self.taste = taste
        self.count = count
        self.price = price

    def bin(self, message):
        '''Здесь будут храниться данные для корзины юзера'''
        if i == 0:
            bot.send_message(message.chat.id, 'Вы ничего не приобрели')
        if i > 0:
            bot.send_message(message.chat.id, f'Ваш товар:'
                                              f'\n')


@bot.message_handler(content_types=['text'])
def answer(message):
    global banana
    if message.text == 'Вейпы':
        '''Выбор вкуса вейпа'''
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = 'Банан-клубника'
        markup.add(item1)
        bot.send_message(message.chat.id, 'Выберите вкус продукта:', reply_markup=markup)

    elif message.text == 'Банан-клубника':
        '''Фото и описание вейпа: банан-клубника '''
        banana = message.text
        with open('фото для проекта/banana-strawberry.jpg', 'rb') as banana_strawberry:
            '''Текст после отправки фото'''
            markup = types.InlineKeyboardMarkup(row_width=4)
            item1 = types.InlineKeyboardButton('Добавить в корзину', callback_data='bin1')
            markup.add(item1)
            bot.send_photo(message.chat.id, banana_strawberry)
            bot.send_message(message.chat.id, 'Это наш банановый вейп'
                                              '\nЦена:500руб', reply_markup=markup)

    elif message.text == 'Корзина':
        global i2
        '''Корзина, где передаётся информация в класс'''
        i2 = i
        i2 = i2*500
        answer_banana_strawberry = vape(banana, str(i), str(i2))
        answer_banana_strawberry.bin(message)
    else:
        '''Ответ на неизвестное сообщение + имя автора с его сообщением'''
        bot.send_message(message.chat.id, 'Введите /start')
        answer = message.text
        author = message.from_user.username
        print(f'{author} написал сообщение: {answer}')

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    '''Возврат ответа при нажатии кнопки'''
    try:
        if call.message:
            if call.data == 'bin1':
                global i
                i = i+1
                bot.send_message(call.message.chat.id, f'Товар был добавлен {i} раз')
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)