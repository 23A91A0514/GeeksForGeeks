class Solution:
    def maxSum(self, arr):
        n = len(arr)
        max_sum = 0
        
        for i in range(n - 1):
            # Subarray of size 2
            max_sum = max(max_sum, arr[i] + arr[i + 1])
            
            # Subarray of size 3
            if i + 2 < n:
                sub = [arr[i], arr[i+1], arr[i+2]]
                sub.sort()
                max_sum = max(max_sum, sub[0] + sub[1])
        
        return max_sum
