# https://projecteuler.net/problem=3

import math

def get_primes(n):
    a = [2, 3]
    if n == 2:
        return [2]
    elif n == 3:
        return a
    elif n < 2:
        return []
    i = 5
    while i <= n:
        p = True
        for j in a:
            if i % j == 0:
                p = False
        if p:
            a.append(i)
        i += 1
    return a


def is_prime(n):
    p = get_primes(math.sqrt(n))
    for i in p:
        if n % i == 0:
            return i
    return 0


# This function iteratively generates a list of prime numbers based on whether or not they are divisible by smaller
# prime values. A placeholder for the input is created, and that placeholder is repeatedly divided by each new prime
# for as long as that prime is a factor of the placeholder. Worst case runtime for this algorithm is roughly O(n^(1/2)),
# but the runtime is cut considerably by a factor of the square of any prime factors discovered
def highest_prime_factor(inp):
    cur = inp
    i = 2
    primes = []
    primefactors = []

    while i <= cur:
        p = True
        a = True
        # add to prime list
        for j in primes:
            if j > math.sqrt(i):
                break
            if i % j == 0:
                p = False
                break
        if p:
            primes.append(i)
            # attempt to cut down input
            while cur % i == 0:
                primefactors.append(i)
                cur /= i
        i += 1
    return max(primefactors)

print(highest_prime_factor(600851475143))
