def any_base_convert(num, start, final):
    '''
    Converts a number "num" from base "start" to base "final"
    '''
    temp = base_10(num, start)
    return base_convert(temp, final)


def base_convert(num, base):
    '''
    Converts a number "num" from base 10 to base "base"
    '''
    ALPHANUMERIC = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    
    num = int(num)

    if num < base:
        return ALPHANUMERIC[num]
    return base_convert(num//base, base) + base_convert(num % base, base)


def base_10(num, base):
    '''
    Converts a number "num" from base "base" to base 10
    '''
    num = str(num)

    ALPHANUMERIC = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    LOOKUP_TABLE = {x: n for n, x in enumerate([s for s in ALPHANUMERIC[:base]])}

    return convert_base_10(num, base, 0, LOOKUP_TABLE)


def convert_base_10(num, base, iteration, LOOKUP_TABLE):
    '''
    Performs the actual conversion to base 10
    '''
    if len(num) == 1:
        return LOOKUP_TABLE.get(num[0]) * (base ** iteration)
    return (convert_base_10(num[:-1], base, iteration + 1, LOOKUP_TABLE) 
          + convert_base_10(num[-1],  base, iteration,     LOOKUP_TABLE))


def main():
    print(any_base_convert('Hello', 62, 10))
    print(any_base_convert('260914464', 10, 62))


if __name__ == '__main__':
    main()