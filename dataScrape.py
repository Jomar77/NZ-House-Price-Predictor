from bs4 import BeautifulSoup
import requests
import pandas as pd
location = []
price = []
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1",
}

cookies = {'session': '17ab96bd8ffbe8ca58a78657a918558'}
r = requests.get(
    "https://homes.co.nz/map/ashburton/ashburton?searchLoc=no%7DjGwwfw_@&view=list",
    headers=headers,
    cookies =cookies
)
soup = BeautifulSoup(r.content, "lxml")
for d in soup.select(".ng-star-inserted .address"):
    name=d.find('div')
    if name is not None:
        location.append(name.text)
    else:
        location.append("-")

df = pd.DataFrame({'Product Name':location})
print(df)