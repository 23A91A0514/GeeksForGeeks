class Solution:
    def removeUtil (self, S):
        s=list(S)
        while 1:
            lth=len(s)
            tmp=[1]*lth
            for ix in range(1,lth):
                if s[ix]==s[ix-1]:
                    tmp[ix]+=tmp[ix-1]
            ret=[]
            ix=lth-1
            while ix>=0:
                if tmp[ix]==1:
                    ret.append(s[ix])
                ix-=tmp[ix]
            s=ret[::-1]
            if len(s)==lth:
                break
        return ''.join(s)