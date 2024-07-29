# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if  list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val<=list2.val:
            temp = list1
            list1 = list1.next
        else:
            temp = list2
            list2 = list2.next
        
        temphead = temp
        while list1!=None and list2!=None:
            if list1.val<=list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next=list2
                list2 = list2.next
            temp = temp.next
            
        if list1:
            while list1!=None:
                temp.next=list1
                list1=list1.next
                temp = temp.next
        if list2:
            while list2!=None:
                temp.next=list2
                list2=list2.next
                temp = temp.next
        return temphead
        
        
