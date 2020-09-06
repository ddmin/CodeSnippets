# read credentials from mail.conf

def read_creds(CONFIG_PATH):
    with open(CONFIG_PATH, "r") as f:
        creds = f.read().split('\n')
    return creds

def parse_creds(CONFIG_PATH):
    creds = read_creds(CONFIG_PATH)
    credentials = {}
    for i in creds:
        n = i.split(': ')
        if len(n) >= 2:
            credentials[n[0]] = n[1]

    if 'smtp-port' in credentials:
        credentials['smtp-port'] = int(credentials['smtp-port'])

    if 'imap-port' in credentials:
        credentials['imap-port'] = int(credentials['imap-port'])

    return credentials

def main():
    credentials = parse_creds('/home/ddmin/.config/mail/mail.conf')
    print(credentials)

if __name__ == '__main__':
    main()
