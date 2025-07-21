class Solution {
    static final int MAX = 10001;

    public int cntCoprime(int[] arr) {
        int[] freq = new int[MAX];
        for (int num : arr) {
            freq[num]++;
        }

        int[] countMultiples = new int[MAX];
        for (int i = 1; i < MAX; i++) {
            for (int j = i; j < MAX; j += i) {
                countMultiples[i] += freq[j];
            }
        }

        int[] mobius = getMobius(MAX - 1);

        long res = 0;
        for (int i = 1; i < MAX; i++) {
            if (mobius[i] == 0) continue;
            long c = countMultiples[i];
            res += mobius[i] * (c * (c - 1) / 2);
        }

        return (int) res;
    }

    // Sieve to compute Möbius function
    private int[] getMobius(int n) {
        int[] mobius = new int[n + 1];
        boolean[] isPrime = new boolean[n + 1];
        for (int i = 0; i <= n; i++) {
            mobius[i] = 1;
            isPrime[i] = true;
        }

        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i; j <= n; j += i) {
                    mobius[j] *= -1;
                    isPrime[j] = false;
                }
                long square = 1L * i * i;
                for (int j = (int) square; j <= n; j += square) {
                    mobius[j] = 0;
                }
            }
        }

        return mobius;
    }
}
