class Solution:    
    def rotateDeque(self, dq, type, k):
        n=len(dq)
        if type==1:
            while(k):
                dq.appendleft(dq.pop())
                k-=1
        else:
            while(k):
                dq.append(dq.popleft())
                k-=1