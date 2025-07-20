class TrieNode:
    def __init__(self):
        self.children = {}
        self.serial = ""

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        trie_root = TrieNode()
        for path in paths:
            curr_node = trie_root
            for folder in path:
                if folder not in curr_node.children:
                    curr_node.children[folder] = TrieNode()
                curr_node = curr_node.children[folder]
        
        freq = Counter()
        
        def dfs(node):
            if not node.children:
                return 
            
            temp = []
            for folder, child in node.children.items():
                dfs(child)
                temp.append(folder+"_"+child.serial+"_")
            
            temp.sort()
            node.serial = "".join(temp)
            freq[node.serial] += 1
        
        dfs(trie_root)
        ans = []
        temp_path = []
        def operate(node):
            if freq[node.serial]>1:
                return
            
            if temp_path:
                ans.append(temp_path[:])

            for folder, child in node.children.items():
                temp_path.append(folder)
                operate(child)
                temp_path.pop()
        
        operate(trie_root)
        return ans
