class Solution:
    def utility(self, a, b, opr):
        # code here
        if opr==1:
            print(int(a+b))
        elif opr == 2:
            print(int(a-b))
        elif opr==3:
            print(int(a*b))
        else:
            print("Invalid Input")

