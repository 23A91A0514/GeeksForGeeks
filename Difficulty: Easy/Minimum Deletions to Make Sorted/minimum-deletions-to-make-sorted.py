from bisect import bisect_left

class Solution:
    def minDeletions(self, arr):
        lis = []

        for x in arr:
            pos = bisect_left(lis, x)

            if pos == len(lis):
                lis.append(x)
            else:
                lis[pos] = x

        return len(arr) - len(lis)