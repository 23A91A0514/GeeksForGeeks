class Solution:    
    def findUnion(self, a, b):
        l = set(a)
        l1 = set(b)
        return l.union(l1)
