class Solution:
    def mergeArrays(self, a, b):
        # code here
        n = len(a)
        m = len(b)
        
        end, start = len(a)-1, 0
        
        while a[end] > b[start]:
            
            temp = a[end]
            a[end] = b[start]
            b[start] = temp
            
            end -= 1
            start += 1
            
            if end < 0 or start == m:
                break
            
        a.sort() # nlogn
        b.sort() # mlogn