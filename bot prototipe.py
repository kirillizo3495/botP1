import random

from aiogram import Router
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                         ReplyKeyboardRemove)
from aiogram import Router
router: Router = Router()
# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN: str = '6064408255:AAGBbsdGXRGz70OfVSxpp7mlVOQHxxogsVU'

rock = ['Metallica-Master Of Puppets', 'Metallica-Sad But True', 'Metallica-Fade To Black',
        'Nirvana-Smells Like Teen Spirit', 'Nirvana-Come As You Are', 'Nirvana-Heart-Shaped Box',
        'КИНО-Хочу перемен', 'КИНО-Группа крови', 'КИНО-Звезда по имени Солнце', 'КИНО-Пачка сигарет',
        'КИНО-Кончится лето', 'КИНО-Стук', 'КИНО-Последний герой', 'Би-2-Полковнику никто не пишет',
        'Nautilus Pompilius-Крылья', 'Nautilus Pompilius-Зверь', 'Nautilus Pompilius-Матерь богов',
        'Агата Кристи-Как на войне',]

pop_music= ['Руки Вверх!-18 мне уже', 'Руки Вверх!-Выпускной', 'Руки Вверх!-Когда мы были молодыми',
            'Руки Вверх!-Студент', 'Руки Вверх!-Ай-яй-яй', 'Иванушки International-Тополиный пух',
            'Иванушки International-Снегири', 'Градусы-Научиться бы не париться', 'Градусы-Хочется',
            'Ласковый май-Белые розы', 'Ласковый май-Седая ночь', 'Ласковый май-Детство',]

classic=['Бах-Nocturne in E Flat Major Op. 9, No. 2', 'Бах-Sonata in C Major K.330: I. Allegro',
         'Бах-Sonata Op. 13, No. 8 in C Minor', 'Бах-Sonatina in C Major Op. 36, Spiritoso']

punk_rock =['Король и Шут-Театральный демон вот ссылка: https://www.youtube.com/watch?v=j0i_E3Btuo0']


# Создаем объекты бота и диспетчера
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()

# Создаем объекты кнопок
button_1: KeyboardButton = KeyboardButton(text='Грустное')
button_2: KeyboardButton = KeyboardButton(text='Веселое')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2]])

# Создаем кнопки игровой клавиатуры
button_1: KeyboardButton = KeyboardButton(text='Рок')
button_2: KeyboardButton = KeyboardButton(text='Панк рок')
button_3: KeyboardButton = KeyboardButton(text='Поп-музыка')
button_4: KeyboardButton = KeyboardButton(text='Классическая')
# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков
game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1],
                                              [button_2],
                                              [button_3],
                                              [button_4]],
                                    resize_keyboard=True)
# Словарь, в котором будут храниться данные пользователя





# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nкакая тебе музыка нравится,',
                         reply_markup=keyboard)
    # Если пользователь только запустил бота и его нет в словаре '
    # 'users - добавляем его в словарь


# Этот хэндлер срабатывает на согласие пользователя играть в игру
@dp.message(Text(text="Грустное"))
async def process_yes_answer(message: Message):
    await message.answer('Ясно, а какой тип музыки тебе нравится?', reply_markup=game_kb)

@dp.message(Text(text="Веселое"))
async def process_yes_answer(message: Message):
    await message.answer('Хорошо, а какой тип музыки тебе нравится?', reply_markup=game_kb)

@dp.message(Text(text="Рок"))
async def process_yes_answer(message: Message):
    await message.answer("Советую послушать")
    await message.answer(random.choice(rock))
@dp.message(Text(text="Панк рок"))
async def process_yes_answer(message: Message):
    await message.answer("Советую послушать")
    await message.answer(random.choice(punk_rock))

@dp.message(Text(text="Поп-музыка"))
async def process_yes_answer(message: Message):
    await message.answer('Советую послушать')
    await message.answer(random.choice(pop_music))
@dp.message(Text(text="Классическая"))
async def process_yes_answer(message: Message):
    await message.answer("Советую послушать")
    await message.answer('Советую тебе послушать')
# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                         f'а вам нужно его угадать\nУ вас есть  '
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавай сыграем?')


# Этот хэндлер будет срабатывать на команду "/stat"
@dp.message(Command(commands=['stat']))
async def process_stat_command(message: Message):
    await message.answer(
                    f'Всего игр сыграно: '
                    f'{users[message.from_user.id]["total_games"]}\n'
                    f'Игр выиграно: {users[message.from_user.id]["wins"]}')


# Этот хэндлер будет срабатывать на команду "/cancel"
@dp.message(Command(commands=['cancel']))
async def process_cancel_command(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.answer('Вы вышли из игры. Если захотите сыграть '
                             'снова - напишите об этом')
        users[message.from_user.id]['in_game'] = False
    else:
        await message.answer('А мы итак с вами не играем. '
                             'Может, сыграем разок?')


# Этот хэндлер будет срабатывать на согласие пользователя сыграть в игру


if __name__ == '__main__':
    dp.run_polling(bot)
