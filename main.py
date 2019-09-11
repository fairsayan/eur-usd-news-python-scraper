import requests
from bs4 import BeautifulSoup

url = 'https://it.investing.com/currencies/eur-usd-news'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

titles = soup.findAll('article', {'class': 'articleItem'})
for title in titles:
  node = title.find('div', {'class': 'textDiv'}).find('a', {'class': 'title'})
  if node:
    print (node.get_text().strip())
