import math

class Solution:
    def countNumbers(self, n):
        primes = self._sieve(int(math.sqrt(n)) + 1)
        prime_set = set(primes)
        count = 0


        for p in primes:
            if p**8 <= n:
                count += 1
            else:
                break

        
        size = len(primes)
        for i in range(size):
            for j in range(i+1, size):
                val = (primes[i]**2) * (primes[j]**2)
                if val <= n:
                    count += 1
                else:
                    break

        return count

    def _sieve(self, limit):
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, limit + 1, i):
                    is_prime[j] = False
        return [i for i, prime in enumerate(is_prime) if prime]
