import re
import requests

url = input('Enter website URL: ')
site = requests.get(url).text
tag = input('Enter tag: ')
pattern = re.compile(f'(<{tag}(\s.*)?>)(.*?)(</{tag}>)')

matches = pattern.finditer(site)

text = ''
for match in matches:
    text += match[3] + '\n'

print(text)
