# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, head):
        count, temp = 0, head
        while temp:
            count+=1
            temp = temp.next
        return count

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        length = self.getLength(head)
        rotate = k % length
        if not rotate: return head
        count, temp = 0, head
        copyHead = None
        while temp:
            count+=1
            if count == length-rotate:
                copyHead = temp.next
                temp2 = temp.next
                temp.next=None
                while temp2.next:
                    temp2 = temp2.next
                temp2.next = head
                break
            temp = temp.next
        return copyHead           
    
    # Clean code
    # def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     if not head or not head.next or k == 0:
    #         return head

    #     # Find the length of the list and the tail node
    #     length = 1
    #     tail = head
    #     while tail.next:
    #         tail = tail.next
    #         length += 1

    #     # Normalize k in case it's greater than the length of the list
    #     k = k % length

    #     if k == 0:
    #         return head

    #     # Find the new tail position and rotate the list
    #     new_tail_pos = length - k
    #     current = head
    #     for _ in range(new_tail_pos - 1):
    #         current = current.next

    #     new_tail = current
    #     new_head = current.next

    #     # Perform the rotation
    #     new_tail.next = None
    #     tail.next = head

    #     return new_head
