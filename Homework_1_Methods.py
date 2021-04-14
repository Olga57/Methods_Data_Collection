### Задание 1
### Посмотреть документацию к API GitHub,
### разобраться как вывести список репозиториев для конкретного пользоват
import requests
import json
url = 'https://api.github.com'
username = 'Olga57'
token = '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'
r = requests.get(f'https://api.github.com/users/{username}/repos')
print("Done")
with open('data.json', 'w') as f:
    json.dump(r.json(), f)

for i in r.json():
    print(i['name'])