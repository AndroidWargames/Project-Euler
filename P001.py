# https://projecteuler.net/problem=1

def mult_3n5(upper):
    upper -= 1 # since we're looking for numbers below the input
    cycles = upper//15
    # every cycle of 15 contains the same pattern of 7 numbers
    cnums = [3, 5, 6, 9, 10, 12, 15]
    # those numbers MOD 15 summed is 60
    # add the previous triangular number * 15
    presum = cycles * 60 + int(cycles * (cycles - 1) / 2 * 15 * 7)
    top = upper % 15
    tsum = 0
    for i in cnums:
        if i <= top:
            tsum += 15*cycles + i
    return presum + tsum


def mult_3n5_naive(upper):
    out = 0
    for i in range(upper):
        if i % 3 == 0 or i % 5 == 0:
            out += i
    return out

print(mult_3n5(1000))
print(mult_3n5_naive(1000))