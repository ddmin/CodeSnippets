import random
import webbrowser
import requests
import re

p = re.compile(r"<title>(.*)</title>")

with open("dailyprogrammer.txt", "r") as f:
	links = [x for x in f.read().split('\n')][:-1]

if len(links) == 0:
	input("You have completed all the challenges!")
	exit()

url = links[0]
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

site = requests.get(url, headers=headers).text[:900]
title = p.search(site).group(1)
print(title)

webbrowser.open(url)

print("Finished? (y/n): ")
op = input("> ").lower()[0]

if op == 'y':
	links.pop(0)

with open("dailyprogrammer.txt", "w") as f:
	f.write("")

with open("dailyprogrammer.txt", 'a') as f:
	for link in links:
		f.write(link + '\n')
