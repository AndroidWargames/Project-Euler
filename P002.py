# https://projecteuler.net/problem=2


def even_fibonacci(upper):
    total = 0
    fib = [1, 1]
    cycle = 0
    while fib[1] < upper:
        fib = [fib[1], sum(fib)]
        if cycle == 0:
            total += fib[1]
        cycle = (cycle + 1) % 3
    return total

print(even_fibonacci(4*10**6))
