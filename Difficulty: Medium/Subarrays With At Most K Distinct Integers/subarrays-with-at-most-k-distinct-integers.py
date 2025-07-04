from collections import defaultdict

class Solution:
    def countAtMostK(self, arr, k):
        count = defaultdict(int)
        left = 0
        result = 0
        distinct = 0

        for right in range(len(arr)):
            if count[arr[right]] == 0:
                distinct += 1
            count[arr[right]] += 1

            while distinct > k:
                count[arr[left]] -= 1
                if count[arr[left]] == 0:
                    distinct -= 1
                left += 1

            result += right - left + 1 
        return result

        