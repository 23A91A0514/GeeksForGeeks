class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        if n == 0 or k == 0:
            return -1

        left = 0
        max_len = -1
        char_count = {}

        for right in range(n):
            char = s[right]
            char_count[char] = char_count.get(char, 0) + 1

            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            if len(char_count) == k:
                max_len = max(max_len, right - left + 1)

        return max_len