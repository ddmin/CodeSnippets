from bs4 import BeautifulSoup
import requests


def strip_text(text):
    copy = ''
    for x in text:
        copy += x
        if x == '>':
            break
    return copy

def get_link(text):
    for x in range(len(text)):
        if text[x:x+6] == 'href="':
            return text[x+6:-2]



source = requests.get("https://www.nytimes.com/section/opinion").text
soup = BeautifulSoup(source, 'lxml')

soup = soup.find_all("article")

crawl = []
for article in soup:
    x = str(article.find("a"))
    x = strip_text(x)
    x = get_link(x)
    crawl.append(x)

for link in crawl:

    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')
    try:
        full_copy = 'Source: ' + link + '\n\n'
        title = soup.find("header", class_="css-dm8bmq e345g291")
        title = title.find("span").text
        full_copy += 'Title: ' + title + '\n'

        author =soup.find("div", class_="css-1baulvz")
        author = author.find("span", class_="css-1baulvz").text
        
        print(title)
        print(author)

        subtitle = soup.find("header", class_="css-dm8bmq e345g291")
        subtitle = subtitle.find("p", class_="css-1fv8d3g ewc5vgb0").text
        full_copy += 'Subtitle: '+subtitle + '\nBy ' + author + '\n\n' 

        actual_text = soup.find_all("div",class_="css-18sbwfn StoryBodyCompanionColumn")
        copy = ''

        for x in actual_text:
            mini = x.find_all("p")
            for y in mini:
                copy += y.text +'\n\n'

        full_copy += copy
    
        title = title.replace(':', '-')+'.txt'
        
        with open(title, 'w') as f:
            f.write(full_copy)
            time.sleep(3)

    except:
        print()
