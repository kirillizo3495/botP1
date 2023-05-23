import requests
import time
from pprint import pprint

API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '6064408255:AAGBbsdGXRGz70OfVSxpp7mlVOQHxxogsVU'
TEXT: str = 'а я просто ничего не умею... пока что'
MAX_COUNTER: int = 100             #это количество итераций цикла, в котором мы получаем апдейты от сервера.

offset: int = -1                   # чтобы получать апдейты
counter: int = 0                   # когда эта переменная будет равна MAX_COUNTER
chat_id: int                       #


while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    #https://api.telegram.org/bot6064408255:AAGBbsdGXRGz70OfVSxpp7mlVOQHxxogsVU/getUpdates?offset=436827543
    if updates['result']:
        pprint(updates["result"])
        pprint(updates["result"][0]["username"])
        pprint(updates["result"][1]['update_id'])


        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

            pprint(updates["result"])
            pprint(updates["result"][0]['update_id'])
            pprint(updates["result"][1]['update_id'])



    time.sleep(1)
    counter += 1


    @dp.message(Text(text=['Да', 'Давай', 'Сыграем', 'Игра',
                           'Играть', 'Хочу играть'], ignore_case=True))
    async def process_positive_answer(message: Message):
        if not users[message.from_user.id]['in_game']:
            await message.answer('Ура!\n\nЯ загадал число от 1 до 100, '
                                 'попробуй угадать!')
            users[message.from_user.id]['in_game'] = True

        else:
            await message.answer('Пока мы играем в игру я могу '
                                 'реагировать только на числа от 1 до 100 '
                                 'и команды /cancel и /stat')


    # Этот хэндлер будет срабатывать на отказ пользователя сыграть в игру
    @dp.message(Text(text=['Нет', 'Не', 'Не хочу', 'Не буду'], ignore_case=True))
    async def process_negative_answer(message: Message):
        if not users[message.from_user.id]['in_game']:
            await message.answer('Жаль :(\n\nЕсли захотите поиграть - просто '
                                 'напишите об этом')
        else:
            await message.answer('Мы же сейчас с вами играем. Присылайте, '
                                 'пожалуйста, числа от 1 до 100')


    # Этот хэндлер будет срабатывать на отправку пользователем чисел от 1 до 100
    @dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
    async def process_numbers_answer(message: Message):
        if users[message.from_user.id]['in_game']:
            if int(message.text) == users[message.from_user.id]['secret_number']:
                await message.answer('Ура!!! Вы угадали число!\n\n'
                                     'Может, сыграем еще?')
                users[message.from_user.id]['in_game'] = False
                users[message.from_user.id]['total_games'] += 1
                users[message.from_user.id]['wins'] += 1
            elif int(message.text) > users[message.from_user.id]['secret_number']:
                await message.answer('Мое число меньше')
                users[message.from_user.id]['attempts'] -= 1
            elif int(message.text) < users[message.from_user.id]['secret_number']:
                await message.answer('Мое число больше')
                users[message.from_user.id]['attempts'] -= 1

            if users[message.from_user.id]['attempts'] == 0:
                await message.answer(
                    f'К сожалению, у вас больше не осталось '
                    f'попыток. Вы проиграли :(\n\nМое число '
                    f'было {users[message.from_user.id]["secret_number"]}'
                    f'\n\nДавайте сыграем еще?')
                users[message.from_user.id]['in_game'] = False
                users[message.from_user.id]['total_games'] += 1
        else:
            await message.answer('Мы еще не играем. Хотите сыграть?')


    # Этот хэндлер будет срабатывать на остальные текстовые сообщения
    @dp.message()
    async def process_other_text_answers(message: Message):
        if users[message.from_user.id]['in_game']:
            await message.answer('Мы же сейчас с вами играем. '
                                 'Присылайте, пожалуйста, числа от 1 до 100')
        else:
            await message.answer('Я довольно ограниченный бот, давайте '
                                 'просто сыграем в игру?')
