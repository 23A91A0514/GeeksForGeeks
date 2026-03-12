class Solution:
    def getPairs(self, arr):
        seen = set()
        pairs = set()

        for x in arr:
            if -x in seen:
                pairs.add((min(x, -x), max(x, -x)))
            seen.add(x)

        res = [list(p) for p in pairs]
        res.sort()
        return res