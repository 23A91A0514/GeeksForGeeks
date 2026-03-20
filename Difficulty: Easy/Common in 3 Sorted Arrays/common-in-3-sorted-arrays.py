class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        k=set(arr1)
        l=set(arr2)
        o=set(arr3)
        
        return sorted(k & l & o)