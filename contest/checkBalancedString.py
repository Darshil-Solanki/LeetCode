class Solution:
    def isBalanced(self, num: str) -> bool:
        even, odd = int(num[0]), int(num[1])
        flag = True
        for i in range( 2, len(num)):
            if flag:
                even+=int(num[i])
                flag = False
            else:
                odd+=int(num[i])
                flag = True
        return even == odd
