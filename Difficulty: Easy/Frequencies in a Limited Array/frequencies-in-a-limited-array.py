class Solution:
    def frequencyCount(self, arr):
        n = len(arr)
        res = [0]*n
        
        for num in arr:
            res[num-1] += 1
        
        return res