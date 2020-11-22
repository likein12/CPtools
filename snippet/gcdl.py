def gcd(a,b):
    a,b = max(a,b),min(a,b)
    while a%b!=0:
        a,b = b,a%b
    return b

def gcdl(A):
    if len(A)==2:
        return gcd(A[0],A[1])
    elif len(A)==1:
        return A[0]
    else:
        return gcd(gcdl(A[:len(A)//2]),gcdl(A[len(A)//2:]))