class Solution:
    def findExtra(self,a,b):
        s1=set(a)
        s2=set(b)
        s3=s1-s2
        L=list(s3)
        if(L[0] in a):
              return a.index(L[0])