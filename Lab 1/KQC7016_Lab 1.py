import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
page = requests.get(URL)
print (page.text)
soup = BeautifulSoup(page.content, "html.parser")
print (soup)

books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    print(title)
    print(price)
    print()

# Additional Code
# Filter books under £30
print ("Books below £30:")
print()
for book in books:
    price = book.find("p", class_="price_color").text
    title = book.h3.a["title"]

    price_value = float(price[1:])  # remove £ symbol

    if price_value < 30:
        print(title, "-", price)
        print()