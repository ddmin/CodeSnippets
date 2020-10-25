fizzbuzz = lambda n: '\n'.join([f'{i}\t{"Fizz" * (i % 3==0)}{"Buzz" * (i % 5==0)}{"Baxx" * (i % 7==0)}' for i in range(1, n+1)])

print(fizzbuzz(500))