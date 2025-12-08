from collections import Counter
class Solution:
    def findDuplicates(self, arr):
        # code here
        l=Counter(arr)
        res=[]
        for i in l:
            if l[i]>1:
                res.append(i)
        return res
                
        