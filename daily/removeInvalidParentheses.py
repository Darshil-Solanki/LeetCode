class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left = right = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left == 0:
                    right += 1
                else: 
                    left -= 1
        
        self.ans = set()

        def dfs(depth, left, right, left_rem, right_rem, curr):
            if depth == len(s):
                if left == right and left_rem == right_rem == 0:
                    self.ans.add(curr)
            else:
                if s[depth] == "(" and left_rem>0:
                    dfs(depth+1, left, right, left_rem-1, right_rem, curr)
                
                if s[depth] == ")" and right_rem > 0:
                    dfs(depth+1, left, right, left_rem, right_rem-1, curr)
                
                if s[depth] != "(" and s[depth] != ")":
                    dfs(depth+1, left, right, left_rem, right_rem, curr+s[depth])
                elif s[depth] == "(":
                    dfs(depth+1, left+1, right, left_rem, right_rem, curr+"(")
                elif s[depth] == ")" and right<left:
                    dfs(depth+1, left, right+1, left_rem, right_rem, curr+")")
        
        dfs(0, 0, 0, left, right, "")
        return list(self.ans)
