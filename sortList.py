# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeSort(self, head):
        if not head.next: return head
        slow = head
        fast = head
        prev = slow
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        head = self.mergeSort(head)
        slow = self.mergeSort(slow)
        return self.merge(head, slow)

    def merge(self, head, slow):
        dummy = ListNode()
        temp = dummy
        while head and slow:
            if head.val<=slow.val:
                dummy.next = head
                head = head.next
            else:
                dummy.next = slow
                slow = slow.next
            dummy = dummy.next
        
        while head:
            dummy.next = head
            head = head.next
            dummy = dummy.next

        while slow:
            dummy.next = slow
            slow = slow.next
            dummy = dummy.next
        
        return temp.next
            
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        return self.mergeSort(head)

    # # Better way of doing same thing
    # def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     # base case: node is empty or single-element
    #     if not head or not head.next:
    #         return head

    #     # find midpoint using fast+slow pointers
    #     slow = head
    #     fast = head.next
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
        
    #     # midpoint is slow.next
    #     mid = slow.next
    #     slow.next = None

    #     # recursively sort left and right halves
    #     left = self.sortList(head)
    #     right = self.sortList(mid)

    #     # merge sorted halves
    #     placeholder = ListNode()
    #     curr = placeholder
    #     while left and right:
    #         # left val should be merged next (after curr), then move up left
    #         if left.val < right.val:
    #             curr.next = left
    #             left = left.next
    #         # right val should be merged next
    #         else:
    #             curr.next = right
    #             right = right.next
    #         curr = curr.next
    #     # append remaining nodes from left or right half
    #     curr.next = left or right

    #     return placeholder.next  
