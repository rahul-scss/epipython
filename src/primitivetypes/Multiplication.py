import sys

# Multiply two non negative integers using only the following operators:
#   assignment
#   bitwise operators >>, <<, |, &, ~, ^
#   equality checks and boolean combinations thereof
# implies cannot use increment, decrement, or test if x < y

def increment(x):
    xorer = 1
    y = x
    lsb = y & 1
    while (lsb == 1):
        xorer = (xorer << 1) | 1
        y = y >> 1
        lsb = y & 1
    return x ^ xorer

def add(x, y):
    c = 0
    result = 0
    shift = 0
    while ((x != 0) or (y != 0) or (c != 0)):
        bitSum = ((x ^ y) ^ c) & 1
        if bitSum == 1:
            result = result | (1 << shift)
        shift = increment(shift)
        if (c == 0):
            c = (c | (x & y)) & 1
        else: 
            c = (c & (x | y)) & 1
        x = x >> 1
        y = y >> 1
    return result

def multiply(x, y):
    result = 0
    shift = 0
    while (y != 0):
        if ((y & 1) == 1):
            result = add(result, (x << shift))
        y = y >> 1
        shift = increment(shift)
    return result

x = int(sys.argv[1])
y = int(sys.argv[2])
print(multiply(x, y))