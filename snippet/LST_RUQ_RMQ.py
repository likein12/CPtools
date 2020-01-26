class LST_RUQ_RMQ:
    # Range Minimum Query
    def __init__(self, N):
        self.LV = (N-1).bit_length()
        self.N0 = 2**self.LV
        self.INF = 2**31 - 1
        self.data = [self.INF]*(2*self.N0)
        self.lazy = [None]*(2*self.N0)

    # 伝搬される区間のインデックス(1-indexed)を全て列挙するgenerator
    def gindex(self, l, r):
        L = l + self.N0; R = r + self.N0
        lm = (L // (L & -L)) >> 1
        rm = (R // (R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1; R >>= 1
        while L:
            yield L
            L >>= 1

    # 1-indexedで単調増加のインデックスリストを渡す
    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i-1]
            if v is None:
                continue
            self.lazy[2*i-1] = self.data[2*i-1] = self.lazy[2*i] = self.data[2*i] = v
            self.lazy[i-1] = None

    def update(self, l, r, x):
        *ids, = self.gindex(l, r)
        # 1. トップダウンにlazyの値を伝搬
        self.propagates(*ids)
    
        # 2. 区間[l, r)のdata, lazyの値を更新
        L = self.N0 + l; R = self.N0 + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] = self.data[R-1] = x
            if L & 1:
                self.lazy[L-1] = self.data[L-1] = x
                L += 1
            L >>= 1; R >>= 1

        # 3. 伝搬させた区間について、ボトムアップにdataの値を伝搬する
        for i in ids:
            self.data[i-1] = min(self.data[2*i-1], self.data[2*i])

    def query(self, l, r):
        # 1. トップダウンにlazyの値を伝搬
        self.propagates(*self.gindex(l, r))
        L = self.N0 + l; R = self.N0 + r

        # 2. 区間[l, r)の最小値を求める
        s = self.INF
        while L < R:
            if R & 1:
                R -= 1
                s = min(s, self.data[R-1])
            if L & 1:
                s = min(s, self.data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s
