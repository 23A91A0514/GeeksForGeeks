class Solution:
    def computeValue(self, n: int) -> int:
        MOD = 10**9 + 7
        fact = [1] * (2*n + 1)
        for i in range(1, 2*n + 1):
            fact[i] = (fact[i-1] * i) % MOD

        def modinv(x):
            return pow(x, MOD-2, MOD)

        numerator = fact[2*n]
        denominator = (fact[n] * fact[n]) % MOD
        return (numerator * modinv(denominator)) % MOD

