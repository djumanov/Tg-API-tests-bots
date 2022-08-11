
import requests

TOKEN = '5528595058:AAHoj8gqsXVAR91sWHa2CocMU8qydTTh_Oo'
URL = 'https://api.telegram.org/bot'

url_for_getUpdates = f'{URL}{TOKEN}/getUpdates'
url_for_sendMessage = f'{URL}{TOKEN}/sendMessage'


def sendMessage(chat_id, text):
    msg = {
        'chat_id': chat_id,
        'text': text
    }
    r = requests.get(url=url_for_sendMessage, params=msg)


while True:
    
    r0 = requests.get(url=url_for_getUpdates)
    if r0.status_code == 200:
        first_msgs = len(r0.json()['result'])
        
        r1 = requests.get(url=url_for_getUpdates)
        if r1.status_code == 200:
            last_msgs = len(r1.json()['result'])
            print("ok 1")
            if first_msgs != last_msgs:
                msg     = r1.json()['result'][-1]['message']
                chat_id = msg['from']['id']
                text    = msg['text']
                print("ok 2")
                sendMessage(chat_id, text)
                print(" sent ")


            

        
