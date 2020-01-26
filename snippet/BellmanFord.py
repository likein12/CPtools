vi=0
min_dis_list = [10**27 for i in range(N)]
min_dis_list[vi] = 0
prev_list = [-1 for i in range(N)]

for i in range(N-1):
    for e in e_list:
		u,v,d = e
		if min_dis_list[v]>min_dis_list[u]+d:
			min_dis_list[v]=min_dis_list[u]+d
			prev_list[v]=u

neg_loop_flag=[False for i in range(N)]

for i in range(N):
	for e in e_list:
		u,v,d = e
		if min_dis_list[u] + d < min_dis_list[v]:
			neg_loop_flag[v]=True
			min_dis_list[v] = min_dis_list[u] + d
		if neg_loop_flag[u]:
			neg_loop_flag[v]=True
