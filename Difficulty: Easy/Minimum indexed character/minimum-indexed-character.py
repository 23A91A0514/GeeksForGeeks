class Solution:
    def minIndexChar(self,s1,s2):
        for ch in s1:
            if ch in s2:
                output=s1.index(ch)
                return output

        else:
            return -1