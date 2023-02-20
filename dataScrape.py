from bs4 import BeautifulSoup
import requests

url = "https://www.oneroof.co.nz/search/houses-for-sale/district_ashburton-canterbury-281_bedroom_3,4_price-to_500000_order_lowest-price-2_page_1"
page = requests.get(url)
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_='house-feature-wrap')

for list in lists:
    price = list.find('div', class_='price')
    location = list.find('div', class_='address')
    bedroom = list.find('div', class_='other')
    info = [ location, price, bedroom]
    print(info)
