''' Structure of linked list Node
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def removeDuplicates(head):
    temp = head
    
    while temp is not None and temp.next is not None:
        newDistinct = temp.next
        
        while newDistinct is not None and newDistinct.data == temp.data:
            newDistinct = newDistinct.next
            
        temp.next = newDistinct
        
        temp = temp.next
        
    return head

    #code here
    