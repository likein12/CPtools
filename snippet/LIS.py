#weakly increase
def LIS(L):
    INF = float('inf')
    DP = [INF]*(len(L)+1)

    def bisect(v):
        if v<DP[0]:
            return 0
        l = 0
        r = len(L)
        while r-l>1:
            if v<DP[(l+r)//2]:
            #if v<=DP[(l+r)//2]:
                r = (l+r)//2
            else:
                l = (l+r)//2
        return r
    
    for v in L:
        DP[bisect(v)] = v
    return DP
