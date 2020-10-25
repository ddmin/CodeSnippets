import time

def timeFib(func, n):
    start = time.time()
    for i in range(n):
        func(i)
    end = time.time()

    print(f'took {end-start} seconds')

def regular_fibonacci(n):
    if n == 0 or n == 1:
        return 1
    b4 = 1
    ftr = 1
    for i in range(n-2):
        temp = ftr
        ftr = b4 + ftr
        b4 = temp
    return ftr

def recursive_fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def memoized_fibonacci():
    prev = [1, 1]
    def fib(n):
        if len(prev) > n:
            return prev[n-2] + prev[n-1]
        else:
            start = len(prev) - 1
            while start != n:
                result = prev[start] + prev[start-1]
                prev.append(result)
                start += 1
            return prev[-1]
    return fib

fib = memoized_fibonacci()

for i in range(2):
    print(f"Pass {i+1}")
    print("regular  : ", end='')
    timeFib(regular_fibonacci, 2500)

    print("memoized : ", end='')
    timeFib(fib, 100000)

    print("recursive: ", end='')
    timeFib(recursive_fibonacci, 16)

    print()

for i in range(2):
    print(f"Pass {i+3}")
    print("regular  : ", end='')
    timeFib(regular_fibonacci, 5000)

    print("memoized : ", end='')
    timeFib(fib, 200000)

    print("recursive: ", end='')
    timeFib(recursive_fibonacci, 33)

    print()

for i in range(2):
    print(f"Pass {i+5}")
    print("regular  : ", end='')
    timeFib(regular_fibonacci, 5500)

    print("memoized : ", end='')
    timeFib(fib, 250000)

    print("recursive: ", end='')
    timeFib(recursive_fibonacci, 34)

    print()
