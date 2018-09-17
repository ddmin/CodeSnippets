def titleize(title):
    exceptions = ['a', 'he', 'for', 'the', 'and', 'in',
                  'to', 'of', 'from', 'with']

    if ':' in title:
        double = title.split(':')
        master = ''
        for part in double:
            master += titleize(part)[:-1]
            if part != double[-1]:
                master += ': '
        return master

    master_title = title.split()[0].capitalize() + ' '
    for word in title.split()[1:]:
        if word not in exceptions:
            master_title += word.capitalize() + ' '
        else:
            master_title += word.lower() + ' '
    return master_title

def main():
    title = input('Enter title: ')
    print(titleize(title))

if __name__ == '__main__':
    main()
