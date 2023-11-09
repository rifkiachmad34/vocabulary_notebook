import requests

api_key = '03e8c9aa-3e68-4995-938c-1cfea6fdd08e'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definition = res.json()
print(definition)