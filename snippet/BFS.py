from collections import deque

vi = 0  #change
INF = float('inf')

Q = deque([vi])

min_path_list = [INF]*N #change
min_path_list[vi] = 0

while len(Q)>0:
    v = Q.pop()
    for v1 in e_list[v]:
        if min_path_list[v1] >= INF:
            Q.appendleft(v1)
            min_path_list[v1] = min_path_list[v]+1 #change
