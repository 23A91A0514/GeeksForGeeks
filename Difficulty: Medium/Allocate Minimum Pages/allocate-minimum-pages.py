class Solution:
    def alot(self,arr,mid,k):
        st=1
        page=0
        for i in arr:
            if page+i>mid:
                st+=1
                page=0
            page+=i
            if st>k:
                return False
        return True
        
    def findPages(self, arr, k):
        if k>len(arr):
            return -1
        low=max(arr)
        high=sum(arr)
        res=high
        while low<=high:
            mid=(low+high)//2
            if self.alot(arr,mid,k):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res
                