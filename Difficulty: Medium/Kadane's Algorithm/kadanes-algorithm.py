class Solution:
    def maxSubarraySum(self, arr):
        # Initialize both variables with the first element of the array
        maxi = arr[0]
        cur = arr[0]
        
        # Start looping from the second element (index 1)
        for i in range(1, len(arr)):
            # Decide: Is it better to add the current number to our running total, 
            # or start a brand new subarray starting exactly at this number?
            cur = max(arr[i], cur + arr[i])
            
            # Update the global maximum if our current running total is higher
            maxi = max(maxi, cur)
            
        return maxi