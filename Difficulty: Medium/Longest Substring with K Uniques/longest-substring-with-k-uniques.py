class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        if n == 0 or k == 0:
            return -1

        left = 0
        max_len = -1
        c_count = {}

        for i in range(n):
            c = s[i]
            c_count[c] = c_count.get(c, 0) + 1

            while len(c_count) > k:
                c_count[s[left]] -= 1
                if c_count[s[left]] == 0:
                    del c_count[s[left]]
                left += 1

            if len(c_count) == k:
                max_len = max(max_len, i - left + 1)

        return max_len