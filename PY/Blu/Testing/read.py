import imaplib
import email
import re

import cred

def read(creds):
    username = creds['username']
    password = creds['password']
    imap_server = creds['imap']
    imap_port = creds['imap-port']

    mail = imaplib.IMAP4_SSL(imap_server, imap_port)
    mail.login(username, password)

    mail.select("Inbox")

    typ, data = mail.search(None, 'ALL')
    mail_ids = data[0].split()

    for n in mail_ids[::-1]:
        print('Email ID: ' + n.decode('utf-8'))
        typ, data = mail.fetch(n, '(RFC822)')

        for x in data:
            if isinstance(x, tuple):
                print(x)
                msg = email.message_from_string(x[1].decode('utf-8'))

                p = re.compile('Subject:.*\n([\w\W]*)')
                html_test = re.compile('<[\w\W]*>')

                email_subject = msg['subject']
                email_from = msg['from']
                email_date = msg['date']
                email_body = re.search(p, str(msg)).group(1)

                if re.search(html_test, email_body):
                    email_body = '\nThis email contains HTML elements.'

                print(f'Subject: {email_subject}')
                print(f'From: {email_from}')
                print(f'Recieved: {email_date}')
                print(email_body)
                print('==================================')
                print()

def main():
    CONFIG = '/home/ddmin/.config/mail/mail.conf'
    creds = cred.parse_creds(CONFIG)

    read(creds)


if __name__ == '__main__':
    main()
