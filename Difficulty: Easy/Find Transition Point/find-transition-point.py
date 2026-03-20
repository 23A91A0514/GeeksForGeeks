class Solution:
    def transitionPoint(self, arr): 
        n=len(arr)
        for i in range(n):
            if arr[i]==1:
                return i
                break
        else:
            return -1
        # Code here