# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow
        prev = None
        while curr:
            node = curr.next
            curr.next, prev, curr = prev, curr, node
        sum = 0
        while prev:
            if head.val+prev.val>sum: sum = head.val+prev.val
            head = head.next
            prev = prev.next
        return sum

    # def pairSum(self, head: Optional[ListNode]) -> int:
    #     prev_node = None
    #     curr_node = head
    #     tail_node = head
    #     while tail_node:
    #         tail_node = tail_node.next.next
    #         curr_node.next, prev_node, curr_node = prev_node, curr_node, curr_node.next

    #     reversed_node = prev_node
    #     prev_node = curr_node
    #     best_sum = 0
    #     while curr_node:
    #         curr_sum = reversed_node.val + curr_node.val
    #         if curr_sum > best_sum:
    #             best_sum = curr_sum
            
    #         curr_node = curr_node.next
    #         reversed_node.next, prev_node, reversed_node = prev_node, reversed_node, reversed_node.next
        
    #     return best_sum
