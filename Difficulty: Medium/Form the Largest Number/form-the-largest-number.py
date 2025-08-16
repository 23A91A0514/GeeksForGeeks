from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        # Convert all integers to strings for easy comparison
        arr = list(map(str, arr))
        
        # Define custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        # Sort using custom comparator
        arr.sort(key=cmp_to_key(compare))
        
        # Edge case: when all elements are 0 (e.g. [0, 0, 0])
        if arr[0] == '0':
            return '0'
        
        # Join and return the result
        return ''.join(arr)
