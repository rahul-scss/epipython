import sys

def printBinary(x):
    print(format(x, 'b'))

# 11010001100101100101   LSB is at index 0 (right most), MSB is at highest index (left most)
# input is a (64 bit) number and two indices. Objective is to swap the bits at indices i and j.

def getBitAtIndex(x, i):
    y = x >> i
    return y & 1

def toggleBitAtIndex(x, i):
    return x ^ (1 << i)

def doBitSwap(x, i, j):
    if (i == j):
        return x
    xi = getBitAtIndex(x, i)
    xj = getBitAtIndex(x, j)
    if (xi == xj):
        return x
    y = toggleBitAtIndex(x, i)
    return toggleBitAtIndex(y, j)

x = int(sys.argv[1])
i = int(sys.argv[2])
j = int(sys.argv[3])
printBinary(x)
printBinary(doBitSwap(x, i, j))
