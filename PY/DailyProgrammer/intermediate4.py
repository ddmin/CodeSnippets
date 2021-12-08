# [Intermediate] Challenge 4

# return the position of the next operation according to order of operations
def get_pos(lst):
    # order of operations
    for op in ['*', '/', '+', '-']:
        for n, i in enumerate(lst):
            if i == op:
                return n

# perform the appropriate operation
def operation(i, inp):
    if inp[i] == '+':
        ans = float(inp[i-1]) + float(inp[i+1])
    elif inp[i] == '-':
        ans = float(inp[i-1]) - float(inp[i+1])
    elif inp[i] == '*':
        ans = float(inp[i-1]) * float(inp[i+1])
    elif inp[i] == '/':
        ans = float(inp[i-1]) / float(inp[i+1])

    return ans

# calculate the answer
def calculate(inp):

    inp = parse(inp)

    while len(inp) != 3:

        i = get_pos(inp)
        n = operation(i, inp)
        inp = inp[:i-1] + [n] + inp[i+2:]

    # Perform operation one last time
    return operation(1, inp)

# break up input into numbers and symbols
def parse(inp):
    stack = []
    temp = [i for i in inp]

    last = -1
    for i in range(len(temp)):
        if not temp[i].isnumeric():
            stack.append(''.join(temp[last + 1: i]))
            stack.append(temp[i])
            last = i

    # loop ends before last number is entered
    stack.append(''.join(temp[last + 1:]))
    return stack

def main():
    print('PyCalc 1.0.0')
    while True:
        try:
            inp = input('>>> ')

            if inp == 'exit':
                break

            inp = inp.replace(' ', '')
            print(calculate(inp))
        except:
            print('Error. Check your input.')

if __name__ == '__main__':
    main()
