class Solution:
    def maxProduct(self,arr):
        n = len(arr)
         
        max_ending_here = arr[0]
        min_ending_here = arr[0]
        ans = arr[0]
         
        for i in range(1,n):
            if arr[i] < 0:
                max_ending_here, min_ending_here = min_ending_here, max_ending_here
                
            max_ending_here = max(arr[i], max_ending_here * arr[i])
            min_ending_here = min(arr[i], min_ending_here * arr[i])
         
            ans = max(ans, max_ending_here)
         
        return ans