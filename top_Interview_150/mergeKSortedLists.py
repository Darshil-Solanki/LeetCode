# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeList(lists):
            if len(lists)==1:
                return lists[0]
            if len(lists)>1:
                mid = len(lists)//2
                left = lists[:mid]
                right = lists[mid:]
                leftP = mergeList(left)
                rightP = mergeList(right)
                dummy = ListNode()
                mergeHead  = dummy
                while leftP and rightP:
                    if leftP.val < rightP.val:
                        dummy.next = ListNode(leftP.val)
                        leftP = leftP.next
                    else:
                        dummy.next = ListNode(rightP.val)
                        rightP = rightP.next
                    dummy = dummy.next
                while leftP:
                    dummy.next = ListNode(leftP.val)
                    leftP = leftP.next
                    dummy = dummy.next
                while rightP:
                    dummy.next = ListNode(rightP.val)
                    rightP = rightP.next
                    dummy = dummy.next
                return mergeHead.next
        return mergeList(lists)



        # # Create an empty heap
        # heap = []
        # for List in lists:
        #     pointer = List
        #     # Traverse the current linked list and push each node's value onto the heap
        #     while pointer:
        #         heappush(heap, pointer.val)
        #         pointer = pointer.next
        # # Create a dummy node to serve as the head of the merged linked list
        # dummy = ListNode(0)
        # curr = dummy
        # # Pop values from the heap and create nodes in the merged linked list
        # while len(heap)>0:
        #     curr.next = ListNode(heappop(heap))
        #     curr = curr.next
        # # Return the next node of the dummy node, which is the head of the merged linked list
        # return dummy.next

        # Runtime of this is more efficient(approx. same as Heap method) than divide and conquer method
        # newList = []
        # for i in lists:
        #     cur = i
        #     while cur:
        #         newList.append(cur.val)
        #         cur = cur.next
        # newList.sort()
        # if len(newList) == 0:
        #     return None
        # node = ListNode(newList[0])
        # cur = node
        # for i in range(1, len(newList)):
        #     cur.next = ListNode(newList[i])
        #     cur = cur.next
        # return node
