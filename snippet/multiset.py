from heapq import heappop, heappush
from collections import defaultdict

class multiset:
    def __init__(self, l = []):
        self.heap = []
        for x in l:
            heappush(self.heap, x)
        self.hashmap = defaultdict(int)
        for x in l:
            self.hashmap[x] += 1
        self.erased = defaultdict(int)
    
    def insert(self, x):
        heappush(self.heap, x)
        self.hashmap[x] += 1
        
    def erase(self, x):
        self.erased[x] += 1
        self.hashmap[x] -= 1
        if self.hashmap[x] == 0:
            self.hashmap.pop(x)

    def count(self, x):
        return self.hashmap[x]
    
    def contains(self, x):
        flag = self.hashmap[x] > 0
        if self.hashmap[x] == 0:
            self.hashmap.pop(x)
        return flag
    
    def begin(self):
        while self.erased[self.heap[0]]>0:
            x = self.heap[0]
            heappush(self.heap)
            self.erased[x] -= 1
        return self.heap[0]

        