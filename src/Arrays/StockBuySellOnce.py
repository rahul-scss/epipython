import sys

def solve(A):
    minSoFar = -1
    maxProfitSoFar = -1
    i = 0
    while (i < len(A)):
        if (A[i] < minSoFar or minSoFar == -1):
            minSoFar = A[i]
        elif (minSoFar != -1):
            p = A[i] - minSoFar
            if (p > maxProfitSoFar):
                maxProfitSoFar = p
        i += 1
    return maxProfitSoFar

A = []
i = 1
while (i < len(sys.argv)):
    A.append(int(sys.argv[i]))
    i += 1

print(solve(A))
