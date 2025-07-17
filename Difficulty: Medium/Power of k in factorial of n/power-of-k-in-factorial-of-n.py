class Solution:
    def maxKPower(self, n, k):
        def prime_factors(x):
            factors = {}
            d = 2
            while d * d <= x:
                while x % d == 0:
                    factors[d] = factors.get(d, 0) + 1
                    x //= d
                d += 1
            if x > 1:
                factors[x] = 1
            return factors

        def count_in_factorial(n, p):
            count = 0
            power = p
            while power <= n:
                count += n // power
                power *= p
            return count

        k_factors = prime_factors(k)
        res = float('inf')
        for p, exp in k_factors.items():
            count = count_in_factorial(n, p)
            res = min(res, count // exp)
        return res
