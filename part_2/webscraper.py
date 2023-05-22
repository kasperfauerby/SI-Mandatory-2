import requests
import sqlite3
from bs4 import BeautifulSoup

def create_database():
    conn = sqlite3.connect('champions.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS champions (name TEXT, title TEXT, difficulty TEXT)')
    conn.commit()
    conn.close()

def insert_champion(conn, name, title, difficulty):
    c = conn.cursor()
    c.execute('INSERT INTO champions VALUES (?, ?, ?)', (name, title, difficulty))
    conn.commit()

def scrape_champions(url):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        champions = soup.find_all('div', {'class': 'm-12dr3gi'})
        conn = sqlite3.connect('champions.db')
        create_database()
        for champion in champions:
            name = champion.find('div', {'class': 'm-123baga'}).text.strip()
            title = champion.find('div', {'class': 'm-am8tfa'}).text.strip()
            difficulty = champion.find('div', {'class': 'm-s5xdrg'}).text.strip()
            insert_champion(conn, name, title, difficulty)
            print(name + ' - ' + title + ' - ' + difficulty)
        conn.close()

if __name__ == '__main__':
    scrape_champions('https://app.mobalytics.gg/lol/champions')