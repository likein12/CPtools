from collections import deque

def EulerTour(vi):
    INF = float('inf')
    Q = deque([vi])
    vs = [vi]
    depth = [0]
    min_path_list = [INF]*N #change
    min_path_list[vi] = 0
    checked_list = [-1]*N
    checked_list[vi] = 0
    count = 1
    while len(Q)>0:
        v = Q.pop()
        if len(v)==1:
            Q.append((v,0))
            for v1 in e_list[v]:
                if checked_list[v1]==-1:
                    checked_list[v1] = count
                    count+=1
                    vs.append(v1)
                    Q.append(v1)
                    min_path_list[v1]=min(min_path_list[v1],min_path_list[v]+1)
                    depth.append(min_path_list[v1])
        else:
            vs.append(v[0])
    return vs, depth, checked_list
