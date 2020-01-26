from collections import defaultdict
def compression(A):
    B = sorted(A)
    atoi = defaultdict(int)
    itoa = []
    prev = -float('inf')
    count = 0
    for i in range(N):
        if prev < B[i]:
            itoa.append(B[i])
            atoi[B[i]] = count
            prev = B[i]
            count+=1
    return atoi,itoa
