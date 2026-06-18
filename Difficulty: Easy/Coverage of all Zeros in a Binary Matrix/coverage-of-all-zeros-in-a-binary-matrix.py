class Solution:
    def findCoverage(self, mat):
        rows, cols = len(mat), len(mat[0])
        result = 0

        def fun(is_row, fixed_index, start, end):
            for idx in range(start, end):
                if is_row and mat[fixed_index][idx]:
                    return 1
                elif not is_row and mat[idx][fixed_index]:
                    return 1
            return 0

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    result += fun(1, r, 0, c)         # left
                    result += fun(1, r, c + 1, cols)  # right
                    result += fun(0, c, 0, r)         # up
                    result += fun(0, c, r + 1, rows)  # down

        return result