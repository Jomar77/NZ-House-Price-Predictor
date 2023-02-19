from bs4 import BeautifulSoup
import requests

url = "https://www.realestate.co.nz/residential/sale/canterbury/ashburton?maxp=500000&minba=1&minbe=2&mincp=1&minp=400000"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_='tile--body')

for list in lists:
    title = list.find('h3', class_='h-6')
    location = list.find('h3', class_='mb-1')
    bedroom = list.find('div', ='bathroom')
    bathroom = list.find('div', class_='price')