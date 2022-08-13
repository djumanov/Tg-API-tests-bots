import requests


token = '5528595058:AAHoj8gqsXVAR91sWHa2CocMU8qydTTh_Oo'


def getUpdates():
    r = requests.get(url=f'https://api.telegram.org/bot{token}/getUpdates')
    if r.status_code == 200:
        results = r.json()['result']
        last_message = results[-1]
        print(last_message)
        return last_message

getUpdates()
