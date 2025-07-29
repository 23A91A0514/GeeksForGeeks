class Solution:
    def asciirange(self, s):
        from collections import defaultdict
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
        res = []
        for ch in first:
            if first[ch] != last[ch] and last[ch] - first[ch] > 1:
                total = sum(ord(s[i]) for i in range(first[ch] + 1, last[ch]))
                if total > 0:
                    res.append(total)
        return res
