class Solution:
    def maxCircularSum(self, arr):
        def kadane(nums):
            max_current = max_global = nums[0]
            for x in nums[1:]:
                max_current = max(x, max_current + x)
                max_global = max(max_global, max_current)
            return max_global

        def min_kadane(nums):
            min_current = min_global = nums[0]
            for x in nums[1:]:
                min_current = min(x, min_current + x)
                min_global = min(min_global, min_current)
            return min_global

        total_sum = sum(arr)
        max_kadane = kadane(arr)
        min_kadane_val = min_kadane(arr)

        if max_kadane < 0:
            return max_kadane
        return max(max_kadane, total_sum - min_kadane_val)
