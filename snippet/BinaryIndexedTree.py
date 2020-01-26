class BIT:
            
    def __init__(self, L):
        self.N = len(L)
        self.bit = [0]*self.N
        for i,l in enumerate(L):
            self.add(i,l)
        self.N0 = 1
        while self.N0*2 <= self.N:
            self.N0 *= 2

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

    #you can use this function when the BIT has only non-negative values.
    def lower_bound(self, w):
        if w<=0:
            return 0
        x = 0
        k = self.N0
        while k>0:
            if x+k<=self.N:
                if self.bit[x+k-1]<w:
                    w-=self.bit[x+k-1]
                    x+=k
            k//=2
        return x+1
