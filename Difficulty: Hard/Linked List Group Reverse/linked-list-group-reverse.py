"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""

class Solution:
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head

        # Helper to reverse k nodes and return new head and tail
        def reverse_k_nodes(start, k):
            prev = None
            curr = start
            count = 0
            while curr and count < k:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                count += 1
            return prev, start, curr  # new head, new tail, next group's start

        dummy = Node(0)
        dummy.next = head
        prev_tail = dummy
        current = head

        while current:
            # Check how many nodes remain
            temp = current
            count = 0
            while temp and count < k:
                temp = temp.next
                count += 1

            # Even if less than k, we still reverse (as per updated rule)
            new_head, new_tail, next_group = reverse_k_nodes(current, count)
            prev_tail.next = new_head
            new_tail.next = next_group
            prev_tail = new_tail
            current = next_group

        return dummy.next