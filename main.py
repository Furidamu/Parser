import requests
from bs4 import BeautifulSoup

def find_key(key, list_of_cryptos):
    for elements in list_of_cryptos:
        if elements["names"].lower() == key.lower():
            print("Найден: ", elements["names"], elements["market_cap"], elements["price"])

page = requests.get('https://coinmarketcap.com/ru/all/views/all/')
soup = BeautifulSoup(page.text, 'html.parser')

tbody = soup.find('tbody')

names = [element.text for element in tbody.find_all(class_='cmc-table__cell--sort-by__name')]

market_cap = [element.text for element in tbody.find_all(class_='cmc-table__cell--sort-by__market-cap')]
price = [element.text for element in tbody.find_all(class_='cmc-table__cell--sort-by__price')]

list_of_cryptos = []

for i in range(len(names)):
    d = {}
    d.update({"names": names[i]})
    d.update({"market_cap": market_cap[i]})
    d.update({"price": price[i]})
    list_of_cryptos.append(d)
    print(d["names"], d["market_cap"], d["price"])

Key = input("Введите название: ")

find_key(Key, list_of_cryptos);

with open("test.txt", 'w') as List:
    for i in range(len(names)):
        List.write(names[i] + " " + market_cap[i] + " " + price[i] + "\n")