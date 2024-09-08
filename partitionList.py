# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return None
        copyHead = lowerList = greaterListHead = greaterList = None
        temp = head
        while temp:
            if temp.val<x:
                if not lowerList:
                    lowerList = ListNode(temp.val)
                    copyHead = lowerList
                else:
                    lowerList.next = ListNode(temp.val)
                    lowerList = lowerList.next
            else:
                if not greaterList:
                    greaterList = ListNode(temp.val)
                    greaterListHead = greaterList
                else:
                    greaterList.next = ListNode(temp.val)
                    greaterList = greaterList.next
            temp = temp.next
        if not lowerList:
            return greaterListHead
        if greaterListHead:
            lowerList.next = greaterListHead
        return copyHead

        # Better Way of doing samething with use of one dummy node at beginning
        # beforeHead = ListNode(0)
        # afterHead = ListNode(0)
        # before = beforeHead
        # after = afterHead

        # while head:
        #     if head.val < x:
        #         before.next = head
        #         before = head
        #     else:
        #         after.next = head
        #         after = head
        #     head = head.next

        # after.next = None
        # before.next = afterHead.next

        # return beforeHead.next
