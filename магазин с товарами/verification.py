import telebot
'''Данные для авторизации бота'''
token = '5874711088:AAF0SMwNzCUdKVJy9HwVu2bxKKKmQlPf3kI'
bot = telebot.TeleBot(token)
'''База данных'''
apple_pod = 'фото/яблоко.jpg'
grape_pod = 'фото/виноградjpg.jpg'
tovars_photo = [apple_pod,grape_pod]
tovars_text = ['Яблочная одноразка блабла','Виноградный вкус, насыщенный блабла']
tovars_name = ['Яблочный под','Виноградный под']
korzina = []