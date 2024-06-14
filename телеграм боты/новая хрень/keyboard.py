from telebot import types
from photos import pods
count = 0

'''Кнопки на старте'''
start_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = 'Смотреть товар'
item2 = 'Оплатить'
start_menu.add(item2,item1)

'''Кнопки товаров инлайновые'''
tovars = types.InlineKeyboardMarkup(row_width=1)
tovars.add(types.InlineKeyboardButton('🍓Вейпы🍓', callback_data = 'veip'))
tovars.add(types.InlineKeyboardButton('🍒Поды🍒', callback_data = 'pod'))
tovars.add(types.InlineKeyboardButton('🥝Жижи🥝', callback_data = 'jj'))

'''Стрелочки и товары для подов'''
strelki_pod = types.InlineKeyboardMarkup(row_width=3)
strelki_pod.add((types.InlineKeyboardButton('<<', callback_data = 'str-l-pod')),(types.InlineKeyboardButton(str(count)+'/'+str(len(pods)),callback_data='countt')),(types.InlineKeyboardButton('>>', callback_data = 'str-r-pod')))

