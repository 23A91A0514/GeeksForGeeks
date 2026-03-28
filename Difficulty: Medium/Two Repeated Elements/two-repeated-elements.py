class Solution:
    def twoRepeated(self, arr):
        l=[]
        s=set()
        for i in arr:
            if i not in  s:
                s.add(i)
            else:
                l.append(i)
        return l
        # code here
