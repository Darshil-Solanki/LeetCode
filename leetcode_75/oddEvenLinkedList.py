# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        dummyOdd, dummyEven = ListNode(0), ListNode(0)
        dummyOdd.next = dummyEven
        dummyEven.next = head
        evenhead = dummyEven
        while dummyEven and dummyEven.next:
            dummyOdd.next = dummyEven.next
            dummyOdd = dummyEven.next
            dummyEven.next = dummyOdd.next
            dummyEven = dummyOdd.next
        dummyOdd.next = evenhead.next
        return head

        # simpler and better version
        # odd = head
        # even = head.next
        # evenbase = even
        # while even and even.next:
        #     odd.next = even.next
        #     odd = odd.next
        #     even.next = odd.next
        #     even = even.next
        # odd.next = evenbase
        # return head
