class Solution:
    def myAtoi(self, s):
        a=""
        s=s.strip()
        for i in s:
            if i.isalpha():
                break
            a+=i
        try:
            if int(a)>(2**31-1):
                return 2**31-1
            elif int(a)<-2**31:
                return -2**31
            else:
                return int(a)
        except:
            if len(a)<=1:
                return 0


        # code here
        