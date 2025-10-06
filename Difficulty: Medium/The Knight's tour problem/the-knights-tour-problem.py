class Solution:
    def knightTour(self, n):
        # code here
        di = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
        res = []
        def backtrack(pos, mat, step):
            if step == n ** 2:
                raise

            for dx, dy in di:
                nx, ny = pos[0] + dx, pos[1] + dy
                if nx < n and ny < n and nx >= 0 and ny >= 0 and mat[nx][ny] == -1:
                    mat[nx][ny] = step
                    backtrack((nx, ny), mat, step + 1)
                    mat[nx][ny] = -1

        mat = [[-1] * n for i in range(n)]
        mat[0][0] = 0
        try:
            backtrack((0, 0), mat, 1)
        except Exception:
            res = mat
        return res