

from collections import Counter
class Solution:
    def removeDuplicates(self, s):
        freq=Counter(s)
        res=""
        for key,value in freq.items():
            if value!=2:
                res=res+key
            else:
                res=res+key
        return res