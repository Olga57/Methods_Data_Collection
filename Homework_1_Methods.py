### Задание 1
### Посмотреть документацию к API GitHub,
### разобраться как вывести список репозиториев для конкретного пользоват
import requests
import json
url = 'https://api.github.com'
username = 'Olga57'
token = ''
r = requests.get(f'https://api.github.com/users/{username}/repos')
print("Done")
with open('data.json', 'w') as f:
    json.dump(r.json(), f)

for i in r.json():
    print(i['name'])