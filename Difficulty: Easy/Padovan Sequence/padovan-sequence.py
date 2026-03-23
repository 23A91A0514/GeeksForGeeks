class Solution:
    def padovanSequence(self, n):
        mod = 10**9 + 7
        
        # Base cases
        if n <= 2:
            return 1
        
        a, b, c = 1, 1, 1  # P(0), P(1), P(2)
        
        for i in range(3, n + 1):
            d = (a + b) % mod
            a, b, c = b, c, d
        
        return c