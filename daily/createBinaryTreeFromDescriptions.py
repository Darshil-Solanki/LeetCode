# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        is_child = defaultdict(bool)

        for u, v, is_left in descriptions:
            if u not in nodes:
                nodes[u] = TreeNode(u)
            if v not in nodes:
                nodes[v] = TreeNode(v)
            is_child[v] = True

            if is_left:
                left_node = nodes[v]
                nodes[u].left = left_node
            else:
                right_node = nodes[v]
                nodes[u].right = right_node

        for node in nodes.keys():
            if not is_child[node]:
                return nodes[node]
