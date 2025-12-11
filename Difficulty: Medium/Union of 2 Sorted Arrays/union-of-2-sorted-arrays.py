class Solution:
    def findUnion(self, a, b):
        c=[]
        l=set(a).union(set(b))
        for i in l:
            c.append(i)
        c.sort()
        return c
        
        # code here 