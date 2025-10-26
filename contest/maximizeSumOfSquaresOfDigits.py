class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum>num*9: return ""
        qut, rem = divmod(sum, 9)
        ans = "9"*qut + (str(rem) if rem else "")
        return ans + "0"*(num-len(ans))

        # self.ans = ""
        # self.m_square = 0
        
        # def backtrack(curr, rem, tot, square_tot):
        #     if rem<0:
        #         return
                
        #     if rem == 0:
        #         if square_tot>self.m_square and tot==sum:
        #             self.m_square = square_tot
        #             self.ans = "".join(curr)
        #         return
                
        #     if tot>sum:
        #         return
                
        #     for i in range(9, -1, -1):
        #         curr.append(str(i))
        #         backtrack(curr, rem-1, tot+i, square_tot+i*i)
        #         curr.pop()

        # backtrack([], num, 0, 0)
        # return self.ans
