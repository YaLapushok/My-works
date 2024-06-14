import telebot, requests
from telebot import types

token = '5826717307:AAFU1EZDSE46jfmCUIAF0kFIw4vxLk1yzBw'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(keyboard=True)
    markup.add(types.InlineKeyboardButton('Начать общение',callback_data='start_msg'))
    bot.send_message(message.chat.id, 'Привет, я буду общаться с тобой через гс.\n'
                                      '||Чтобы начать нажми кнопку ниже\n'
                                      '\\\/', reply_markup=markup)

@bot.message_handler(content_types=['text','voice'])
def get_audio(message):
    if message is message.voice:
        file_info = bot.get_file(message.voice.file_id)
        file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))
        bot.send_message(message.chat.id, 'Записал ботик')

        with open('voice.ogg', 'wb') as f:
            f.write(file.content)
    elif message is message.text:
        bot.send_message(message.chat.id, 'сасац')



if __name__ == '__main__':
    bot.polling(none_stop=True)