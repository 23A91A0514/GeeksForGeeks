from collections import Counter

class Solution:
    def isSubset(self, a, b):
        ca = Counter(a)
        cb = Counter(b)
        
        for i in cb:
            if cb[i] > ca[i]:
                return False
        
        return True