class Solution:
    def maxLength(self, arr):
        mx=0
        sm=0
        seen={0:-1}
        for ix,ve in enumerate(arr):
            sm+=ve
            if sm in seen:
                mx=max(mx,ix-seen[sm])
            if sm not in seen:
                seen[sm]=ix
        return mx