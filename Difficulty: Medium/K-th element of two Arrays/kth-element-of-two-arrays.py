class Solution:
    def kthElement(self, a, b, k):
        a.sort()
        b.sort()
        l=a+b
        l.sort()
        return l[k-1]
        # code here
        