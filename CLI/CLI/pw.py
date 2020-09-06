import getpass
import json
import os
import pyperclip
import random
import string
import sys

generate_password = lambda: ''.join([str(random.choice(string.ascii_letters
                                    +string.digits)) for x in range(20)])

clear_screen = lambda: os.system('cls') 

def update_accounts(accounts, account, password=None):
    option = 'y'

    if not password:
        password = generate_password()

    if account in accounts['Accounts']:
        print(f"{account} already exists. Would you like to update? (y/n)")
        option = input('> ').lower()[0]

    if option == 'y':
        accounts['Accounts'][account] = password

    with open("passwords.json", "w") as f:
        json.dump(accounts, f, indent=2)

def list_accounts(accounts):
    for i, account in enumerate(accounts['Accounts']):
        print(f"{str(i+1).rjust(2, '0')}. {account}")
    print()

def read_accounts():
    with open("passwords.json") as f:
        accounts = json.load(f)

    return accounts

def main():
    cwd = os.getcwd()
    directory = os.path.join(cwd, 'Passwords')

    if not os.path.isdir(directory):
        os.mkdir(directory)
        with open(os.path.join(directory, "passwords.json"), "w") as f:
            default = {"Accounts": {}}
            json.dump(default, f, indent=2)

    os.chdir(directory)

    

    while True:
        accounts = read_accounts()
        
        clear_screen()
        
        list_accounts(accounts)
        print("Options:")
        print("1. Add/Update Account Password")
        print("2. Get Account Password")
        print("3. Exit")
        option = input("> ")
        
        clear_screen()

        if option == '1':
            print("Name of account:")
            account = input("> ")
            print("Password for account:")
            print("(Leave blank for random password)")
            password = getpass.getpass()
            update_accounts(accounts, account, password)

        elif option == '2':
            list_accounts(accounts)
            account_list = [account for account in accounts['Accounts']]
            print("Get password of which account?")
            number = int(input("> ")) - 1
            password = accounts['Accounts'].get(account_list[number])
            pyperclip.copy(password)

        elif option == '3':
            sys.exit()

if __name__ == '__main__':
    main()