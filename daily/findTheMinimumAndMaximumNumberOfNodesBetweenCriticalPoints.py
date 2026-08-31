# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr = head
        critical_points = []
        prev = None
        i = 0
        while curr:
            if prev and curr.next:
                if prev.val<curr.val>curr.next.val:
                    critical_points.append(i)
                if prev.val>curr.val<curr.next.val:
                    critical_points.append(i)
            prev = curr
            curr = curr.next
            i += 1
        
        if  len(critical_points)<2:
            return [-1, -1]
        
        return [min(b-a for a, b in pairwise(critical_points)), critical_points[-1]-critical_points[0]]
