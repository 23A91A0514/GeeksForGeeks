from collections import Counter
class Solution:
    def single(self, arr):
        count = Counter(arr)
        for key,val in count.items():
            if val == 1:
                return key