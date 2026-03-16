#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        for i in arr:
            if i==k:
                return True
                break
        else:
            return False
        #Your code here