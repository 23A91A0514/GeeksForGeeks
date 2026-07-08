from typing import List

class Solution:
    def findPair(self, arr: List[int], x: int) -> bool:
        arr.sort()
        n = len(arr)

        i, j = 0, 1

        while i < n and j < n:
            if i == j:
                j += 1
                continue

            diff = arr[j] - arr[i]

            if diff == x:
                return True
            elif diff < x:
                j += 1
            else:
                i += 1

        return False