def Zalgorithm(S):
    A = [0]*len(S)
    A[0] = len(S)
    i = 1
    j = 0
    while i < len(S):
        while i+j < len(S):
            if S[j] == S[i+j]:
                j+=1
            else:
                break
        A[i] = j
        if j==0:
            i+=1
            continue
        k = 1
        while i+k<len(S):
            if k+A[k]<j:
                A[i+k] = A[k]
                k+=1
            else:
                break
        i += k
        j -= k
    return A
