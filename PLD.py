##Polynomial Long DIvision##
#Performs polynomial long division#

def broadcast(polynomial, constant):
    return [x*constant for x in polynomial]

def format_poly():
    dividend_coefficients = []
    print('Dividend:\n')
    while True:
        coef = input("Coefficient: ")
        if coef == '':
            break
        dividend_coefficients.append(coef)

    print('\n\nQuotient:\n')
    quotient_coefficients = []
    while True:
        coef = input("Coefficient: ")
        if coef == '':
            break
        quotient_coefficients.append(coef)

    return [quotient_coefficients, dividend_coefficients]

def format_answer(start, answer):
    times_run = 0
    for x in answer:
        if x>0 and times_run != 0:
            print('+', end='')
        if x != 1: 
            try:
                print(int(x), end='')
            except:
                print(x, end='')
        else:
            pass
        
        if start == 1:
            print('x', end=' ')
        elif start == 0:
            pass
        else:
            print('x^'+str(start), end=' ')
            
        start-=1
        times_run += 1

quotient, dividend = format_poly()

quotient = list(map(lambda x: int(x), quotient))
dividend = list(map(lambda x: int(x), dividend))

start = len(dividend) - len(quotient)

answer = []
for iterations in range(len(dividend)-(len(quotient)-1)):
    divisor = dividend[0]/quotient[0]
    answer.append(divisor)
    temp_quotient = broadcast(quotient, divisor)
    dividend = [dividend[x] - temp_quotient[x]
                for x in range(len(temp_quotient))] + dividend[len(temp_quotient):]
    dividend = dividend[1:]

remainder = dividend

print()
print('Answer:')
format_answer(start, answer)
print()
print('Remainder:')
format_answer(len(remainder)-1, remainder)
