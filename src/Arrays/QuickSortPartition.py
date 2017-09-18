import sys

# given an array A and pivot index p, so pivot element being E = A[p] (from original array) arrange the array such that 
# all elements less than E appear first, then elements equal to E then elements greater than E

def partition(A, p):
    e = A[p]
    unexploredStart = 0
    unexplorerEnd = len(A) - 1
    smallEnd = -1
    while (unexploredStart <= unexplorerEnd):
        if (A[unexploredStart] == e):
            unexploredStart += 1
        elif (A[unexploredStart] > e):
            temp = A[unexplorerEnd]
            A[unexplorerEnd] = A[unexploredStart]
            A[unexploredStart] = temp
            unexplorerEnd -= 1
        else:
            smallEnd += 1
            if (smallEnd < unexploredStart):
                temp = A[unexploredStart]
                A[unexploredStart] = A[smallEnd]
                A[smallEnd] = temp
            unexploredStart += 1

A = [1,6,4,2,6,2,8,5,3,234,2,6,2,6,8,3,2,67,8,3,2,6,8,3,23,3]
p = 6
partition(A, p)
print (', '.join(map(lambda x:str(x), A)))