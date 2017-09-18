import sys

# decimal encoded numbers given as arrays. MSB would be a negative number if number is negative.
# implement multiplication

def add(A, B):
    if (len(A) == 0 and len(B) == 0):
        return [0]
    if (len(A) == 0):
        return list(map(lambda x:x, B))
    if (len(B) == 0):
        return list(map(lambda x:x, Z))
    S = []
    a = len(A) - 1
    b = len(B) - 1
    carry = 0
    while (a >= 0 and b >= 0):
        sum = A[a] + B[b] + carry
        S.append(sum % 10)
        carry = sum/10
        a -= 1
        b -= 1
    X = []
    x = -1
    if (a >= 0):
        X = A
        x = a
    elif (b >= 0):
        X = B
        x = b
    while (x >= 0):
        sum = X[x] + carry
        S.append(sum % 10)
        carry = sum/10
        x -= 1
    if (carry > 0):
        S.append(carry)
    S.reverse()
    return S

def multiplyDigit(A, x):
    if (len(A) == 0):
        return [0]
    if (x == 0):
        return [0]
    P = []
    carry = 0
    i = len(A) - 1
    while (i >= 0):
        product = (A[i] * x) + carry
        P.append(product % 10)
        carry = product / 10
        i -= 1
    if (carry > 0):
        P.append(carry)
    P.reverse()
    return P

def appendZeroes(X, n):
    i = 0
    while (i < n):
        X.append(0)
        i += 1

def multiply(A, B):
    negative = False
    if (A[0] < 0):
        A[0] = 0 - A[0]
        negative = True
    if (B[0] < 0):
        B[0] = 0 - B[0]
        negative = not negative
    zeroesToAppend = 0
    P = []
    b = len(B) - 1
    while (b >= 0):
        tp = multiplyDigit(A, B[b])
        appendZeroes(tp, zeroesToAppend)
        P = add(P, tp)
        zeroesToAppend += 1
        b -= 1
    if (negative == True and len(P) > 0):
        P[0] = 0 - P[0]
    return P

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


x = sys.argv[1]
y = sys.argv[2]
X = getArrayForNumber(x)
Y = getArrayForNumber(y)
S = multiply(X, Y)
print(S)