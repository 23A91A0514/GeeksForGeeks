class Solution {
    private long gcd(long a, long b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    private long lcm(long a, long b) {
        return (a / gcd(a, b)) * b;
    }

    private long lcm3(long a, long b, long c) {
        return lcm(lcm(a, b), c);
    }

    int lcmTriplets(int n) {
        if (n <= 2) return n;
        long result;

        if (n % 2 != 0) {
            result = lcm3(n, n - 1, n - 2);
        } else {
            if (n % 3 != 0) {
                result = lcm3(n, n - 1, n - 3);
            } else {
                result = lcm3(n - 1, n - 2, n - 3);
            }
        }

        return (int) result;
    }
}
