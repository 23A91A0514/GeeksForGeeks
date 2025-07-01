from collections import defaultdict

class Solution:
    def substrCount(self, s, k):
        if k > len(s):
            return 0

        count = 0
        freq = defaultdict(int)
        distinct = 0

        
        for i in range(k):
            if freq[s[i]] == 0:
                distinct += 1
            freq[s[i]] += 1

        if distinct == k - 1:
            count += 1

         
        for i in range(k, len(s)):
            out_char = s[i - k]
            freq[out_char] -= 1
            if freq[out_char] == 0:
                distinct -= 1

            in_char = s[i]
            if freq[in_char] == 0:
                distinct += 1
            freq[in_char] += 1

            if distinct == k - 1:
                count += 1

        return count
