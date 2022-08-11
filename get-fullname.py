
import requests

TOKEN = '5528595058:AAHoj8gqsXVAR91sWHa2CocMU8qydTTh_Oo'
URL   = 'https://api.telegram.org/bot'


def getMe():
    url = URL + TOKEN + '/getME'
    r = requests.get(url=url)
    if r.status_code == 200:
        print(r.json())



def getUpdates():
    url = URL + TOKEN + '/getUpdates'
    r = requests.get(url=url)
    if r.status_code == 200:
        updates = r.json()['result'][-1]
        fulname = f"{updates['message']['from']['first_name']} {updates['message']['from']['last_name']}"
        print(fulname)

getMe()
getUpdates()