class Solution:
    def find(self, arr, x):
        fidex = -1
        for i in range(len(arr)):
            if arr[i] == x:
                fidex = i
                break

        lidex = -1
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == x:
                lidex = i
                break

        return (fidex, lidex)