from telebot import *

bot = TeleBot(token="5923889055:AAHRNQqLZpEKvXUgVua0bO8Xr8xDpag1tWQ")

@bot.message_handler(commands=['start'])
def start(message):
    '''Ответ на команду /start'''
    markup = types.InlineKeyboardMarkup(row_width=4)
    markup.add(types.InlineKeyboardButton('Начать',callback_data='начать'))
    bot.send_message(message.chat.id,"Всем привет!\nЭто чат-бот с резюме моего создателя.\nПриятного пользования")
    bot.send_message(message.chat.id,"Для продолжения нажми на кнопку",reply_markup=markup)
@bot.message_handler(content_types=['text'])
def react(message):
    '''Обработка сообщений и ответ на них'''
    if message.text=='Начать':
        bot.delete_message(message.chat.id,message.message_id)
        bot.delete_message(message.chat.id,message.message_id)
        bot.send_message(message.chat.id,'чмо')
    else:
        bot.send_message(message.chat.id,'Что-то пошло не так,попробуй по другому')
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    try:
        if call.message=='начать':
            bot.send_message(call.message.chat.id,'Меня зовут Михаил, мне 18 лет и я полон сил устроиться имеено к Вам на работу!\n'
                                                  'У меня имеется множество проектов, включая данный, которые помогут предоставить информацию о том, на что я способен.\n'
                                                  'Из положительных качеств могу отметить участие и призерство в таких олимпиадах как:\n'
                                                  '-Росатом\n-Deadline(Тинькофф)\n-ВСОШ\n-RoboTeach(УГНТУ)\n'
                                                  'Именно там я и смог погрузиться в сферу айти, т.к. без нужных знаний приходилось выкручиваться и решать задачи.\n'
                                                  'Сейчас изучаю Java,JS,автотестирование на селениум.\n'
                                                  'Ссылка на мои проекты в гитхаб:')
    except Exception as e:
        print(e)


if __name__=='__main__':
    print('Start polling')
    bot.polling(none_stop=True)