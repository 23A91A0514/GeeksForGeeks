import math

class Solution:
    def minSoldiers(self, arr, k):
        n = len(arr)
        lucky_count = 0
        additions = []

        for num in arr:
            remainder = num % k
            if remainder == 0:
                lucky_count += 1
            else:
                additions.append(k - remainder)

        required_lucky = math.ceil(n / 2)
        troops_needed = required_lucky - lucky_count

        if troops_needed <= 0:
            return 0

        additions.sort()
        return sum(additions[:troops_needed])
