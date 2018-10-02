import json,pyperclip
import sys
import random
import string


def generate_password():
    return ''.join([str(random.choice(string.ascii_letters+string.digits))
                    for x in range(20)])

def post_json(account, password):
    with open('passwords.json', 'r') as f:
        data = json.load(f)

    load = data['Accounts']
    load.append({'account': account, 'password': password})
    make_json = {"Accounts": load}

    with open('passwords.json', 'w') as f:
        json.dump(make_json, f, indent=2)
    print(f'Account {account} has been updated.')


def check_account(dic, account):
    for x in dic.items():
        if account in x:
            return True
    return False
        

def main():
    if len(sys.argv) < 2:
        print('Help:')
        print('add - adds account and password to json file')
        print('copy - copies password to clipboard')
        sys.exit()

    with open('passwords.json') as f:
        data = json.load(f)

    password_dictionary = {account['account']: account['password']
                           for account in data['Accounts']}

    command = sys.argv[1]

    if command == 'add':
        account = sys.argv[2]
        if check_account(password_dictionary, account) is not True:
            
            password = generate_password()
            post_json(account, password)
            
            sys.exit()
        else:
            print(f'{account} is already in the database')
            sys.exit()


    if command == 'copy':
        account = sys.argv[2]
        if account in password_dictionary:
            password = password_dictionary[account]
            pyperclip.copy(password)
            print(f'Password for {account} has been copied to clipboard')
            sys.exit()
        else:
            print(f'Account {account} does not exist. Would you update the database?')
            confirm = input('Y/N: ').lower()
            if confirm == 'n':
                sys.exit()
            else:
                password = input('Enter the password for {account}: ')
                post_json(account, password)
                sys.exit()

if __name__ == '__main__':
    main()
