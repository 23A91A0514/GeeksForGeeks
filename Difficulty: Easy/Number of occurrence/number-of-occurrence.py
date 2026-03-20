class Solution:
    def countFreq(self, arr, target):
        # code here
        n = len(arr)
        count = 0
        for i in range(n):
            if(arr[i]==target):
                count+=1
        return count