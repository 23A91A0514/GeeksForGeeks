'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        # Step 1: Count number of 0s, 1s, and 2s
        count = [0, 0, 0]
        current = head

        while current:
            count[current.data] += 1
            current = current.next

        # Step 2: Overwrite the values in the linked list
        current = head
        i = 0
        while current:
            if count[i] == 0:
                i += 1
            else:
                current.data = i
                count[i] -= 1
                current = current.next

        return head
    