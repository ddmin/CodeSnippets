import requests
from bs4 import BeautifulSoup

url = input('URL: ')

top_url = input('Top Level Domain URL (leave blank for none): ')
if top_url:
    TOP_LEVEL = True
else:
    TOP_LEVEL = False

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
    try:
        if 'href' in i.attrs:
            LINK = i['href']

            if TOP_LEVEL:
                LINK = top_url + LINK

            print(f"Downloading {LINK}")
            # wget.download(LINK, out=f'{COUNT_FROM + n}.{FILE_FORMAT}')

            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            response = requests.get(LINK, headers=headers)

            with open(f'{COUNT_FROM + n}.{FILE_FORMAT}', 'wb') as img:
                img.write(response.content)
    except:
        print("Error. Skipping.\n")
        continue
