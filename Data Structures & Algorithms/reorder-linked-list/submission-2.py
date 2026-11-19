# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow    
        slow = slow.next
        prev = None
        mid.next = None 
        new = slow

        while new:
            new = slow.next
            slow.next = prev
            prev = slow
            if new: slow = new

            
        curr = head
        while slow and curr is not mid:
            nxt = slow.next
            slow.next = curr.next
            curr.next = slow
            curr = curr.next.next
            slow = nxt





    