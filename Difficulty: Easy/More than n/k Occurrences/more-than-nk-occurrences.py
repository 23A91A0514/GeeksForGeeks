from collections import Counter

class Solution:
    def countOccurence(self, arr, k):
        n = len(arr)
        threshold = n // k
        
        freq = Counter(arr)
        
        count = 0
        for val in freq.values():
            if val > threshold:
                count += 1
                
        return count