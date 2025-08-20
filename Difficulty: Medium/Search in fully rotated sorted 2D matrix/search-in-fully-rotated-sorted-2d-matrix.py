class Solution:
    def searchMatrix(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        left = 0
        right = n * m - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // m
            col = mid % m
            mid_val = mat[row][col]

            if mid_val == x:
                return True
            if mat[left // m][left % m] <= mid_val:
                if mat[left // m][left % m] <= x < mid_val:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if mid_val < x <= mat[right // m][right % m]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
