# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        newList = None
        temp = None
        while head is not None:
            if left==count:
                tempStack = []
                while count!=right+1:
                    tempStack.append(head.val)
                    head = head.next
                    count+=1
                if not newList:
                    newList = ListNode(tempStack.pop())
                    temp = newList
                while tempStack:
                    node = ListNode(tempStack.pop())
                    temp.next = node
                    temp = temp.next
            else:        
                if not newList:
                    newList = ListNode(head.val)
                    temp = newList
                else:
                    node = ListNode(head.val)
                    temp.next = node
                    temp = temp.next 
                head = head.next
                count+=1               
        return newList

        # Better inplace reverse method
        # cur = dummy = ListNode(next=head)
        # for _ in range(left-1):
        #     cur = cur.next
        # prev_end = cur
        # cur = cur.next
        # res = None
        # for _ in range(left, right+1):
        #     nxt, cur.next = cur.next, res
        #     cur, res = nxt, cur
        # prev_end.next.next = cur
        # prev_end.next = res
        # return dummy.next
