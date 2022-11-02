import requests
from bs4 import BeautifulSoup
import json

req = requests.get('https://www.imdb.com/name/nm0001569/')

#print(req.status_code)
#print(req.text)
#print(req.request.headers)

soup = BeautifulSoup(req.text, 'html.parser')

films = soup.find('div', {'class': 'filmo-category-section'})

chuck_films = []

for film in films.find_all('div', {'class': 'filmo-row'}):
    span = film.find('span')
    title = film.find('a')
    #print(span.text.strip(), title.text.strip(), title['href'])
    chuck_films.append((span.text.strip(), title.text.strip(), title['href']))

print(chuck_films)

with open('scripts/Lab004/chuck_films.json', 'w') as f:
    json.dump(chuck_films, f)