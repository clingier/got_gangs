import requests
from bs4 import BeautifulSoup

r = requests.get('https://gameofthrones.fandom.com/wiki/Game_of_Thrones_Wiki')
s = BeautifulSoup(r.text, 'html.parser')

tables = s.find_all('a')

def get_characters_from_tables(table):
    rows = table.find_all('tr')[2:]
    characters = set()
    for row in rows:
        character = row.find_all('td')[1].text
        characters.add(character)
    return characters


