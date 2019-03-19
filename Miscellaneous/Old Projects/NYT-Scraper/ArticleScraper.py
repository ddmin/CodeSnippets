from bs4 import BeautifulSoup
import requests
import pyperclip
import time

print('Enter the URLs of the articles you want:')
inn = ''
links = []
while True:
    inn = input()
    if inn == '':
        break
    links.append(inn)
    
print()
print("Copy article to clipboard or text file?")
print("1. Clipboard")
print("2. Text File")
print("3. Both")
option = int(input())
print()

master_copy = ''
for link in links:
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')

    try:
        full_copy = 'Source: ' + link + '\n\n'
                
        title = soup.find("title").text
                
        full_copy += 'Title: ' + title + '\n'


        author =soup.find("div", class_="css-1baulvz")
        author = author.find("span", class_="css-1baulvz").text

        full_copy += '\nBy ' + author + '\n\n'
        print(full_copy)
        actual_text = soup.find_all("div",class_="css-18sbwfn StoryBodyCompanionColumn")
        copy = ''

        for x in actual_text:
            mini = x.find_all("p")
            for y in mini:
                copy += y.text +'\n\n'

        full_copy += copy
        master_copy += full_copy + '\n\n\n\n\n'
        title = title.replace(':', '-')+'.txt'
        
        if option == 2 or option == 3:      
            with open(title, 'w') as f:
                
                f.write(full_copy)
                print()
                print(f'Article copied to text file')

    except:
        print("Oops, something went wrong!")
        print('Press enter to quit')
        print()
        input()

if option == 1 or option == 3:
    pyperclip.copy(master_copy)
    print("Article(s) copied to clipboard")

print()
print('Done')
print('Press enter to quit')
print()
input()
