class BIT:
            
    def __init__(self, L):
        self.N = len(L)
        self.bit = [0]*self.N
        for i,l in enumerate(L):
            self.add(i,l)

    def add(self, a, w):
        x = a + 1
        for i in range(1000):
            self.bit[x-1] += w
            x += x & -x
            if x > self.N:
                break

    def sum(self, a):
        x = a+1
        ret = 0
        for i in range(1000):
            ret += self.bit[x-1]
            x -= x & -x
            if x <= 0:
                break        
        return ret

