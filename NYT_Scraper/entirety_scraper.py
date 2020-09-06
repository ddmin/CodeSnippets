from bs4 import BeautifulSoup
import requests
import time


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

def isolate_link(text):
    copy = ''
    for x in range(len(text)):
        if text[x:x+6] == 'href="':
            x = x+6
            while True:
                copy += text[x]
                x += 1
                if text[x] == '"':
                    break
    return copy


source = requests.get("https://www.nytimes.com").text
soup = BeautifulSoup(source, 'lxml')

lnk = soup.find_all("a", class_="css-1wjnrbv")

for site in lnk:
    s = isolate_link(str(site))
    source = requests.get(s).text
    
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
            
            title = soup.find("title").text
            print(title)
            
            full_copy += 'Title: ' + title + '\n'


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
            
            with open(title, 'w') as f:
                f.write(full_copy)
            

        except:
            pass
