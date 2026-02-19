class Solution:
    def missingRange(self, arr, low, high):
        arr_set = set(arr)   # O(n)
        result = []

        for i in range(low, high + 1):  # O(high - low)
            if i not in arr_set:         # O(1)
                result.append(i)

        return result
