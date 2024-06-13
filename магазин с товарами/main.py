from tovars import answer
from verification import bot
from call_back import call_back

if __name__=='__main__':
    print('Bot start working!')
    bot.polling(non_stop=True)