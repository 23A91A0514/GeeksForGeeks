class Solution:
    def isValid(self, s):
        has_leading_zero = any(part.startswith("0") and len(part) > 1 for part in s.split(".")
)       
        s=s.split('.')
        if len(s)!=4:
            return False
        elif len(s)==4:
            if has_leading_zero:
                return False
            for i in s:
                if i=='' or int(i)>255:
                    return False
            return True
        return False

