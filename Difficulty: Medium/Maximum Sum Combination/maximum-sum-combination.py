import heapq

class Solution:
    def topKSumPairs(self, a, b, k):
        a.sort(reverse=True)
        b.sort(reverse=True)
        
        n = len(a)
        result = []
        max_heap = []
        visited = set()
        
        # Initial pair (0, 0)
        heapq.heappush(max_heap, (-(a[0] + b[0]), 0, 0))
        visited.add((0, 0))
        
        while k > 0 and max_heap:
            current_sum, i, j = heapq.heappop(max_heap)
            result.append(-current_sum)
            k -= 1
            
            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(max_heap, (-(a[i + 1] + b[j]), i + 1, j))
                visited.add((i + 1, j))
            
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(max_heap, (-(a[i] + b[j + 1]), i, j + 1))
                visited.add((i, j + 1))
        
        return result
