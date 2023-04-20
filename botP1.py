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
        pprint(updates["result"][0]['update_id'])
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