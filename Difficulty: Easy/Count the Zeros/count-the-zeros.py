#User function Template for python3

class Solution:
    def countZeroes(self, arr):
        c=0
        for i in arr:
            if i==0:
                c+=1
        return c
        # code here