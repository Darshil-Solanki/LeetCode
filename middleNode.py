# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = head
        n=1
        while head.next!=None:
            n+=1
            mid = mid.next if not n%2 else mid
            head = head.next
        return mid
            
            
        
