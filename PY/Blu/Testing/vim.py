# open vim buffer

import os

vim = lambda : os.system('vim /tmp/mail.txt')

def format_message():
    with open('/tmp/mail.txt', 'w') as f:
        HEADER = 'To: \nSubject: \n'
        f.write(HEADER)

def parse_message():
    with open('/tmp/mail.txt', 'r') as f:
        txt = f.read()

    to = txt.split('\n')[0].split()[1:]
    body = txt

    return to, body

def main():
    format_message()
    vim()
    to, body = parse_message()
    print(to)
    print(body)

if __name__ == '__main__':
    main()
