import requests
from bs4 import BeautifulSoup

#把爬蟲偽裝成正常瀏覽器
# head{"User-Agent" : ""}

response = requests.get('http://books.toscrape.com/')
if False:
    if response.ok:
        print(response.text)
    else:
        print(response.status_code)
        print("請求失敗")

#Price
content = response.content
soup = BeautifulSoup(content, "html.parser")
all_prices = soup.findAll("p", attrs={"class" : "price_color" })
for price in all_prices:
    print(price.string)

#Book title

all_titles = soup.findAll("h3")
for title in all_titles:
    print(title.string)