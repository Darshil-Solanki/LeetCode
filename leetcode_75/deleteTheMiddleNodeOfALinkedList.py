# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if fast==slow:
            return
        prev.next=slow.next
        return head

        # better with dummy node
        # dummy = ListNode(0)
        # dummy.next = head
        # fast = head
        # slow = dummy

        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next


        # slow.next = slow.next.next

        # return dummy.next
