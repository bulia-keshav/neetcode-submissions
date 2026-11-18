# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        if not list1 and list2: return []

        dummyhead = ListNode(-101)
        dummyhead.next = list1
        curr = dummyhead

        while list2:
            if not curr.next:
                nxt = list2.next
                list2.next = curr.next
                curr.next = list2
                list2 = nxt

            elif list2.val  > curr.next.val :
                curr = curr.next
            else:
                nxt = list2.next
                list2.next = curr.next
                curr.next = list2
                list2 = nxt


        return dummyhead.next
        

