class Solution:
    def reverse(self, head):
        if not head:
            return None

        current = head
        prev_node = None

        while current:
            current.prev, current.next = current.next, current.prev
            prev_node = current
            current = current.prev

        return prev_node
