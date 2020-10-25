class UnavaliableBaseError(Exception):
    def __init__(self):
        Exception.__init__(self, "Sadly there aren't enough characters in " \
                                 "the English alphabet to allow for " \
                                 "bases higher than 62. Also why would you" \
                                 " need anything higher?")


def convert_decimal(base, number):
    base = int(base)
    conversion = ''
    
    if number == 0:

        return 0
    
    while number != 0:

        remainder = number % base
        number = number // base
        remainder = index(remainder)
        conversion += remainder

    return conversion[::-1]

def index(index):
    if index > 61:
        raise UnavaliableBaseError()
    
    look_up = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    return look_up[index]


def character_search(char):
    look_up = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for x in range(len(look_up)):
        if look_up[x] == str(char):
            return x
    

def convert_to_decimal(base, number):
    base = int(base)
    summ = 0
    for x, y in zip(range(len(str(number))-1, -1, -1), range(len(str(number)))):
        z = character_search(str(number)[y])
        summ += z*(base**x)
    return summ

        
def anybase(base1, base2, number):
    number = convert_to_decimal(base1, number)
    number = convert_decimal(base2, number)
    return number


def main():
    number = input('Convert: ')
    
    base1 = input('from base: ')

    if int(base1) > 62:
        raise UnavaliableBaseError()
        
    base2 = input('to base: ')
    
    if int(base2) > 62:
        raise UnavaliableBaseError()

    print('\nConversion: ', end='')
    print(anybase(base1, base2, number))



if __name__ == '__main__':
    main()
