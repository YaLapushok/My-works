import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext
from verefication import tg_token
from big_parser import parser

bot = Bot(token=tg_token,parse_mode='html')
dp = Dispatcher()
class Group(StatesGroup):
    name = State()
    teg = State()


@dp.message(Command('start'))
async def start(message:Message):
    await message.answer('Данный бот парсит данные с авито на тему \'персональный компьюнтер\'\n'
                         'Напиши /go чтобы начать получать данные\n')

@dp.message(Command('go'))
async def go(message:Message, state:FSMContext):
    await state.set_state(Group.name)
    await message.answer(f'Прежде чем начать поиск, напишите что будем искать:\n'
                         f'(Наример: плюшевый мишка)')


@dp.message(Group.name)
async def name_handler(message:Message, state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Group.teg)
    await message.answer('Теперь давайте напишем ключевое слово, которое должно быть в объявлении:\n'
                         '(Например: розовый)')

@dp.message(Group.teg)
async def teg_handler(message:Message, state:FSMContext):
    await state.update_data(teg=message.text)
    data = await state.get_data()
    await message.answer('Бот начал работу')
    try:
        await message.answer('\'\'\'\n'+parser(str(data['name']),str(data['teg']))[0]+'\n\'\'\'\n'+parser(str(data['name']),str(data['teg']))[1])
    except:
        await message.answer("Что-то пошло не так")
    await state.clear()


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
if __name__=='__main__':
    asyncio.run(main())