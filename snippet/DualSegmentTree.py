class DualSegmentTree:
    def __init__(self, n) :
        self.n = n
        self.N0 = 1 << n.bit_length()
        self.data = [10**15] * (self.N0*2)
 
    def update(self, l, r, val) :
        l += self.N0
        r += self.N0
        while l < r:
            if l & 1:
                self.data[l] = min(self.data[l], val)
                l += 1
            if r & 1:
                self.data[r-1] = min(self.data[r-1], val)
                r -= 1
            l //= 2
            r //= 2
 
    def query(self, i):
        i += len(self.data) // 2
        ret = self.data[i]
        while i > 0:
            i //= 2
            ret = min(ret, self.data[i])
        return ret if ret < 10**15 else -1