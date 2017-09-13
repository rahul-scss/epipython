import sys

# weight is number of 1s in binary representation of number. e.g., weight of 4 (100) is 1, weight of 11 (1011) is 3.
# given x, find y such that |y-x| is minimum and both y and x have the same weight.

def printBinary(x):
    print(format(x, 'b'))

def getWeight(x):
    weight = 0
    while x > 0:
        x = x & (x-1) # eliminates right most set bit from x.
        weight+=1
    return weight

def bruteForceSolution(x):
    i = 1
    wx = getWeight(x)
    while i < x:
        if (getWeight(i+x) == wx):
            return (i+x)
        if (getWeight(x-i) == wx):
            return (x-i)
        i+=1
    i = x+1
    while (getWeight(i) != wx):
        i+=1
    return i

def solution(x):
    # if last bit is 0, then find the position of least significant 1, and slide that 1 to the right by 1.
    # if last bit is 1, find the least significant 0 and swap it with the 1 right to the right of it
    if (x & 1 == 0):
        z = x & (~(x-1)) # x=1010100 => z=0000100
        return (z >> 1) | (x & (x-1)) # (0000010) | (1010000) = 1010010
    else:
        # lsb is 1
        # x = 101010111 , desired output 101011011
        y = ~x  # 010101000
        z = y & (~(y-1)) # z = 000001000
        z = z | (z >> 1) # z = 000001100
        return x ^ z

x = int(sys.argv[1])
printBinary(x)
s = solution(x)
print(s)
printBinary(s)
br = bruteForceSolution(x)
print(br)
printBinary(br)

