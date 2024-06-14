from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(KeyboardButton('Купить одноразку'))

sub_verefication_menu = InlineKeyboardMarkup(row_width = 1)
sub_verefication_menu.insert(InlineKeyboardButton(text='Подписаться на канал!', url='https://t.me/mamylov_bot'))
sub_verefication_menu.insert(InlineKeyboardButton(text='Уже подписан!', callback_data='sub_check'))
