# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = l1.val+l2.val
        newLi = ListNode(n%10 if n>9 else n)
        temp = newLi
        carry = 1 if n>9 else 0
        l1, l2 = l1.next, l2.next
        while l1 and l2:
            n = l1.val+l2.val+carry
            node = ListNode(n%10 if n>9 else n)
            carry = 1 if n>9 else 0
            l1, l2 = l1.next, l2.next
            temp.next=node
            temp = node
        if not l1 and not l2 and carry:
            temp.next =  ListNode(1)
        while l1:
            n = l1.val+carry
            node = ListNode(n%10 if n>9 else n)
            carry = 1 if n>9 else 0
            l1 = l1.next
            temp.next=node
            temp = node
            if not l2 and carry:
                temp.next =  ListNode(1)
        while l2:
            n = l2.val+carry
            node = ListNode(n%10 if n>9 else n)
            carry = 1 if n>9 else 0
            l2 = l2.next
            temp.next=node
            temp = node
            if not l2 and carry:
                temp.next =  ListNode(1)
        return newLi
