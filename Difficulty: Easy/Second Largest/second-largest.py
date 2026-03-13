class Solution:
    def getSecondLargest(self, arr):
        n=len(arr)
        large=arr[0]
        second=-1
        for i in range(1,n):
            if arr[i]>large:
                large=arr[i]
        for i in range(n):
            if arr[i]>second and arr[i]< large:
                second=arr[i]
        return second