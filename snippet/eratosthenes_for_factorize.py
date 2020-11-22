def SOE_for_factorize(n):
    p = 2
    D = [0]*(n+1)
    while p**2<=n:
        if D[p]==0:
            k = p*p
            while k <= n:
                if D[k] == 0:
                    D[k] = p
                k += p
        p+=1
    return D
