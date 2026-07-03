class Solution:
    def getPairs(self, arr):
        # code here
        res = set()
        set1 = set()
        
        for data in arr:
            if -data in set1:
                res.add((min(data,-data),max(data,-data)))
            
            set1.add(data)
        
        return sorted(list(res))