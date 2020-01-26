from collections import deque

INF = float('inf')

def EulerTour(vi):
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

class SegmentTree:
    def __init__(self, L, op, ide):
        self.op = op
        self.ide = ide
        self.sz = len(L)
        self.n = 1
        self.s = 1
        for i in range(1000):
            self.n *= 2
            self.s += 1
            if self.n >= self.sz:
                break
        self.node = [self.ide]*(2*self.n-1)

        for i in range(self.sz):
            self.node[i+self.n-1] = L[i]

        for i in range(self.n-2,-1,-1):
            self.node[i] = self.op(self.node[i*2+1],self.node[i*2+2])
    
    def add(self, a, x):
        k = a+self.n-1
        self.node[k] += x
        for i in range(1000):
            k = (k-1)//2
            self.node[k] = self.op(self.node[2*k+1], self.node[2*k+2])
            if k <= 0:
                break
    
    def substitute(self, a, x):
        k = a+self.n-1
        self.node[k] = x
        for i in range(1000):
            k = (k-1)//2
            self.node[k] = self.op(self.node[2*k+1], self.node[2*k+2])
            if k <= 0:
                break

    def get_one(self, a):
        k = a+self.n-1
        return self.node[k]
    
    def get(self, l, r):
        res = self.ide
        n = self.n
        if self.sz <= r or 0 > l:
            print("error")
            return False

        for i in range(self.s):
            count = 2**i-1
            a = (r+1)//n
            b = (l-1)//n
            if a-b == 3:
                res = self.op(self.node[count+b+1],res)
                res = self.op(self.node[count+b+2],res)
                right = a*n
                left = (b+1)*n-1
                break
            if a-b == 2:
                res = self.op(self.node[count+b+1],res)
                right = a*n
                left = (b+1)*n-1
                break
            n = n//2

        #left
        n1 = n//2        
        for j in range(i+1,self.s):
            count = 2**j-1 
            a = (left+1)//n1
            b = (l-1)//n1
            if a-b == 2:
                res = self.op(self.node[count+b+1],res)
                left = (b+1)*n1-1                
            n1 = n1//2

        #right
        n1 = n//2        
        for j in range(i+1,self.s):
            count = 2**j-1 
            a = (r+1)//n1
            b = (right-1)//n1
            if a-b == 2:
                res = self.op(self.node[count+b+1],res)
                right = a*n1                
            n1 = n1//2
        return res
    
vs,depth,id = EulerTour(vi)

ST = SegmentTree(depth, min, INF)

def LCA(x,y):
    return vs[ST.get_min_index(x,y)]
# segment tree index is needed