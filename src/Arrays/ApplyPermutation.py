import sys

# Example: given array A = [a,b,c,d], given permutation P = [2,0,1,3]
# then permutated A = [b,c,a,d] that is element A[i] goes to element A[P[i]]

class Input:
    def __init__(self, a, p):
        self.A = a
        self.P = p

def readInput(X):
    a = []
    p = []
    narg = int(X[1])
    i = 2
    while (i < narg + 2):
        a.append(X[i])
        i += 1
    t = i
    while (i < t + narg):
        p.append(int(X[i]))
        i += 1
    return Input(a, p)

def permute(input):
    E = input.A
    P = input.P
    i = 0
    t2 = E[i]
    while (i < len(P)):
        if (P[i] == -1):
            i += 1
            if (i < len(P)):
                t2 = E[i]
            continue
        t1 = E[P[i]]
        E[P[i]] = t2
        t2 = t1
        z = P[i]
        P[i] = -1
        i = z
    
ip = readInput(sys.argv)
print(ip.A)
print(ip.P)
permute(ip)
print(ip.A)
print(ip.P)