class Solution:
    def farMin(self, arr):
        n = len(arr)
        result = [-1] * n

        # Step 1: Preprocess right-side minimums
        right_min = [0] * n
        right_min[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right_min[i] = min(arr[i], right_min[i + 1])

        # Step 2: For each i, binary search for farthest j > i where arr[j] < arr[i]
        for i in range(n):
            low, high = i + 1, n - 1
            idx = -1
            while low <= high:
                mid = (low + high) // 2
                if right_min[mid] < arr[i]:
                    idx = mid  # Potential farthest found, but try farther
                    low = mid + 1
                else:
                    high = mid - 1
            result[i] = idx

        return result
