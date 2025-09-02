'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def swapKth(self, head, k):
        # Count total nodes
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        if k > n:
            return head
        
        if 2 * k - 1 == n:
            return head
        
        prevX = None
        currX = head
        for i in range(1, k):
            prevX = currX
            currX = currX.next
        
        prevY = None
        currY = head
        for i in range(1, n - k + 1):
            prevY = currY
            currY = currY.next
        
        if prevX:
            prevX.next = currY
        else:
            head = currY
        
        if prevY:
            prevY.next = currX
        else:
            head = currX
        
        currX.next, currY.next = currY.next, currX.next
        
        return head