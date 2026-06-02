class Solution:
    def sumDiffPairs(self, arr, k):
        # code here
        arr.sort(reverse=True)
        s = 0
        while len(arr) > 1:
            if arr[0] - arr[1] < k:
                s += arr[0] + arr[1]
                arr.pop(0)
            arr.pop(0)
        return s