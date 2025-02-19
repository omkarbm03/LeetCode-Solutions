from typing import Optional

# Define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        # Traverse the linked list
        while curr:
            # Store the next node temporarily to avoid losing the reference
            temp = curr.next
            # Reverse the direction of the current node's pointer
            curr.next = prev
            # Move prev and curr pointers one step forward
            prev = curr
            curr = temp
        
        # At the end, prev will point to the new head of the reversed list
        return prev

# Helper function to convert a Python list to a linked list
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a Python list (for visualization)
def linkedlist_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

# Example Usage
solution = Solution()
input_list = [1, 2, 3, 4, 5]

# Convert the Python list to a linked list
head = list_to_linkedlist(input_list)

# Reverse the linked list
reversed_head = solution.reverseList(head)

# Convert the reversed linked list back to a Python list for visualization
reversed_list = linkedlist_to_list(reversed_head)

print("Reversed List:", reversed_list)  # Output: [5, 4, 3, 2, 1]