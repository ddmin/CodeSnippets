import requests

BASEURL = input('Base URL (replace page with <>): ')
FIRST = int(input('First page: '))
LAST = int(input('Last page: '))
PADDING = int(input('Pad Length: '))
FILEFORMAT = input('Image Format: ')

for i in range(FIRST, LAST+1):
    print()

    if PADDING-len(str(i)) > 0:
        NUMBER = '0'*(PADDING-len(str(i))) + str(i)
    else:
        NUMBER = str(i)

    IMG_URL = BASEURL.replace('<>', NUMBER)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(IMG_URL, headers=headers)

    print(f'Downloading Page {NUMBER} ({IMG_URL})')
    with open(f'{NUMBER}.{FILEFORMAT}', 'wb') as img:
        img.write(response.content)
