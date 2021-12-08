# [Intermediate] Challenge 6

def remove_duplicates(string):
    lst = []
    for i in string:
        if i not in lst:
            lst.append(i)
    return ''.join(lst)

def main():
    test1 = 'ameliorate'
    test2 = 'indispensible'
    test3 = 'incorrigible'
    test4 = 'ganglia'
    test5 = 'amyotrophic'

    ans1 = 'ameliort'
    ans2 = 'indspebl'
    ans3 = 'incorgble'
    ans4 = 'ganli'
    ans5 = 'amyotrphic'

    tests = [(test1, ans1), (test2, ans2),
             (test3, ans3), (test4, ans4), (test5, ans5)]

    for test in tests:
        if remove_duplicates(test[0]) != test[1]:
            print('Test Failed.')
            print(f"'{test[0]}' returned ", end='')
            print(f"'{remove_duplicates(test[0])}' instead of '{test[1]}'")
            return False

    print('All tests passed!')

if __name__ == '__main__':
    main()
