class Solution:
    def canSplit(self, arr):
        tot=sum(arr)
        if tot%2==1:
            return False
        pre=0
        tar=tot//2
        for i in range(len(arr)):
             pre+=arr[i]
             if pre==tar:
                 return True
        return False
            
        #code here