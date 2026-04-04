class Solution:
    def subArrayExists(self,arr):
        pref={}
        sum=0
        for i in range(len(arr)):
            sum+=arr[i]
            if sum==0:
                return True
            elif sum in pref:
                return True
            if sum not in pref:
                pref[sum]=True
                
        return False