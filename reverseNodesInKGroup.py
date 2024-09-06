# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        copy = None
        copyHead = None
        while head:
            stack = []
            count = 0
            while head and count!=k:
                stack.append(head.val)
                head = head.next
                count+=1
            if len(stack)==k:
                while stack:
                    node = ListNode(stack.pop())
                    if not copyHead:
                        copy = copyHead = node
                    else:
                        copy.next = node
                        copy = copy.next
            else:
                while stack:
                    copy.next = ListNode(stack.pop(0))
                    copy = copy.next
            count = 0
        return copyHead
    
    # Better in-place solution
    # def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     if head is None or k == 1:
    #         return head

    #     # Dummy node initialization
    #     dummy = ListNode(0)
    #     dummy.next = head
    #     ptr = dummy

    #     while ptr is not None:
    #         tracker = ptr

    #         # Check if there are at least k nodes ahead
    #         for i in range(k):
    #             tracker = tracker.next
    #             if tracker is None:
    #                 return dummy.next

    #         # Reverse the k nodes
    #         previous, current = self.reverseLinkedList(ptr.next, k)

    #         # Link the reversed part back to the main list
    #         lastNodeOfReversedGroup = ptr.next
    #         lastNodeOfReversedGroup.next = current
    #         ptr.next = previous
    #         ptr = lastNodeOfReversedGroup

    #     return dummy.next

    # def reverseLinkedList(self, head: ListNode, k: int) -> Tuple[ListNode, ListNode]:
    #     previous = None
    #     current = head

    #     for _ in range(k):
    #         # Temporarily store the next node
    #         next_node = current.next
    #         # Reverse the current node
    #         current.next = previous
    #         # Move previous and current one step forward
    #         previous = current
    #         current = next_node

    #     # Return the new head and the next pointer for further operations
    #     return previous, current
