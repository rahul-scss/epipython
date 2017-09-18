import sys

def getArrayForNumber(x):
    negative = False
    start = 0
    if (x[0] == '-'):
        negative = True
        start = 1
    N = []
    while (start < len(x)):
        N.append(int(x[start]))
        start += 1
    if (negative == True):
        N[0] = 0 - N[0]
    return N

def solve(A):
    current = 0
    lastValid = 0
    while (current < len(A)):
        if (A[current] == A[lastValid]):
            current += 1
            continue
        lastValid += 1
        A[lastValid] = A[current]
        current += 1
    lastValid += 1
    while (lastValid < len(A)):
        A[lastValid] = -1
        lastValid += 1

n = sys.argv[1]
N = getArrayForNumber(n)
solve(N)
print(N)