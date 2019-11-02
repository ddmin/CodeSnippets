from bs4 import BeautifulSoup
from datetime import date
import requests
import config
import praw
import time

#clean up javascript
def slashclean(string):
    copy = ''
    for x in range(len(string)):
        if string[x] != '\\':
            copy += string[x]
    return copy

def authenticate():
    print("Authenticating HighlanderBot...")
    reddit = praw.Reddit(username = config.username,
                         password = config.password,
                         client_id = config.client_id,
                         client_secret = config.client_secret,
                         user_agent = "ddmin's HighlanderBot v1.8")
    print("Authenticated!\n")
    return reddit

def scrape_herricks():
    source = requests.get('https://www.herricks.org/').text
    soup = BeautifulSoup(source, 'lxml')

    slideshow = soup.find('div', class_ = 'ui-widget app gallery json')

    text = slideshow.find('script').text

    text = text.split('{"photoname":')
    text.pop(0)

    headlines = list(map(lambda x: (x.split(',')[0])[1:-1], text))
    headlines = list(map(lambda x: x.strip(), headlines))

    text = slideshow.find('script').text
    text = slideshow.find('script').text
    text = text.split('"caption":')
    text.pop(0)

    par = list(map(lambda x: (x.split('"pause":"","link":"/'))[:-1], text))

    text_body = ''

    for x in range(len(par)):
        text_body += '#**'+headlines[x]+'**\n'
        text_body += '*'+(slashclean(str(par[x][0][1:-2]))).strip() + '*\n'
    return text_body

def run_bot(reddit, date, text_body):
    title = 'Herricks Homepage ' + date
    reddit.subreddit('Herricks').submit(title, selftext=text_body)
    print(title)
    print('Submitted!\n')

def get_previous_homepage():
    with open('previous_homepage.txt', 'r') as f:
        previous_homepage = f.read()
    return previous_homepage

def main():
    reddit = authenticate()
    while True:
        try:
            text_body = scrape_herricks()
            today = str(date.today())
            if text_body != get_previous_homepage():
                run_bot(reddit, today, text_body)
                
                with open('previous_homepage.txt', 'w') as f:
                    f.write(text_body)
                    
                print('Task completed\n')
            else:
                print('Sleeping for 2 hours')
                time.sleep(7200)
        except:
            print('Error')
            time.sleep(10)

if __name__ == '__main__':
    main()
