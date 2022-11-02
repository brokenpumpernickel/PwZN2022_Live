import json

with open('scripts/Lab004/chuck_films.json', 'r') as f:
    chuck = json.load(f)

print(chuck)