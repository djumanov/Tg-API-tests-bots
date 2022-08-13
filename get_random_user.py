import requests


token = '2057309601:AAFJaNwnVt3Wrz2dAP98VRxIwp3VDxhLalU'


def getUpdates():
    r = requests.get(url=f'https://api.telegram.org/bot{token}/getUpdates')
    if r.status_code == 200:
        results      = r.json()['result']
        last_message = results[-1]
        update_id    = last_message['update_id']
        msg = last_message['message']
        print(msg)
        chat_id      = msg['from']['id']
        text         = msg.get('text', 'no')

        return update_id, chat_id, text
    
    return -1, None, None

print(getUpdates())



