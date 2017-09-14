import sys

# Given two positive integers x and y, compute quotient of x/y using only addition, subtraction and bit shift operators.

def quotient(x, y):
    while (x >= y):
        y1 = y
        while (x >= y1):
            y1 = y1 << 1
        y1 = y1 >> 1
        x = x - y1
    return x

x = int(sys.argv[1])
y = int(sys.argv[2])
print(quotient(x, y))
