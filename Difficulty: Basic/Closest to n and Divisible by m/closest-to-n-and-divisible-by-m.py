
class Solution:
        def closestNumber(self, n, m):
            q = n // m

            a = q * m
            b = (q + 1) * m

            if abs(n - a) < abs(n - b):
                return a
            elif abs(n - a) > abs(n - b):
                return b
            else:
                return a if abs(a) > abs(b) else b