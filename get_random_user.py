import requests


token = '2057309601:AAFJaNwnVt3Wrz2dAP98VRxIwp3VDxhLalU'


def getUpdates():
    r = requests.get(url=f'https://api.telegram.org/bot{token}/getUpdates')
    if r.status_code == 200:
        results      = r.json()['result']
        last_message = results[-1]
        update_id    = last_message['update_id']
        msg = last_message['message']
        chat_id      = msg['from']['id']
        text         = msg.get('text', 'no')

        return update_id, chat_id, text
    
    return -1, None, None


def getRandomUser():
    r = requests.get(url='https://randomuser.me/api')
    user = r.json()['results'][0]
    first = user['name']['first']
    last = user['name']['last']
    
    return first + " " + last



def sendMessage(chat_id, text):
    if not text:
        text = getRandomUser()
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    r = requests.get(url=f'https://api.telegram.org/bot{token}/sendMessage', params=payload)



def main():
    last_update_id = getUpdates()[0]
    while True:
        curr_update_id, chat_id, text = getUpdates()
        if last_update_id != curr_update_id:
            if text == "/start":
                sendMessage(chat_id, False)
            else:
                sendMessage(chat_id, f"{text} is not telegram command.")
            last_update_id = curr_update_id

main()



