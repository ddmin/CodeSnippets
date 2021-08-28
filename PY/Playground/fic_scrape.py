import requests
from bs4 import BeautifulSoup
import re

print('Enter link:')
website = input('> ')

print('Enter title:')
title = input('> ')

print(f'Scraping {website}...')
source = requests.get(website).text
soup = BeautifulSoup(source, 'lxml')

story = soup.find('div', id='storytext')
print('Extracting text...')

story = re.sub(r'</p>', '\n', str(story))
story = re.sub(r'<.+?>', '', str(story))

story = re.sub(r'""', '"\n"', str(story))

print(f'Writing text to {title}.txt')
with open(f'{title}.txt', 'w') as f:
    f.write(story)
