#wrote this on my own- tricky one
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode(-101)
        head  = merged
        if list1 is None: return list2
        if list2 is None: return list1

        while list1 and list2:

            if list1.val <= list2.val:
                merged.next = list1
                merged = merged.next
                list1 = list1.next
            else: 
                merged.next = list2
                merged = merged.next
                list2 = list2.next

        merged.next = list2 or list1
        return head.next