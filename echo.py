
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

    print("sent message ......... -> ", text)


def getUpdates():
    r = requests.get(url=url_for_getUpdates)
    stc = r.status_code

    if stc == 200:
        result = r.json()['result']
        msg    = result[-1]['message']
        msg_id = msg['message_id']

        return stc, msg_id, msg
    
    return stc, None, None



while True:
    status_code0, msgs0, msg0 = getUpdates()
    print("status code 00 --->  ", status_code0)
    if status_code0 == 200:
        status_code1, msgs1, msg1 = getUpdates()
        print("status code 01 --->  ", status_code0)
        if status_code1 == 200:
            if msgs0 != msgs1:
                chat_id = msg1['from']['id']
                text    = msg1['text']
                sendMessage(chat_id, text)
