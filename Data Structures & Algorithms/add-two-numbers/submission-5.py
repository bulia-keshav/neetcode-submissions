# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        n = 0
        n1= 0
        n2 = 0 
        while curr1:
            
            n1 += curr1.val*((10)**n)


            curr1 = curr1.next
            n +=1
        n = 0    
        while curr2:
            n2 += curr2.val*((10)**n)

            curr2 = curr2.next
            n +=1
        n3 = n1+n2

        out = ListNode(0)
        curr = out
        for i in str(n3)[::-1]:
            curr.next = ListNode(i)
            curr = curr.next

        return out.next



