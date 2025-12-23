import bisect

class Solution:
    def cntInRange(self, arr, queries):
        arr.sort()
        ans = []
        for a, b in queries:
            # count how many arr elements lie in [a, b]
            left = bisect.bisect_left(arr, a)
            right = bisect.bisect_right(arr, b)
            count = right - left
            ans.append(count)
        return ans