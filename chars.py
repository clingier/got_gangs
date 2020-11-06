import requests
from bs4 import BeautifulSoup

r = requests.get('https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_characters')
s = BeautifulSoup(r.text, 'html.parser')

tables = s.find_all('table', {'class': 'wikitable'})

def get_characters_from_tables(table):
    rows = table.find_all('tr')[2:]
    characters = set()
    for row in rows:
        character = row.find_all('td')[1].text
        characters.add(character)
    return characters

g_characters = set()

for t in tables:
    g_characters |= get_characters_from_tables(t)