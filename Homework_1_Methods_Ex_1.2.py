### Изучить список открытых API. Найти среди них любое,
# требующее авторизацию (любого типа). Выполнить запросы к нему,
# пройдя авторизацию. Ответ сервера записать в файл.
import requests
import json


access_token = ''
base_url = f'https://api.vk.com/method/account.getInfo'
params = {'v': '5.52',
          'access_token': access_token}
response = requests.get(base_url, params = params)
with open('data1.json','w') as f:
    json.dump(response.json(), f)
