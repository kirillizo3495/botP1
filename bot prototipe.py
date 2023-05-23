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

rock = ['Metallica-Master Of Puppets https://www.youtube.com/watch?v=E0ozmU9cJDg',
        'Metallica-Sad But True https://www.youtube.com/watch?v=TpohVYomw2o',
        'Metallica-Fade To Black https://www.youtube.com/watch?v=9HZ_tx8aWuA',
        'Nirvana-Smells Like Teen Spirit https://www.youtube.com/watch?v=hTWKbfoikeg',
        'Nirvana-Come As You Are https://www.youtube.com/watch?v=vabnZ9-ex7o',
        'КИНО-Хочу перемен https://www.youtube.com/watch?v=-vdfEZwPd3M',
        'КИНО-Группа крови https://www.youtube.com/watch?v=xtxjm7ciwmc',
        'КИНО-Звезда по имени Солнце https://www.youtube.com/watch?v=Z4jQ4hZfk00',
        'КИНО-Пачка сигарет https://www.youtube.com/watch?v=Zj88LoDlSxQ',
        'КИНО-Кончится лето https://www.youtube.com/watch?v=iOvYGQtFBNM',
        'КИНО-Стук https://www.youtube.com/watch?v=0Cih47XDcNw',
        'КИНО-Последний герой https://www.youtube.com/watch?v=ufNgB0POzzY',
        'Би-2-Полковнику никто не пишет https://www.youtube.com/watch?v=Yzl_F_OxpQo',
        'Nautilus Pompilius-Крылья https://www.youtube.com/watch?v=4owHHfZBsyI',
        'Nautilus Pompilius-Зверь https://www.youtube.com/watch?v=Ez3RGAPhx84',
        'Nautilus Pompilius-Матерь богов https://www.youtube.com/watch?v=GbX-UqR3D6A',
        'Агата Кристи-Как на войне https://www.youtube.com/watch?v=1fm1XCJAY0s',]

pop_music= ['Руки Вверх!-18 мне уже https://www.youtube.com/watch?v=N6UfSfNcnqw',
            'Руки Вверх!-Выпускной https://www.youtube.com/watch?v=aFC2idsSXnk',
            'Руки Вверх!-Когда мы были молодыми https://www.youtube.com/watch?v=86O8yX3ogxE',
            'Руки Вверх!-Студент https://www.youtube.com/watch?v=gRW89Oqk0QI',
            'Руки Вверх!-Ай-яй-яй https://www.youtube.com/watch?v=11ymi0FmBUw',
            'Иванушки International-Тополиный пух https://www.youtube.com/watch?v=UUryvYF8tUs',
            'Градусы-Научиться бы не париться https://www.youtube.com/watch?v=5oD_SsE-iXM',
            'Градусы-Хочется https://www.youtube.com/watch?v=Puy6whV8nc0',
            'Ласковый май-Белые розы https://www.youtube.com/watch?v=bK_HiQka7ck',
            'Ласковый май-Седая ночь https://www.youtube.com/watch?v=_VJYsPRk4fg',
            'Ласковый май-Детство https://www.youtube.com/watch?v=G9z3j7Jdd0M',]

classic=['Бах-Nocturne in E Flat Major Op. 9, No. 2 https://www.youtube.com/watch?v=p29JUpsOSTE',
         'Бах-Sonata in C Major K.330: I. Allegro https://www.youtube.com/watch?v=3UQs0r56Wwo',
         'Бах-Sonata Op. 13, No. 8 in C Minor https://www.youtube.com/watch?v=91MTUXla-lE',
         'Бах-Sonatina in C Major Op. 36, Spiritoso https://www.youtube.com/watch?v=8vR9vvjR2_k']

