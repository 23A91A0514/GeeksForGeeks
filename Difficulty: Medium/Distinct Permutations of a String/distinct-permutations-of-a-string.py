class Solution:
    def findPermutation(self, s):
        # Code here
        res=set()
        l=list(s)
        n=len(l)
        def per(fi):
            if fi==n-1:
                res.add("".join(l))
                return
            for i in range(fi,n):
                l[fi],l[i]=l[i],l[fi]
                per(fi+1)
                l[fi],l[i]=l[i],l[fi]
        
        per(0)
        return sorted(res)