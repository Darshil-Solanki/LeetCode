class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        left, right = bin(left)[2:], bin(right)[2:]
        if len(right)>len(left): return 0
        res, n ="", len(left)
        for i in range(n):
            if left[i]!=right[i]:
                break
            res+=left[i]
        return int(res+"0"*(n-len(res)), 2)

        # Better way of doing same thing in bit level using bit operation
        # count = 0
        # while left!=right:
        #     left >>= 1
        #     right >>= 1
        #     count += 1
        # return left<<count
