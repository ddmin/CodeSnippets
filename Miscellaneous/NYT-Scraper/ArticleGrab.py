from bs4 import BeautifulSoup

with open('Article.txt') as f:
    source = f.read()

soup = BeautifulSoup(source, 'lxml')

title = soup.find("title").text
print(title)

full_copy = 'Title: ' + title + '\n'

author =soup.find("div", class_="css-1baulvz")
author = author.find("span", class_="css-1baulvz").text

full_copy += '\nBy ' + author + '\n\n'
actual_text = soup.find_all("div",class_="css-18sbwfn StoryBodyCompanionColumn")
copy = ''

for x in actual_text:
    mini = x.find_all("p")
    for y in mini:
        copy += y.text +'\n\n'

full_copy += copy

title = title.replace(':', '-')
title = title.replace('|', '-')+'.txt'

print(full_copy)

# with open(title, 'w') as f:
#     f.write(full_copy)