#dijkstra
#you need to prepare e_list = [(orient,dist)]

import heapq

vi = 0
INF = float('inf')
min_d_list = [INF]*N
min_d_list[vi] = 0
prev_list = [-1]*N
q = []
for i in range(N):
	heapq.heappush(q,(min_d_list[i],i))

while len(q)>0:
	d,v = heapq.heappop(q)
	for e in e_list[v]:
		v1,d1 = e
		if min_d_list[v1] > d+d1:
			min_d_list[v1] = d+d1
			prev_list[v1] = v
			heapq.heappush(q,(d+d1,v1))
