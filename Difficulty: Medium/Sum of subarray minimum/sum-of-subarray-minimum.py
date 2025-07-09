class Solution:
    def sumSubMins(self, arr):
        MOD = 2**32
        n = len(arr)
        stack = []
        ple = [0] * n
        nle = [0] * n

        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            ple[i] = count
            stack.append((arr[i], count))

        stack = []

        for i in reversed(range(n)):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            nle[i] = count
            stack.append((arr[i], count))

        total = 0
        for i in range(n):
            total += arr[i] * ple[i] * nle[i]
        
        return total % MOD
