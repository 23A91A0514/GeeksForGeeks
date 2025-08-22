import bisect

class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        low = 1
        high = 2000
        
        while low < high:
            mid = (low + high) // 2
            count = 0
            
            for row in mat:
                # Count of elements ≤ mid in current row
                count += bisect.bisect_right(row, mid)
            
            if count < (n * m + 1) // 2:
                low = mid + 1
            else:
                high = mid
        
        return low
