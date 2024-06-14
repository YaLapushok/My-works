import telebot
from config import TOKEN, YKASSA_TOKEN
from keyboard import start_menu, tovars, strelki_pod
from photos import pods

bot = telebot.TeleBot(TOKEN)
print('Бот начал работу!')


@bot.message_handler(commands=['start','help'])
def start(message):
    bot.send_message(message.chat.id, 'Привет юзер, я тут учусь собирать с тебя деньги', reply_markup=start_menu)


@bot.message_handler(content_types=['text'])
def check(message):
    if message.text == 'Смотреть товар':
        bot.delete_message(message.chat.id, message_id=message.message_id)
        bot.send_message(message.chat.id, 'В этом месяце у нас новая коллекция'
                                          '\nВыберите категорию товара',reply_markup=tovars)
    elif message.text == 'Оплатить':
        pass
    else:
        bot.send_message(message.chat.id, 'Чёто неправильно пишешь\nНапиши /start')


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    try:
        count = 0
        if count > len(pods):
            count = len(pods)
        if count < 0:
            count = 0
        if call.message:
            if call.data == 'pod':
                bot.send_message(call.message.chat.id, 'Ниже предоставлены наши поды', reply_markup=strelki_pod)
            elif call.data == 'str-l-pod':
                bot.send_photo(call.message.chat.id, pods[count])
                bot.send_message(call.message.chat.id, 'Это наш бананово-клубничный под, оч вкусный')
                count -= 1
            bot.send_message(call.message.chat.id, 'Ниже предоставлены наши поды', reply_markup=strelki_pod)
            if call.data == 'str-r-pod':
                bot.send_photo(call.message.chat.id, pods[count])
                bot.send_message(call.message.chat.id, 'Это под с вкусом виноград-лед, он кислый')
                count += 1
                bot.send_message(call.message.chat.id, 'Ниже предоставлены наши поды', reply_markup=strelki_pod)
            elif call.data == 'countt':
                pass

    except Exception as e:
        print(e)


if __name__ == '__main__':
    bot.polling(none_stop=True)