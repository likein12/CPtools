INF = float('inf')
D = [[INF]*N for i in range(N)]
for i in range(N):
    for j,d in e_list[i]:
        D[i][j]=d

for k in range(N):
    for i in range(N):
        for j in range(N):
            if D[i][j]>D[i][k]+D[k][j]:
                D[i][j] = D[i][k]+D[k][j]
