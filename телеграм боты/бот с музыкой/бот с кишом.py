import telebot
from telebot import types

token = '5874711088:AAF0SMwNzCUdKVJy9HwVu2bxKKKmQlPf3kI'
bot = telebot.TeleBot(token)
print('Бот начал работу!')
'''Библиотека'''
#kukla = open('музыка\Korol_i_SHut_-_Kukla_kolduna_(musmore.com).mp3', 'rb')


@bot.message_handler(commands=['start'])
def start(message):
    '''Команда /start'''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = 'Акустический'
    #item2 = 'Камнем по голове'
    #item3 = 'Как в старой сказке'
    markup.add(item1)
    bot.send_message(message.chat.id, 'Привет, я бот который скидывает музыку КИШа\n'
                                      '*Выбирай альбом*:', reply_markup=markup, parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def acustik(message):
    '''отправка акустического альбом'''
    if message.text == 'Акустический':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = 'Кукла колдуна'
        markup.add(item1)
        bot.send_message(message.chat.id, 'Выбирай песню:', reply_markup=markup)
    elif message.text == 'Кукла колдуна':
        with open('музыка\Korol_i_SHut_-_Kukla_kolduna_(musmore.com).mp3', 'rb') as kukla:
            bot.send_voice(message.chat.id, kukla)


    else:
        bot.send_message(message.chat.id, 'Напиши /start')


bot.polling(none_stop=True)