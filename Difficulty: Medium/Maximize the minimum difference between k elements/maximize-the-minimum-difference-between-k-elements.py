class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()

        def is_possible(min_diff):
            count = 1
            last = arr[0]
            for i in range(1, len(arr)):
                if arr[i] - last >= min_diff:
                    count += 1
                    last = arr[i]
                    if count == k:
                        return True
            return False

        left, right = 0, arr[-1] - arr[0]
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                answer = mid
                left = mid + 1  # try to increase the min difference
            else:
                right = mid - 1  # reduce the min difference

        return answer
