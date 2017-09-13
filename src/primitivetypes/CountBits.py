def countBits(x):
    numberOfBits = 0
    while (x != 0):
        numberOfBits += x & 1
        x = x >> 1
    return numberOfBits

print(countBits(76342661))
