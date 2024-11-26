# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        copy = ListNode(head.val)
        copyHead = copy
        temp = head.next
        while temp:
            copy.next = ListNode(temp.val)
            copy = copy.next
            temp = temp.next
            length+=1
        if length==1: return None
        count=1
        if count==length+1-n: return copyHead.next
        temp = copyHead
        while head:
            if count==length-n:
                temp.next = temp.next.next
                break
            temp = temp.next
            head = head.next
            count+=1
        return copyHead

        # Better Solution with in-place removal
        # fast = slow = head
        # for _ in range(n):
        #     fast = fast.next
        # if not fast:
        #     return head.next
        # while fast.next:
        #     fast = fast.next
        #     slow = slow.next
        # slow.next = slow.next.next
        # return head
