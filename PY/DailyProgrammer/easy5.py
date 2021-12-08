# [Easy] Challenge 5

import sys
import getpass

pw = getpass.getpass("Enter your password: ")

if not (pw == "password"):
    print("Wrong Password!")
    sys.exit()

print("Hello World!")
