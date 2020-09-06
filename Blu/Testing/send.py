# send mail

import smtplib
import ssl

# From testing directory
import cred
import vim

def send(msg, to, creds):
    username = creds['username']
    password = creds['password']
    smtp_address = creds['smtp']
    smtp_port = creds['smtp-port']
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, to, msg)

def main():
    CONFIG = '/home/ddmin/.config/mail/mail.conf'
    creds = cred.parse_creds(CONFIG)

    vim.format_message()
    vim.vim()
    to, msg = vim.parse_message()

    send(msg, to, creds)

if __name__ == '__main__':
    main()
