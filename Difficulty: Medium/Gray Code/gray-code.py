class Solution:
    def graycode(self,n):
        #code here
        if n == 1:
            return ["0", "1"]
        prev = self.graycode(n - 1)
        return ["0" + code for code in prev] + ["1" + code for code in reversed(prev)]
    