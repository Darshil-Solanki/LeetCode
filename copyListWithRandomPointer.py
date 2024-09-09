"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        copy = head
        while copy:
            node = copy.next
            copy.next = Node(copy.val)
            copy.next.next = node
            copy = node
        copy = head
        while copy:
            if copy.random:
                copy.next.random = copy.random.next
            copy = copy.next.next
        copy = head
        copyHead = head.next
        temp = copyHead
        while temp.next:
            copy.next = copy.next.next
            copy = copy.next
            
            temp.next = temp.next.next
            temp = temp.next
        return copyHead
