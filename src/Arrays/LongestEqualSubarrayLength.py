import sys

# Write a program that takes an array of integers and find the length of a longest subarray all of whose entries are equal

def solve(A):
    longestSoFar = 1
    current = 1
    i = 1
    while (i < len(A)):
        if (A[i] == A[i-1]):
            current += 1
            if (current > longestSoFar):
                longestSoFar = current
        else:
            current = 1
        i += 1
    return longestSoFar

A = []
i = 1
while (i < len(sys.argv)):
    A.append(int(sys.argv[i]))
    i += 1

print(solve(A))