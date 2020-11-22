from collections import deque

INF = float('inf')

Q = deque([vi])

min_path_list = [[INF]*W for i in range(H)] 
x,y = start
min_path_list[x][y] = 0
nxt = [(0,1),(0,-1),(1,0),(-1,0)]
while len(Q)>0:
    x,y = Q.pop()
    for dx,dy in nxt:
        x1 = x+dx
        y1 = y+dy
        if 0<=x1<H and 0<=y1<W:                  
                if min_path_list[x1][y1]>=INF and S[x1][y1]!='#':
                    Q.appendleft((x1,y1))
                    min_path_list[x1][y1]=min_path_list[x][y]+1
