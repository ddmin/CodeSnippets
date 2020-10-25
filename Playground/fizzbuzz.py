def fizzbuzz(n):
    for i in range(1, n+1):
        print(f'{i}\t\t{"Fizz" * (i % 3==0)}{"Buzz" * (i % 5==0)}{"Baxx" * (i % 7==0)}')

fizzbuzz(1000)
