class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        l=[]
        arr[:]=arr[-1:]+arr[0:]
        for i in range(1,len(arr)):
                    if arr[i]==i:
                         l.append(arr[i])
                
        return l 