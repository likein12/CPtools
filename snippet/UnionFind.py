class UnionFind():
    def __init__(self,size):
        self.table = [-1 for _  in range(size)]
        self.member_num = [1 for _ in range(size)]
 
    #representative
    def find(self,x):
        while self.table[x] >= 0:
            x = self.table[x]
        return x

    def union(self,x,y):
        s1 = self.find(x)
        s2 = self.find(y)
        m1=self.member_num[s1]
        m2=self.member_num[s2]
        if s1 != s2:
            if m1 != m2:
                if m1 < m2:
                    self.table[s1] = s2
                    self.member_num[s2]=m1+m2
                    return [m1,m2]
                else:
                    self.table[s2] = s1
                    self.member_num[s1]=m1+m2
                    return [m1,m2]
            else:
                self.table[s1] = -1
                self.table[s2] = s1
                self.member_num[s1] = m1+m2
                return [m1,m2]
        return [0,0]
