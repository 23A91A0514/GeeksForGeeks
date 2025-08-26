class Solution:
    def isSubSeq(self, s1, s2):
        i, j = 0, 0
        n1, n2 = len(s1), len(s2)

        while i < n1 and j < n2:
            if s1[i] == s2[j]:
                i += 1
            j += 1
        
        return i == n1