punk_rock =['Король и Шут-Театральный демон https://www.youtube.com/watch?v=j0i_E3Btuo0',
            'Король и Шут-Кукла колдуна https://www.youtube.com/watch?v=Nj6aM9ljdQU',
            'Король и Шут-Лесник https://www.youtube.com/watch?v=i7R6_7e10QM',
            'Король и Шут-Дурак и молния https://www.youtube.com/watch?v=svCPBhiZD8g',
            'Сектор газа-Туман https://www.youtube.com/watch?v=p2ZbgHYONHk',
            'КняZz-Адель https://www.youtube.com/watch?v=-Atmfn2mASc',
            'КняZz-Человек-загадка https://www.youtube.com/watch?v=JDfsZTA1yHU',
            'КняZz-Брат https://www.youtube.com/watch?v=ofsp-1s2k9M',
            'КняZz-Дом манекенов https://www.youtube.com/watch?v=0Dycarg0Qh0',
            'КняZz-Пассажир https://www.youtube.com/watch?v=Rn7Oyxa1bEM',
            'КняZz-Банник https://www.youtube.com/watch?v=Etyy-Eox7pU',
            'КняZz-Видел Вия – вот те крест! https://www.youtube.com/watch?v=Ym6Qm9lvMyw',
            'КняZz-Романс https://www.youtube.com/watch?v=dzNQ0xyqrGU',
            'Король и Шут-Мёртвый Анархист https://www.youtube.com/watch?v=dDqqq8IMUvQ',
            'Король и Шут-Танец злобного гения https://www.youtube.com/watch?v=1LJ_g2bPQDA',
            'Король и Шут-Воспоминания о былой любви https://www.youtube.com/watch?v=3QjZoV87yCM']


# Создаем объекты бота и диспетчера
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()

# Создаем объекты кнопок
button_1: KeyboardButton = KeyboardButton(text='Грустно😔')
button_2: KeyboardButton = KeyboardButton(text='Весело😆')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2]],
                                    resize_keyboard=True)

# Создаем кнопки
button_1: KeyboardButton = KeyboardButton(text='Рок🎸')
button_2: KeyboardButton = KeyboardButton(text='Панк рок🎸')
button_3: KeyboardButton = KeyboardButton(text='Поп-музыка🎹')
button_4: KeyboardButton = KeyboardButton(text='Классическая🎻')


game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2],
                                              [button_3, button_4]],
                                    resize_keyboard=True)
# Словарь, в котором будут храниться данные пользователя

button_1: KeyboardButton = KeyboardButton(text='Давай✅')
button_2: KeyboardButton = KeyboardButton(text='Нет, не хочу!❌')

yes_no: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1,button_2]],
                                    resize_keyboard=True)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nкак настроение?,',
                         reply_markup=keyboard)
    # Если пользователь только запустил бота и его нет в словаре '
    # 'users - добавляем его в словарь


# Этот хэндлер срабатывает на согласие пользователя играть в игру
@dp.message(Text(text="Грустно😔"))
async def process_yes_answer(message: Message):
    await message.answer('Ясно, этот бот поможет найти подходящую песню. Кстати, а какой тип музыки тебе нравится?', reply_markup=game_kb)

@dp.message(Text(text="Весело😆"))
async def process_yes_answer(message: Message):
    await message.answer('Хорошо, этот бот поможет найти подходящую песню. Кстати, а какой тип музыки тебе нравится?', reply_markup=game_kb)

@dp.message(Text(text="Рок🎸"))
async def process_yes_answer(message: Message):
    await message.answer(random.choice(rock))
    await message.answer("Советую послушать,может еще что-то хочешь послушать?", reply_markup=yes_no)
@dp.message(Text(text="Панк рок🎸"))
async def process_yes_answer(message: Message):
    await message.answer(random.choice(punk_rock))
    await message.answer("Советую послушать,может еще что-то хочешь послушать?", reply_markup=yes_no)


@dp.message(Text(text="Поп-музыка🎹"))
async def process_yes_answer(message: Message):
    await message.answer(random.choice(pop_music))
    await message.answer('Советую послушать,может еще что-то хочешь послушать?', reply_markup=yes_no)
@dp.message(Text(text="Классическая🎻"))
async def process_yes_answer(message: Message):
    await message.answer(random.choice(classic))
    await message.answer("Советую послушать,может еще что-то хочешь послушать?", reply_markup=yes_no)
# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Я посоветую тебе музыку на твой вкус')

@dp.message(Text(text="Давай✅"))
async def process_yes_answer(message: Message):
    await message.answer("Какой тип музыки хочешь послушать?", reply_markup=game_kb)

@dp.message(Text(text="Нет, не хочу!❌"))
async def process_yes_answer(message: Message):
    await message.answer("Ладно, как захочешь напиши /start", reply_markup=ReplyKeyboardRemove())





# Этот хэндлер будет срабатывать на согласие пользователя сыграть в игру


if __name__ == '__main__':
    dp.run_polling(bot)
