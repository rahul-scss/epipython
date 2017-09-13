import sys

def printBinary(x):
    print(format(x, 'b'))

def parityBruteForce(x):
    parity = 0
    while x > 0:
        parity = parity ^ (x & 1)
        x = x >> 1
    return parity

def paritySlightOptimization(x):
    parity = 0
    while x > 0:
        x = x & (x - 1) # removes rightmost set bit in x.
        parity = parity ^ 1
    return parity

def rightPropagateRightmostSetBit(x):
    # 101010000 to 101011111
    return x | (x ^ (x-1))

def isPowerOfTwo(x):
    # has just one set bit
    return (x & (x-1)) == 0 # LHS removes rightmost set bit from x. so for power of 2, result shold be zero.

n = int(sys.argv[1])
printBinary(n)
print(parityBruteForce(n))
print(paritySlightOptimization(n))
printBinary(rightPropagateRightmostSetBit(n))
print(isPowerOfTwo(n))
