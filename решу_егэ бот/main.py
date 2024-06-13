from telebot import *

bot = TeleBot(token="5874711088:AAF0SMwNzCUdKVJy9HwVu2bxKKKmQlPf3kI")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Это бот, который поможет в обучении ЕГЭ по информатике\nЧтобы начать, напиши Готов")
@bot.message_handler(content_types=['text'])
def ready(message):
    if message.text=='Готов':
        bot.delete_message(message.chat.id,message.message_id)
        bot.edit_message(message.chat.id,'Ты написал Готов')
    else:
        bot.send_message(message.chat.id,'aaa')

if __name__=='__main__':
    bot.polling(none_stop=True)