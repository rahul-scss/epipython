import sys

# input is 64 bit word. reverse the bits.
# 0000...11100101 => 10100111 ... 0000
# 000..111010 => 010111..000

def printBinary(x):
    print(format(x, 'b'))

def reverseBitsBruteForce(x):
    ctr = 0
    y = 0
    while ctr < 64:
        lsb = x & 1
        y = (y << 1) | lsb
        x = x >> 1
        ctr += 1
    return y

x = int(sys.argv[1])
printBinary(x)
printBinary(reverseBitsBruteForce(x))
