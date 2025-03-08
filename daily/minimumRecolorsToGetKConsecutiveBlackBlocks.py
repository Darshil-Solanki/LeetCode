class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w = 0
        for i in range(k):
            if blocks[i]=="W":
                w+=1
                
        if not w: return 0
        left = 0
        ans = w
        for right in range(k, len(blocks)):
            if blocks[right]=="W":
                w+=1
            if blocks[left]=="W":
                w-=1
            left+=1
            if w<ans:ans = w 
            
        return ans
