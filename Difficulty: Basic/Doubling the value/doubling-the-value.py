class Solution:
    def solve(self, b, a):
        for ele in a:
            if ele == b:
                b *= 2
        return b