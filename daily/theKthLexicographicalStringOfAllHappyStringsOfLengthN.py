class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        charset = "abc"
        self.ans = ""
        self.count = 0

        def backtrack(curr, last):
            if len(curr)==n:
                self.count+=1
                if self.count==k: self.ans = curr
                return 
            for c in charset:
                if c!=last:
                    backtrack(curr+c, c)

        backtrack("", "")
        return self.ans


        # faster method from submission
        # totalHappy = 3 * (2**(n-1))
        # if k > totalHappy:
        #     return ""
        
        # output = ""
        # choices = "abc"
        # low, high = 1, totalHappy
        # for i in range(n):
        #     partitionSize = (high - low + 1) // len(choices)
        #     cur = low
        #     for c in choices:
        #         if k in range(cur, cur + partitionSize):
        #             output += c
        #             low = cur
        #             high = cur + partitionSize - 1
        #             choices = "abc".replace(c, "")
        #             break
        #         cur += partitionSize
        # return output
