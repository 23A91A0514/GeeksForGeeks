import heapq
from collections import Counter

class Solution:
    def topKFreq(self, arr, k):
        # Step 1: Count frequency of elements in arr using Counter
        freq = Counter(arr)
        
        # Step 2: Create a max-heap using negation of frequencies and elements
        heap = [(-val, -key) for key, val in freq.items()]
        
        # Step 3: Convert list into a heap (min-heap with negative values, so it behaves like a max-heap)
        heapq.heapify(heap)
        
        # Step 4: Extract top k frequent elements from the heap
        res = []
        for _ in range(k):
            val, key = heapq.heappop(heap)
            res.append(-key)  # Append the original element (negate it back)

        return res
