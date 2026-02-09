class Solution:
    def findKRotation(self, arr):
        if arr == sorted(arr):  # Check if already sorted
            return 0
        for i in range(len(arr)):
            if arr[i] > arr[(i + 1) % len(arr)]:  # Find drop point
                return i + 1
        return 0
