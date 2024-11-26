# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums==[]:
            return None
        root = None
        left, right = 0, len(nums)
        mid=(left+right)//2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:]) 
        return root

    # def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    #     def convert(left: int, right: int) -> TreeNode:
    #         if left > right:
    #             return None
            
    #         mid = (left + right) // 2
    #         node = TreeNode(nums[mid])
    #         node.left = convert(left, mid - 1)
    #         node.right = convert(mid + 1, right)
            
    #         return node
        
    #     return convert(0, len(nums) - 1)
