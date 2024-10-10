# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next        # Move slow pointer one step
            fast = fast.next.next   # Move fast pointer two steps
            
            if slow == fast:        # Cycle detected
                return True
        
        return False  # No cycle
