import requests
from bs4 import BeautifulSoup

request =requests.get("http://www.barclays.lk/searchresult.asp")
content =request.content
soup = BeautifulSoup(content,"html.parser")
element =soup.find("span",{"class":"reguler-price"})
print(element.text.strip())






