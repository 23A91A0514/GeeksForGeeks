from collections import Counter

class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        l = Counter(arr)   # O(n) to build
        res = []

        # find the repeating element (count > 1)
        for num, cnt in l.items():   # iterate only over distinct elements
            if cnt > 1:
                res.append(num)
                break                 # stop after finding the repeating one

        # find the missing element (1..n)
        for i in range(1, n + 1):
            if i not in l:            # membership in Counter (dict) is O(1)
                res.append(i)
                break                 # stop after finding the missing one

        return res
