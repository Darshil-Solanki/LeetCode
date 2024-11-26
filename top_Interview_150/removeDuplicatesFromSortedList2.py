# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        hold = head.val
        temp = head.next
        if not temp: return head
        copy = None
        copyHead = None
        flag = True
        while temp:
            if temp.val!=hold:
                if flag:
                    if not copy:
                        copy = ListNode(hold)
                        copyHead = copy
                    else:
                        copy.next = ListNode(hold)
                        copy = copy.next
                else:
                    flag = True
            else:
                flag = False
            hold = temp.val
            temp = temp.next
        if flag:
            if not copy:
                copyHead = ListNode(hold)
            else:
                copy.next = ListNode(hold)
        return copyHead

        # Better Solution in-place removal
        # sentinel = ListNode(0, head)
        # pred = sentinel

        # while head:
        #     if head.next and head.val == head.next.val:
        #         while head.next and head.val == head.next.val:
        #             head = head.next
        #         pred.next = head.next
            
        #     else:
        #         pred = pred.next
        #     head = head.next

        # return sentinel.next
