class Solution:
    def longestSubarray(self, arr, k):
        first_idx = {}
        s = res = 0
        for i, val in enumerate(arr):
            s += 1 if val > k else -1
            if s > 0:
                res = i + 1
            else:
                first_idx.setdefault(s, i)
                if (s - 1) in first_idx:
                    res = max(res, i - first_idx[s - 1])
        return res