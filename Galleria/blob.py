import wget
import requests
from bs4 import BeautifulSoup

url = input('URL: ')
SEARCH_FOR = input('Searching for: ')
FILE_FORMAT = input('File Format: ')
COUNT_FROM = int(input('Count From: '))

html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')

links = soup.find_all('a')

dl = []

for result in links:
    if SEARCH_FOR in str(result):
        dl.append(result)

for n, i in enumerate(dl):
    print()
    print(i['href'])
    if 'href' in i.attrs:
        LINK = i['href']
        print(f"Downloading {LINK}")
        wget.download(LINK, out=f'{COUNT_FROM + n}.{FILE_FORMAT}')
