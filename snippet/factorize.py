from collections import defaultdict
def factorize(n):
    dd = defaultdict()
    for i in range(2,int(n**0.5)+1):
        while n%i==0 and n>0:
            dd[i]+=1
            n//=i
    if n>1:
        dd[n]+=1
    return dd