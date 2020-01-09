from collections import deque

vi = 0  #change
INF = float("inf")

Q = deque([vi])

checked_list = [False]*N
checked_list[vi]=True

min_path_list = [INF]*N #change
min_path_list[vi] = 0

while len(Q)>0:
    v = Q.pop()
    for v1 in e_list[v]:
        if not checked_list[v1]:
            checked_list[v1]=True
            Q.appendleft(v1)
            min_path_list[v1]=min(min_path_list[v1],min_path_list[v]+1) #change
