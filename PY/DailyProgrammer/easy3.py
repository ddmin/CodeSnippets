# [Easy] Challenge 3

import sys


def rot(letter, num):
    return chr((ord(letter) - 97 + num) % 26 + 97)

def crypt(msg, n):
    new = ''
    for letter in msg:
        if not letter.isalpha():
            new += letter
        elif letter.isupper():
            new += rot(letter.lower(), n).upper()
        else:
            new += rot(letter, n)
    return new


# -m    message to be encrypted / decrypted
# -d    set mode to decrypt (defaults to encrypt)
def parse_args(lst):
    arg_dict = {'m': None, 'd': False, 'n': 13}

    if '-m' not in lst:
        return arg_dict

    elif lst.index('-m') + 1 == len(lst):
        return arg_dict

    else:
        arg_dict['m'] = lst[lst.index('-m') + 1]

    if '-d' in lst:
        arg_dict['d'] = True

    if '-n' not in lst:
        return arg_dict

    elif lst.index('-n') + 1 == len(lst):
        print("(Value for rotation not entered. Defaulting to 13.)\n")
        return arg_dict

    else:
        arg_dict['n'] = int(lst[lst.index('-n') + 1])
        return arg_dict


def help():
    print("CiPyher -m [message] [options]")
    print("\t-h       Display this message and exit.")
    print("\t-m       Message to decrypt / encrypt.")
    print("\t-d       Set mode to decrypt (encrypt by default).")
    print("\t-n       Set value to rotate by.")
    sys.exit()


def main():
    if '-h' in sys.argv:
        help()
        sys.exit()

    arg_dict = parse_args(sys.argv)
    if not arg_dict['m']:
        print("Please supply a message to decrypt / encrypt.")
        sys.exit()

    if not arg_dict['d']:
        print(crypt(arg_dict['m'], arg_dict['n']))
    else:
        print(crypt(arg_dict['m'], -1 * arg_dict['n']))

if __name__ == '__main__':
    main()
