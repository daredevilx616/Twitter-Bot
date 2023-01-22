import requests
from bs4 import BeautifulSoup

req = requests.get("https://bitflyer.com/en-us/bitcoin-chart")
soup = BeautifulSoup(req.content, "html.parser")
prices = soup.find_all('span', {'class': 'c-text--number'})

max_price = prices[0].text
min_price = prices[1].text


