class Solution:
    def minOperations(self, s: str) -> int:
        flag = True
        op1, op2 = 0, 0
        for c in s:
            if flag:
                if c=="1":
                    op1+=1
                else:
                    op2+=1
            else:
                if c=="0":
                    op1+=1
                else:
                    op2+=1
            flag = not flag
        
        return min(op1, op2)
