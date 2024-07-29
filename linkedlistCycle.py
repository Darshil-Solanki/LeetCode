# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        value = {}
        temp = head
        j=0
        while temp!=None:
            if temp.next in value.values():
                return True
            value[j]=temp
            j+=1
            temp=temp.next
        return False

# Better to use set for unique value instead dictionary
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         visited = set()
#         curr = head
#         while curr:
#             if curr in visited:
#                 return True
#             visited.add(curr)
#             curr = curr.next
#         return False
                
        
