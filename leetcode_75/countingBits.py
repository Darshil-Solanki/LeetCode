class Solution:
    def countBits(self, n: int) -> List[int]:
        one = 0
        ans = []
        for i in range(n+1):
            temp = 0
            tempn = i
            while tempn>0:
                tempn = tempn-(pow(2,floor(log(tempn,2))))
                temp+=1
            ans.append(temp)
        return ans

        # fastest method from submission
        # return [i.bit_count() for i in range(n+1)]

        # linear method without using inbuilt method from submission
        # if n == 0:
        #     return [0]
        # ans = [0, 1]
        # target = 2
        # curr = 0
        # i=2
        # while i <= n:
        #     ans.append(1 + ans[curr])
        #     curr += 1
        #     if curr == target:
        #         target *= 2
        #         curr = 0
        #     i+=1
        # return ans
