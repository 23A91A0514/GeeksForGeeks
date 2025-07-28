class Solution:
    def balanceSums(self, mat):
        n = len(mat)
        row_sum = [sum(row) for row in mat]
        col_sum = [sum(mat[i][j] for i in range(n)) for j in range(n)]
        
        max_sum = max(max(row_sum), max(col_sum))
        
        total_operations = 0
        for i in range(n):
            for j in range(n):
                # The minimum of how much we can increase this cell to help both row and column
                target = min(max_sum - row_sum[i], max_sum - col_sum[j])
                mat[i][j] += target
                row_sum[i] += target
                col_sum[j] += target
                total_operations += target
                
        return total_operations
