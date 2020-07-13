import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text,'html.parser')

links =(soup.select('.storylink')[0])
votes = soup.select('.score')

print(votes[0])